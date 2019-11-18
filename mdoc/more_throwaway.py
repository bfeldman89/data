import os
import time
from airtable import Airtable
import camelot
from documentcloud import DocumentCloud
from goodtables import validate

airtab = Airtable(os.environ['other_scrapers_db'],
                  'mdoc', os.environ['AIRTABLE_API_KEY'])

dc = DocumentCloud(
    os.environ['DOCUMENT_CLOUD_USERNAME'], os.environ['DOCUMENT_CLOUD_PW'])

records = airtab.get_all(view='dev', fields=['url', 'csv'])


def csv_writer():
    for rec in records:
        fn = rec['fields']['csv']
        content = rec['fields']['txt_2']
        with open(fn, 'w') as f:
            f.write(content)
        print(fn)


records = airtab.get_all(view='dev', fields='dc_id')
for rec in records:
    obj = dc.documents.get(rec['fields']['dc_id'])
    this_dict = {}
    this_dict['dc_full_text'] = obj.full_text.decode("utf-8")
    airtab.update(rec['id'], this_dict)
    time.sleep(.7)

os.chdir('../parole_statistics_by_race_and_sex')


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

    records = airtab.get_all(view='dev', fields=['url', 'csv'])
    for rec in records:
        tables = camelot.read_pdf(
            rec['fields']['url'], flavor='stream', pages='2', table_regions=['50,342,487,160'])
        tables[0].to_csv(rec['fields']['csv'])


"""
import os
import time
from airtable import Airtable
import camelot
from documentcloud import DocumentCloud

airtab = Airtable(os.environ['other_scrapers_db'],
                  'mdoc', os.environ['AIRTABLE_API_KEY'])

records = airtab.get_all(view='dev', fields=['url', 'csv', 'p'])
len(records)
os.getcwd()
os.chdir('/Users/blakefeldman/code/data/mdoc')

for rec in records:
    tables = camelot.read_pdf(rec['fields']['url'], flavor='stream', pages=rec['fields']['p'], table_regions=['33,324,579,42'])
    tables.export(rec['fields']['csv'], f='csv')

"""

# or via command line
# camelot -p 3 stream -R 33,324,579,42 https://www.mdoc.ms.gov/Admin-Finance/MonthlyFacts/12-01-2016%20Fact%20Sheet.pdf
# tables[1].to_csv('2016-12.csv')

muh_folders = ['specific_offense_stats',
               'probation_stats_by_race_and_sex',
               'probation_stats_by_offense',
               'parole_stats_by_race_and_sex',
               'parole_stats_by_offense',
               'inmate_stats_by_race_sex_and_location',
               'inmate_stats_by_race_and_sex',
               'inmate_stats_by_location',
               'active_offender_pop_by_type',
               'active_community_corrections_pop_by_type',
               'inmate_stats_by_offense_and_location']


def csv_linter(folders):
    path = '/Users/blakefeldman/code/data/mdoc/monthly_fact_sheets'
    for folder in folders:
        os.chdir(f"{path}/{folder}")
        files = os.listdir('.')
        for fn in files:
            if fn.endswith('.csv'):
                report = validate(fn)
                if report['valid']:
                    print(fn)
                else:
                    print(
                        f"{report['error-count']} error(s) in {report['tables'][0]['source']} ")

# csv_linter('inmate_statistics_by_location')
# csv_linter('parole_statistics_by_offense')
# csv_linter('probation_statistics_by_offense')
# csv_linter('inmate_statistics_by_race_sex_and_location')
# csv_linter('active_community_corrections_caseloads_by_type')
# csv_linter('inmate_statistics_by_race_and_sex')
# csv_linter('active_offender_population_by_type')
# csv_linter('probation_statistics_by_race_and_sex')
# csv_linter('parole_statistics_by_race_and_sex')
# csv_linter('specific_offense_statistic')
