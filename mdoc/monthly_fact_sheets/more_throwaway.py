import os
import time
from airtable import Airtable
from documentcloud import DocumentCloud

airtab = Airtable(os.environ['other_scrapers_db'],
                  'mdoc', os.environ['AIRTABLE_API_KEY'])

dc = DocumentCloud(
    os.environ['DOCUMENT_CLOUD_USERNAME'], os.environ['DOCUMENT_CLOUD_PW'])

records = airtab.get_all(view='dev', fields=['txt_2', 'csv'])

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

os.chdir('parole_statistics_by_race_and_sex')
os.getcwd()
records = airtab.get_all(view='dev', fields=['txt_7', 'csv'])
len(records)
for rec in records:
    fn = rec['fields']['csv']
    content = rec['fields']['txt_7']
    with open(fn, 'w') as f:
        f.write(content)
    print(fn)
