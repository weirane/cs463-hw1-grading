import json
import sys
import unittest

from datetime import timedelta, datetime
from dateutil import parser
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner


def processor(data):
    # cleaning: remove paren at the end of test names
    for t in data['tests']:
        name = t['name']
        t['name'] = name[:name.find(' (')]

    # process late submissions
    print('Autograder raw score:', data['score'])
    filename = sys.argv[1]
    submit_time = filename[filename.find('_attempt_') + 9:].split('_')[0]
    submitted = datetime.strptime(submit_time, '%Y-%m-%d-%H-%M-%S')
    due = datetime(2023, 8, 31, 17, 0, 0)
    # with open('/autograder/submission_metadata.json') as f:
    #     meta = json.loads(f.read())
    # submitted = parser.parse(meta['created_at'])
    # due = parser.parse(meta['assignment']['due_date'])
    print('submitted', submitted)
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
        data['score'] = score
        print('Adjusted late score:', score)


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('tests')
    with open('/autograder/results/results.json', 'w') as f:
        JSONTestRunner(visibility='visible', stdout_visibility='visible',
                       post_processor=processor, stream=f).run(suite)
