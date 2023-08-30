import json
import unittest

from datetime import timedelta
from dateutil import parser
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner


def processor(data):
    # cleaning: remove paren at the end of test names
    for t in data['tests']:
        name = t['name']
        t['name'] = name[:name.find(' (')]

    # process late submissions
    print('Autograder raw score:', data['score'])
    with open('/autograder/submission_metadata.json') as f:
        meta = json.loads(f.read())
    submitted = parser.parse(meta['created_at'])
    due = parser.parse(meta['assignment']['due_date'])
    late = submitted - due
    if late > timedelta(hours=48, minutes=5):
        score = 0
        print('late', late)
    elif late > timedelta(hours=24, minutes=5):
        score = min(data['score'], 75)
        print('late', late)
    elif late > timedelta(minutes=5):
        score = min(data['score'], 90)
        print('late', late)
    else:
        score = data['score']

    if score < data['score']:
        print('Adjusted late score:', score)


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('tests')
    with open('/autograder/results/results.json', 'w') as f:
        JSONTestRunner(visibility='visible', stdout_visibility='visible',
                       post_processor=processor, stream=f).run(suite)
