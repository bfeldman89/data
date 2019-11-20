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
    records = airtab.get_all(view='mfs', fields=['url', 'iso', 'dc_pages'])
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
        try:
            new = pd.read_csv(f"raw/{fn}", header=None).T
            new.to_csv(f"transposed/{fn}", header=False, index=False)
        except:
            print(fn, 'fucked up')


def csv_to_airtab():
    files = os.listdir('.')
    for fn in files:
        if fn.endswith('.csv'):
            with open(fn, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    try:
                        airtab.insert(row, typecast=True)
                    except:
                        print(fn, 'fucked up')


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
        os.chdir(f"/Users/blakefeldman/code/data/mdoc/daily_pop/{folder}")
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
