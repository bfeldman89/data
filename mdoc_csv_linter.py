#!/usr/bin/env python
import os
import glob
import time
from github import Github
from goodtables import validate

ghub = Github(os.environ['GITHUB_USERNAME'], os.environ['GITHUB_PW'])

repo = ghub.get_repo('bfeldman89/data')

def lint_these_csvs(folders):
    for folder in folders:
        os.chdir(f"/Users/blakefeldman/code/data/mdoc/{folder}")
        files = glob.glob('*.csv')
        files.sort()
        for fn in files:
            report = validate(fn)
            if report['valid']:
                print(fn, 'is valid!')
            else:
                body_lst = ['# the following errors were identified']
                for error in report['tables'][0]['errors']:
                    body_lst.append(f"- [ ] {error['message']}")
                title_str = f"{folder}/{report['tables'][0]['source']} invalid"
                body_str = '\n'.join(body_lst)
                labels = ['invalid']
                repo.create_issue(title=title_str, body=body_str, labels=labels)
                time.sleep(1.5)
        print('done with', folder, '!')

dp_folders = """daily_pop
daily_pop/per_mo
daily_pop/raw
daily_pop/transposed""".splitlines()

mfs_folders = """monthly_fact_sheets
monthly_fact_sheets/community_corrections_pop_by_type
monthly_fact_sheets/corrections_pop_by_type
monthly_fact_sheets/inmate_pop_by_location
monthly_fact_sheets/inmate_pop_by_offense_and_location
monthly_fact_sheets/inmate_pop_by_race_and_sex
monthly_fact_sheets/inmate_pop_by_race_sex_and_location
monthly_fact_sheets/parole_pop_by_offense
monthly_fact_sheets/parole_pop_by_race_and_sex
monthly_fact_sheets/probation_pop_by_offense
monthly_fact_sheets/probation_pop_by_race_and_sex
monthly_fact_sheets/raw
monthly_fact_sheets/specific_offense_stats""".splitlines()

other_folders = ['annual_reports']

lint_these_csvs(folders=dp_folders)
lint_these_csvs(folders=mfs_folders)
lint_these_csvs(folders=other_folders)


open_issues = repo.get_issues(state='open')
for issue in open_issues:
    print(issue)
