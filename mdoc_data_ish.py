#!/usr/bin/env python
import os
import csv
import glob
import shutil
import time

import camelot
import pandas as pd

from airtable import Airtable
from documentcloud import DocumentCloud
from goodtables import validate

airtab = Airtable(os.environ['other_scrapers_db'],
                  'mdoc', os.environ['AIRTABLE_API_KEY'])

dc = DocumentCloud(username=os.environ['MUCKROCK_USERNAME'],
                   password=os.environ['MUCKROCK_PW'])


def get_raw_dp_csvs():
    os.chdir('/Users/blakefeldman/code/data/mdoc/daily_pop/raw')
    records = airtab.get_all(view='dp needs csv', fields=['url', 'iso', 'dc_pages'])
    for rec in records:
        fn = f"{rec['fields']['iso']}.csv"
        pages = f"1-{rec['fields']['dc_pages']}"
        url = rec['fields']['url']
        tables = camelot.read_pdf(url, pages=pages)
        tables.export(fn, f='csv')


def get_raw_mfs_csvs():
    os.chdir('/Users/blakefeldman/code/data/mdoc/monthly_fact_sheets/raw')
    records = airtab.get_all(view='mfs_needs_tables_extracted', fields=['url', 'iso', 'dc_pages'])
    for rec in records:
        fn = f"{rec['fields']['iso']}.csv"
        pages = f"1-{rec['fields']['dc_pages']}"
        url = rec['fields']['url']
        tables = camelot.read_pdf(url, flavor='stream', pages=pages)
        tables.export(fn, f='csv')


def transpose_raw_csvs():
    os.chdir('/Users/blakefeldman/code/data/mdoc/daily_pop')
    files = os.listdir('raw')
    for fn in files:
        new = pd.read_csv(f"raw/{fn}", header=None).T
        new.to_csv(f"transposed/{fn}", header=False, index=False)


