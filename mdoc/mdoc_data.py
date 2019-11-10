import os
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
    airtab = Airtable(os.environ['other_scrapers_db'], 'mdoc', os.environ['AIRTABLE_API_KEY'])
    records = airtab.get_all(view='mfs', fields=['url', 'iso', 'dc_pages'])
    for rec in records:
        fn = f"{rec['fields']['iso']}.csv"
        pages = f"1-{rec['fields']['dc_pages']}"
        url = rec['fields']['url']
        tables = camelot.read_pdf(url, flavor='stream', pages=pages)
        tables.export(fn, f='csv')


def clean_raw_csvs():
    os.chdir('/Users/blakefeldman/code/data/mdoc/monthly_fact_sheets/raw')
    for fn in os.listdir('.'):
        if fn.endswith('page-1-table-1.csv'):
            print('first table')  # filler code to prevent error/warning
