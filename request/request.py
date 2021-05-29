TOKEN = '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'

import requests as req
import json

PREFIX = ['LEETCODE', 'GENERATOR', 'TRIANGLE', 'HEXNUMBER', 'ITERATOR', 'REQUESTS']
GROUP = ['1021', '1022']
ACTION = ['Added', 'Deleted', 'Refactored', 'Moved']


def get_all_user_prs(user_login, repo_name, pr_state):
    all_prs = req.get('https://api.github.com/repos/{}/{}/pulls?state={}'.format(user_login, repo_name, pr_state),
                      headers={'Authorization': 'Token{}'.format(TOKEN),
                               'Accept': "application/vnd.github.v3+json"}).json()
    return all_prs


def get_all_pr_commits(pr):
    all_pr_commits = req.get(pr['commits_url'], headers={'Authorization': 'Token{}'.format(TOKEN),
                                                         'Accept': "application/vnd.github.v3+json"}).json()
    return all_pr_commits


def get_titles(commit):
    titles = []
    titles.append(commit['commit']['message'])
    return titles


def check_prefixes(titles):
    faults = []
    for title in titles:
        title = title.replace('-', ' ')
        parsed_title = title.split(' ')
        if parsed_title[0] not in PREFIX:
            faults.append('Your task prefix should be one of the following: {}. \n'.format(PREFIX))
        if parsed_title[1] not in GROUP:
            faults.append('Your group should be one of the following: {}. \n'.format(GROUP))
        if parsed_title[2] not in ACTION:
            faults.append('Your action should be one of the following: {}.'.format(ACTION))
        if len(faults) == 0:
            return 'Respect from Damir'
        else:
            return '\n'.join(faults)


def send_pr_comment(pr, message_error):
    param = {'body': message_error,
             'path': req.get(pr['url'] + '/files', headers={'Authorization': 'Token{}'.format(TOKEN),
                                                            'Accept': "application/vnd.github.v3+json"}).json()[0][
                 'filename'],
             'position': 1,
             'commit_id': pr['head']['sha']}
    resp = req.post(pr['url'] + '/comments',
                    headers={'Authorization': 'Token{}'.format(TOKEN), 'Accept': "application/vnd.github.v3+json"},
                    json=param)
    return resp.json()


def verify_pr(pr):
    commits = get_all_pr_commits(pr)
    for commit in commits:
        titles = get_titles(commit)
        faults = check_prefixes(titles)
        send_pr_comment(pr, faults)


def main():
    user_login = 'OcTatiana'
    repo_name = 'python_au'
    pr_state = 'open'
    prs = get_all_user_prs(user_login, repo_name, pr_state)
    for pr in prs:
        verify_pr(pr)


if __name__ == '__main__':
    main()