def csv_to_airtab(files):
    airtab_dp = Airtable(os.environ['other_scrapers_db'], 'mdoc daily pop data', os.environ['AIRTABLE_API_KEY'])
    for fn in files:
        with open(fn, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                airtab_dp.insert(row, typecast=True)


def reorganize_files():
    os.chdir('/Users/blakefeldman/code/data/mdoc/monthly_fact_sheets/raw')
    files = os.listdir('.')
    for fn in files:
        if fn.endswith('page-1-table-2.csv'):
            shutil.move(fn, 'p1t2')
        elif fn.endswith('page-2-table-2.csv'):
            shutil.move(fn, 'p2t2')
        elif fn.endswith('page-3-table-2.csv'):
            shutil.move(fn, 'p3t2')
        elif fn.endswith('page-4-table-2.csv'):
            shutil.move(fn, 'p4t2')
        elif fn.endswith('page-5-table-2.csv'):
            shutil.move(fn, 'p5t2')
        elif fn.endswith('page-6-table-2.csv'):
            shutil.move(fn, 'p6t2')


def csv_writer():
    records = airtab.get_all(view='dev', fields=['dc_id', 'txt_2'])
    for rec in records:
        fn = rec['fields']['csv']
        content = rec['fields']['txt_2']
        with open(fn, 'w') as f:
            f.write(content)
        print(fn)


def get_txt():
    records = airtab.get_all(view='dev', fields='dc_id')
    for rec in records:
        obj = dc.documents.get(rec['fields']['dc_id'])
        this_dict = {}
        this_dict['dc_full_text'] = obj.full_text.decode("utf-8")
        airtab.update(rec['id'], this_dict)
        time.sleep(.7)


def some_shit():
    os.chdir('parole_statistics_by_race_and_sex')
    os.getcwd()
    records = airtab.get_all(view='dev', fields=['txt_8', 'csv'])
    len(records)
    for rec in records:
        fn = rec['fields']['csv']
        content = rec['fields']['txt_8']
        with open(fn, 'w') as f:
            f.write(content)
        print(fn)


def fix_fn():
    fns = os.listdir('.')
    for fn in fns:
        if len(fn) > 11:
            os.rename(fn, f"{fn[:7]}.csv")

    records = airtab.get_all(view='dev', fields=['url', 'csv', 'p'])
    for rec in records:
        tables = camelot.read_pdf(
            rec['fields']['url'], flavor='stream', pages='2', table_regions=['50,342,487,160'])
        tables = camelot.read_pdf(rec['fields']['url'], flavor='stream',
                                  pages=rec['fields']['p'], table_regions=['25,362,595,87'])
        tables.export(rec['fields']['csv'], f='csv')


muh_folders = ['specific_offense_stats',
               'probation_pop_by_race_and_sex',
               'probation_pop_by_offense',
               'parole_pop_by_race_and_sex',
               'parole_pop_by_offense',
               'inmate_pop_by_race_sex_and_location',
               'inmate_pop_by_race_and_sex',
               'inmate_pop_by_location',
               'corrections_pop_by_type',
               'community_corrections_pop_by_type',
               'inmate_pop_by_offense_and_location']


def csv_linter(folders):
    for folder in folders:
        # os.chdir(f"/Users/blakefeldman/code/data/other/{folder}")
        os.chdir(f"/Users/blakefeldman/code/data/mdoc/monthly_fact_sheets/{folder}")
        files = glob.glob('*.csv')
        files.sort()
        for fn in files:
            report = validate(fn)
            if report['valid']:
                pass
            else:
                print(
                    f"\t{report['error-count']} error(s) in {folder}/{report['tables'][0]['source']}")
        print(f"done with {folder}!!\n\n")


def get_coordinates(left, top, width, height):
    x1 = left
    y1 = 792 - top
    x2 = left + width
    y2 = y1 - height
    return f"{x1},{y1},{x2},{y2}"


def merge_dp():
    os.chdir('/Users/blakefeldman/code/data/mdoc/daily_pop/per_page')
    records = airtab.get_all(view='dp needs csv', fields=['iso', 'dc_pages'])
    for rec in records:
        a = pd.read_csv(f"{rec['fields']['iso']}-p1.csv")
        b = pd.read_csv(f"{rec['fields']['iso']}-p2.csv")
        m1 = pd.merge(a, b, on='Location')
        if rec['fields']['dc_pages'] == 2:
            merged = m1
        else:
            c = pd.read_csv(f"{rec['fields']['iso']}-p3.csv")
            if rec['fields']['dc_pages'] == 4:
                d = pd.read_csv(f"{rec['fields']['iso']}-p4.csv")
                m2 = pd.merge(c, d, on='Location')
                merged = pd.merge(m1, m2, on='Location')
            elif rec['fields']['dc_pages'] == 3:
                merged = pd.merge(m1, c, on='Location')
        merged.to_csv(f"{rec['fields']['iso']}.csv", index=False)


def get_mdoc_tables(year, latice_pages, stream_pages=None):
    os.chdir(f"/Users/blakefeldman/code/data/mdoc/annual_reports/{year}")
    tables = camelot.read_pdf(
        f"{year} MDOC Annual Report.pdf", pages=latice_pages)
    tables.export(f"{year}.csv", f='csv')
    if stream_pages:
        tables2 = camelot.read_pdf(
            f"{year} MDOC Annual Report.pdf", flavor='stream', pages=stream_pages)
        tables2.export(f"{year}.csv", f='csv')


def merge_specific_offense_stats(files):
    # os.chdir('/Users/blakefeldman/code/data/mdoc/monthly_fact_sheets/specific_offense_stats')
    # files = glob.glob('*.csv')
    # files.sort()
    these_rows = []
    for fn in files:
        this_dict = {'month': fn.replace('.csv', '')}
        csv_file = open(fn, 'r')
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            this_dict[row['type']] = row['count']
        these_rows.append(this_dict)
    with open('specific_offense_stats.csv', mode='a', newline='') as csv_file:
        fieldnames = ['month', 'armed_robbery_mandatory', 'lifers',
                        'habitual_offenders', 'habitual_lifers', 'death_row', 'total']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in these_rows:
            writer.writerow(row)


def merge_community_corrections_pop_by_type():
    os.chdir(
        '/Users/blakefeldman/code/data/mdoc/monthly_fact_sheets/community_corrections_pop_by_type')
    files = glob.glob('*.csv')
    files.sort()
    these_rows = []
    for fn in files:
        this_dict = {'month': fn.replace('.csv', '')}
        csv_file = open(fn, 'r')
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            this_dict[row['status']] = row['count']
        these_rows.append(this_dict)
    with open('community_corrections_pop_by_type.csv', mode='a', newline='') as csv_file:
        fieldnames = ['month', 'probation', 'compact_probation', 'nonadjudicated', 'post_release', 'TVC_probation', 'probation_total',
                      'parole', 'compact_parole', 'suspension', 'TVC_parole', 'parole_total',
                      'ISP_court', 'ISP_prison', 'ISP', 'earned_release_supervision', 'medical_release', 'FTR_monitoring',
                      'conditional_release', 'TVC', 'RRP', 'transitional_housing', 'community_inmate_total', 'total']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in these_rows:
            writer.writerow(row)

muh_files = ['2020-05.csv', '2020-06.csv', '2020-07.csv', '2020-08.csv']

def add_columns_for_specific_offenses(files):
    for fn in files:
        df = pd.read_csv(fn, index_col='type')
        df['total_count'] = df['count_without_sex_offense'] + df['count_with_sex_offense']
        df.to_csv(f'new_{fn}')


the_big_dict = {
    'corrections_pop_by_type_subtotoals': ['2019-11.csv', '2019-12.csv', '2020-01.csv', '2020-01.csv', '2020-02.csv', '2020-03.csv', '2020-04.csv', '2020-05.csv', '2020-06.csv', '2020-07.csv', '2020-08.csv'],
    'community_corrections_pop_by_type': ['2019-11.csv', '2019-12.csv', '2020-01.csv', '2020-01.csv', '2020-02.csv', '2020-03.csv', '2020-04.csv', '2020-05.csv', '2020-06.csv', '2020-07.csv', '2020-08.csv'],
    'corrections_pop_by_type': ['2019-08.csv', '2019-09.csv', '2019-10.csv', '2019-11.csv', '2019-12.csv', '2020-01.csv', '2020-01.csv', '2020-02.csv', '2020-03.csv', '2020-04.csv', '2020-05.csv', '2020-06.csv', '2020-07.csv', '2020-08.csv']
}

['Custody Population', 'Custody Population %', 'Community Corrections', 'Community Corrections %', 'Other Custody', 'Other Custody %', 'At Large', 'At Large %', 'Off-Grounds Medical', 'Off-Grounds Medical %', 'INMATE TOTAL', 'INMATE TOTAL %', 'Parolees', 'PAROLEES %', 'TVC Parole', 'TVC Parole %', 'Probationers', 'PROBATIONERS %', 'TVC Probation', 'TVC Probation %', 'PAROLEE AND PROBATIONER TOTAL', 'PAROLEE AND PROBATIONER TOTAL %', 'TOTAL INMATES, PAROLEES, & PROBATIONERS', 'TOTAL INMATES, PAROLEES, & PROBATIONERS %']
