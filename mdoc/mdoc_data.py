import os
import shutil
from airtable import Airtable
import camelot


def get_raw_dp_csvs():
    os.chdir('/Users/blakefeldman/code/data/mdoc/daily_pop/raw')
    airtab = Airtable(os.environ['other_scrapers_db'], 'mdoc', os.environ['AIRTABLE_API_KEY'])
    records = airtab.get_all(view='dp', fields=['url', 'iso', 'dc_pages'])
    for rec in records:
        fn = f"{rec['fields']['iso']}.csv"
        pages = f"1-{rec['fields']['dc_pages']}"
        url = rec['fields']['url']
        tables = camelot.read_pdf(url, pages=pages)
        tables.export(fn, f='csv')


def get_raw_mfs_csvs():
    os.chdir('/Users/blakefeldman/code/data/mdoc/monthly_fact_sheets/raw')
    airtab = Airtable(os.environ['other_scrapers_db'],
                      'mdoc', os.environ['AIRTABLE_API_KEY'])
    records = airtab.get_all(view='mfs', fields=['url', 'iso', 'dc_pages'])
    for rec in records:
        fn = f"{rec['fields']['iso']}.csv"
        pages = f"1-{rec['fields']['dc_pages']}"
        url = rec['fields']['url']
        tables = camelot.read_pdf(url, flavor='stream', pages=pages)
        tables.export(fn, f='csv')


def clean_raw_csvs():
    os.chdir('/Users/blakefeldman/code/data/mdoc/daily_pop/raw')
    files = os.listdir('.')
    for fn in files:
        try:
            pd.read_csv(fn, header=None).T.to_csv(
                f"transposed_{fn}", header=False, index=False)
        except:
            print(fn, 'fucked up')


"""
files = os.listdir('.')
for fn in files:
    if fn.startswith('transposed_'):
        print('first table')  # filler code to prevent error/warning
"""

"""
headers = []
files = os.listdir('.')
for fn in files:
    try:
        with open(fn, 'r') as f:
            d_reader = csv.DictReader(f)
            headers.extend(d_reader.fieldnames)
    except UnicodeDecodeError as err:
        print(fn, '------->', err)
    print(fn)

x = list(set(headers))
"""

"""
def csv_to_airtab():
    airtab = Airtable(os.environ['other_scrapers_db'], 'new', os.environ['AIRTABLE_API_KEY'])
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


for fn in files:
    with open(fn, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            airtab.insert(row, typecast=True)

airtab = Airtable(os.environ['other_scrapers_db'], 'new', os.environ['AIRTABLE_API_KEY'])
files = os.listdir('.')
for fn in files:
    if fn.endswith('.csv'):
        with open(fn) as f:
            first_line = f.readline()
        print(fn, '-----', first_line)
"""


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
