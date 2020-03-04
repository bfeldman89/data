# !/usr/local/bin/python3.6
import os
import csv
import glob
import shutil
import time
from airtable import Airtable
import camelot
import pandas as pd
from documentcloud import DocumentCloud
from goodtables import validate

airtab = Airtable(os.environ['other_scrapers_db'],
                  'mdoc', os.environ['AIRTABLE_API_KEY'])

dc = DocumentCloud(
    os.environ['DOCUMENT_CLOUD_USERNAME'], os.environ['DOCUMENT_CLOUD_PW'])


def get_raw_dp_csvs():
    os.chdir('/Users/blakefeldman/code/data/mdoc/daily_pop/raw')
    records = airtab.get_all(view='dp', fields=['url', 'iso', 'dc_pages'])
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
    files = os.listdir('per_page')
    for fn in files:
        new = pd.read_csv(f"raw/{fn}", header=None).T
        new.to_csv(f"transposed/{fn}", header=False, index=False)


def csv_to_airtab():
    files = os.listdir('.')
    for fn in files:
        if fn.endswith('.csv'):
            with open(fn, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    airtab.insert(row, typecast=True)


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
        os.chdir(f"/Users/blakefeldman/code/data/other/{folder}")
        # os.chdir(f"/Users/blakefeldman/code/data/mdoc/monthly_fact_sheets/{folder}")
        files = glob.glob('*.csv')
        files.sort()
        for fn in files:
            report = validate(fn)
            if report['valid']:
                pass
            else:
                print(
                    f"\t{report['error-count']} error(s) in {folder}/{report['tables'][0]['source']}")
        print(f"done with {folder}!!")


def get_coordinates(left, top, width, height):
    x1 = left
    y1 = 792 - top
    x2 = left + width
    y2 = y1 - height
    return f"{x1},{y1},{x2},{y2}"


def merge_dp():
    os.chdir('/Users/blakefeldman/code/data/mdoc/daily_pop/raw')
    records = airtab.get_all(view='dev', fields=['iso', 'dc_pages'])
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


def merge_specific_offense_stats():
    os.chdir(
        '/Users/blakefeldman/code/data/mdoc/monthly_fact_sheets/specific_offense_stats')
    files = glob.glob('*.csv')
    files.sort()
    these_rows = []
    for fn in files:
        this_dict = {'month': fn.replace('.csv', '')}
        csv_file = open(fn, 'r')
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            this_dict[row['type']] = row['count']
        these_rows.append(this_dict)
    with open('specific_offense_stats.csv', mode='w', newline='') as csv_file:
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
    with open('community_corrections_pop_by_type.csv', mode='w', newline='') as csv_file:
        fieldnames = ['month', 'probation', 'compact_probation', 'nonadjudicated', 'post_release', 'TVC_probation', 'probation_total',
                      'parole', 'compact_parole', 'suspension', 'TVC_parole', 'parole_total',
                      'ISP_court', 'ISP_prison', 'ISP', 'earned_release_supervision', 'medical_release', 'FTR_monitoring',
                      'conditional_release', 'TVC', 'RRP', 'transitional_housing', 'community_inmate_total', 'total']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in these_rows:
            writer.writerow(row)


def add_columns_for_specific_offenses(files):
    for fn in files:
        df = pd.read_csv(fn, index_col='type')
        df['count'] = df['count_without_sex_offense'] + \
            df['count_with_sex_offense']
        df.to_csv(f'new_{fn}')


get_mdoc_tables('2004',
                '15-25,27-49,90-97,100-101')
get_mdoc_tables('2005',
                '21-25,29-46,49,50,64,65,67,70-93,96-98,100-112,114-118,120-124,126-132,134-142,146-150,152-164,166-170,172-176,178-184,186-196',
                '17-20')
get_mdoc_tables('2006',
                '23-26,31-48,51,52,65-67,69-74,78-101,104-106,108-120,122-126,128-132,134-140,142-152,156-160,162-174,176-180,182-186,188-194,196-206')
get_mdoc_tables('2007',
                '24-27,32-48,50,63,64,66-73,76,77,80-87,90,91,94,95,99,102,105-107,110,112,113,116,118,119,122,124,125,128-131',
                '20-23,78,79,92,93,100,101,108,109,114,115,120,121,126,127')
get_mdoc_tables('2008',
                '23-26,31-46,48,61,62,64-71,74,75,78-85,88,89,92,93,97,100,103-105,108,110,111,114,116,117,120,122,123,126,129',
                '20-22,90,91,98,99,106,107,112,113,118,119,124,125')
get_mdoc_tables('2009',
                '21-27,31-47,49,62,63,65-72,75,76,79-86,89,90,93,94,98,101,104-106,109,111,112,115,117,118,121,123,124,127-130,134,135,137,140-142,145,148,151,153,154,157',
                '77,78,91,92,99,100,107,108,113,114,119,120,125,126,135,136,143,144,149,150,155,156')
get_mdoc_tables('2010',
                '32-48,50,63,64,66-73,76-77,80-87,90-91,94-95,99,102,105-107,110,112,113,116,118,119,122,124,125,128-131',
                '78,79,92,93,100,101,108,109,114,115,120,121,126,127')
get_mdoc_tables('2011',
                '32-48,50,63,64,66-73,76-77,80-87,90-91,94-95,99,102,105-107,110,112,113,116,118,119,122,124,125,128-131',
                '78,79,92,93,100,101,108,109,114,115,120,121,126,127')
get_mdoc_tables('2012',
                '32-48,50,63,64,66-73,76-77,80-87,90-91,94-95,99,102,105-107,110,112,113,116,118,119,122,124,125,128-131',
                '78,79,92,93,100,101,108,109,114,115,120,121,126,127')
get_mdoc_tables('2013',
                '14-16,18-20,22-24,32-39,45,46,53-59,68-78,80,81,84-109,112-139')
get_mdoc_tables('2014',
                '12-16,18,20,21,28-35,43,44,46,48-53,62-72,74,75,78-103,106-110,112-133')
get_mdoc_tables('2015',
                '14-21,27-32,40,41,43,45-52,61-71,73,76-101,104-108,110-131')
get_mdoc_tables('2016', '3-22,24-30,32-50')
get_mdoc_tables('2017', '3-22,24-30,32-50')
get_mdoc_tables('2018', '3-22,24-30,32-50')
