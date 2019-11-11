import os
from airtable import Airtable

airtab = Airtable(os.environ['other_scrapers_db'], 'new', os.environ['AIRTABLE_API_KEY'])

# for day in ["19-Mar-10", "20-Mar-10", "21-Mar-10", "22-Mar-10", "23-Mar-10", "24-Mar-10", "25-Mar-10", "26-Mar-10", "27-Mar-10"]:
#     rec = airtab.match('raw_date', day)
#     if rec:
#        airtab.update(rec['id'], {'citation': '2010-03-page-3-table-1.csv'})

for day in ["28-Nov-12", "29-Nov-12", "30-Nov-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-11-page-4-table-1.csv'})

for day in ["14-Mar-05", "15-Mar-05", "16-Mar-05", "17-Mar-05", "18-Mar-05", "19-Mar-05", "20-Mar-05", "21-Mar-05", "22-Mar-05", "23-Mar-05", "24-Mar-05", "25-Mar-05", "26-Mar-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-03-page-2-table-1.csv'})

for day in ["10-Feb-14", "11-Feb-14", "12-Feb-14", "13-Feb-14", "14-Feb-14", "15-Feb-14", "16-Feb-14", "17-Feb-14", "18-Feb-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-02-page-2-table-1.csv'})

for day in ["1-Mar-15", "2-Mar-15", "3-Mar-15", "4-Mar-15", "5-Mar-15", "6-Mar-15", "7-Mar-15", "8-Mar-15", "9-Mar-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-03-page-1-table-1.csv'})

for day in ["1-Feb-04", "2-Feb-04", "3-Feb-04", "4-Feb-04", "5-Feb-04", "6-Feb-04", "7-Feb-04", "8-Feb-04", "9-Feb-04", "10-Feb-04", "11-Feb-04", "12-Feb-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-02-page-1-table-1.csv'})

for day in ["1-Jan-18", "2-Jan-18", "3-Jan-18", "4-Jan-18", "5-Jan-18", "6-Jan-18", "7-Jan-18", "8-Jan-18", "9-Jan-18", "10-Jan-18", "11-Jan-18", "12-Jan-18", "13-Jan-18", "14-Jan-18", "15-Jan-18", "16-Jan-18", "17-Jan-18"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2018-01-page-1-table-1.csv'})

for day in ["10-Jan-08", "11-Jan-08", "12-Jan-08", "13-Jan-08", "14-Jan-08", "15-Jan-08", "16-Jan-08", "17-Jan-08", "18-Jan-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-01-page-2-table-1.csv'})

for day in ["28-Jun-13", "29-Jun-13", "30-Jun-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-06-page-4-table-1.csv'})

for day in ["28-Sep-08", "29-Sep-08", "30-Sep-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-09-page-4-table-1.csv'})

for day in ["1-Feb-12", "2-Feb-12", "3-Feb-12", "4-Feb-12", "5-Feb-12", "6-Feb-12", "7-Feb-12", "8-Feb-12", "9-Feb-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-02-page-1-table-1.csv'})

for day in ["1-Mar-03", "2-Mar-03", "3-Mar-03", "4-Mar-03", "5-Mar-03", "6-Mar-03", "7-Mar-03", "8-Mar-03", "9-Mar-03", "10-Mar-03", "11-Mar-03", "12-Mar-03", "13-Mar-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-03-page-1-table-1.csv'})

for day in ["13-Feb-02", "14-Feb-02", "15-Feb-02", "16-Feb-02", "17-Feb-02", "18-Feb-02", "19-Feb-02", "20-Feb-02", "21-Feb-02", "22-Feb-02", "23-Feb-02", "24-Feb-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-02-page-2-table-1.csv'})

for day in ["10-Mar-13", "11-Mar-13", "12-Mar-13", "13-Mar-13", "14-Mar-13", "15-Mar-13", "16-Mar-13", "17-Mar-13", "18-Mar-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-03-page-2-table-1.csv'})

for day in ["28-Oct-15", "29-Oct-15", "30-Oct-15", "31-Oct-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-10-page-4-table-1.csv'})

for day in ["28-Apr-08", "29-Apr-08", "30-Apr-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-04-page-4-table-1.csv'})

for day in ["19-Mar-06", "20-Mar-06", "21-Mar-06", "22-Mar-06", "23-Mar-06", "24-Mar-06", "25-Mar-06", "26-Mar-06", "27-Mar-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-03-page-3-table-1.csv'})

for day in ["22-Feb-17", "23-Feb-17", "24-Feb-17", "25-Feb-17", "26-Feb-17", "27-Feb-17", "28-Feb-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-02-page-3-table-1.csv'})

for day in ["19-Apr-11", "20-Apr-11", "21-Apr-11", "22-Apr-11", "23-Apr-11", "24-Apr-11", "25-Apr-11", "26-Apr-11", "27-Apr-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-04-page-3-table-1.csv'})

for day in ["1-Oct-09", "2-Oct-09", "3-Oct-09", "4-Oct-09", "5-Oct-09", "6-Oct-09", "7-Oct-09", "8-Oct-09", "9-Oct-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-10-page-1-table-1.csv'})

for day in ["1-May-05", "2-May-05", "3-May-05", "4-May-05", "5-May-05", "6-May-05", "7-May-05", "8-May-05", "9-May-05", "10-May-05", "11-May-05", "12-May-05", "13-May-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-05-page-1-table-1.csv'})

for day in ["1-Nov-18", "2-Nov-18", "3-Nov-18", "4-Nov-18", "5-Nov-18", "6-Nov-18", "7-Nov-18", "8-Nov-18", "9-Nov-18", "10-Nov-18", "11-Nov-18", "12-Nov-18", "13-Nov-18", "14-Nov-18", "15-Nov-18", "16-Nov-18", "17-Nov-18", "18-Nov-18", "19-Nov-18"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2018-11-page-1-table-1.csv'})

for day in ["1-Apr-14", "2-Apr-14", "3-Apr-14", "4-Apr-14", "5-Apr-14", "6-Apr-14", "7-Apr-14", "8-Apr-14", "9-Apr-14", "10-Apr-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-04-page-1-table-1.csv'})

for day in ["18-Oct-19", "19-Oct-19", "20-Oct-19", "21-Oct-19", "22-Oct-19", "23-Oct-19", "24-Oct-19", "25-Oct-19", "26-Oct-19", "27-Oct-19", "28-Oct-19", "29-Oct-19", "30-Oct-19", "31-Oct-19"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2019-10-page-2-table-1.csv'})

for day in ["10-May-15", "11-May-15", "12-May-15", "13-May-15", "14-May-15", "15-May-15", "16-May-15", "17-May-15", "18-May-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-05-page-2-table-1.csv'})

for day in ["10-Nov-08", "11-Nov-08", "12-Nov-08", "13-Nov-08", "14-Nov-08", "15-Nov-08", "16-Nov-08", "17-Nov-08", "18-Nov-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-11-page-2-table-1.csv'})

for day in ["14-Apr-04", "15-Apr-04", "16-Apr-04", "17-Apr-04", "18-Apr-04", "19-Apr-04", "20-Apr-04", "21-Apr-04", "22-Apr-04", "23-Apr-04", "24-Apr-04", "25-Apr-04", "26-Apr-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-04-page-2-table-1.csv'})

for day in ["19-Sep-11", "20-Sep-11", "21-Sep-11", "22-Sep-11", "23-Sep-11", "24-Sep-11", "25-Sep-11", "26-Sep-11", "27-Sep-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-09-page-3-table-1.csv'})

for day in ["18-Jul-18", "19-Jul-18", "20-Jul-18", "21-Jul-18", "22-Jul-18", "23-Jul-18", "24-Jul-18", "25-Jul-18", "26-Jul-18", "27-Jul-18", "28-Jul-18", "29-Jul-18", "30-Jul-18", "31-Jul-18"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2018-07-page-2-table-1.csv'})

for day in ["10-Dec-14", "11-Dec-14", "12-Dec-14", "13-Dec-14", "14-Dec-14", "15-Dec-14", "16-Dec-14", "17-Dec-14", "18-Dec-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-12-page-2-table-1.csv'})

for day in ["10-Jun-09", "11-Jun-09", "12-Jun-09", "13-Jun-09", "14-Jun-09", "15-Jun-09", "16-Jun-09", "17-Jun-09", "18-Jun-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-06-page-2-table-1.csv'})

for day in ["1-Jul-08", "2-Jul-08", "3-Jul-08", "4-Jul-08", "5-Jul-08", "6-Jul-08", "7-Jul-08", "8-Jul-08", "9-Jul-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-07-page-1-table-1.csv'})

for day in ["1-Dec-04", "2-Dec-04", "3-Dec-04", "4-Dec-04", "5-Dec-04", "6-Dec-04", "7-Dec-04", "8-Dec-04", "9-Dec-04", "10-Dec-04", "11-Dec-04", "12-Dec-04", "13-Dec-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-12-page-1-table-1.csv'})

for day in ["1-Jun-19", "2-Jun-19", "3-Jun-19", "4-Jun-19", "5-Jun-19", "6-Jun-19", "7-Jun-19", "8-Jun-19", "9-Jun-19", "10-Jun-19", "11-Jun-19", "12-Jun-19", "13-Jun-19", "14-Jun-19", "15-Jun-19", "16-Jun-19", "17-Jun-19", "18-Jun-19", "19-Jun-19", "20-Jun-19"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2019-06-page-1-table-1.csv'})

for day in ["10-Aug-15", "11-Aug-15", "12-Aug-15", "13-Aug-15", "14-Aug-15", "15-Aug-15", "16-Aug-15", "17-Aug-15", "18-Aug-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-08-page-2-table-1.csv'})

for day in ["21-Dec-01", "22-Dec-01", "23-Dec-01", "24-Dec-01", "25-Dec-01", "26-Dec-01", "27-Dec-01", "28-Dec-01", "29-Dec-01", "30-Dec-01", "31-Dec-01"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2001-12-page-3-table-1.csv'})

for day in ["14-Sep-04", "15-Sep-04", "16-Sep-04", "17-Sep-04", "18-Sep-04", "19-Sep-04", "20-Sep-04", "21-Sep-04", "22-Sep-04", "23-Sep-04", "24-Sep-04", "25-Sep-04", "26-Sep-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-09-page-2-table-1.csv'})

for day in ["1-Aug-05", "2-Aug-05", "3-Aug-05", "4-Aug-05", "5-Aug-05", "6-Aug-05", "7-Aug-05", "8-Aug-05", "9-Aug-05", "10-Aug-05", "11-Aug-05", "12-Aug-05", "13-Aug-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-08-page-1-table-1.csv'})

for day in ["1-Sep-14", "2-Sep-14", "3-Sep-14", "4-Sep-14", "5-Sep-14", "6-Sep-14", "7-Sep-14", "8-Sep-14", "9-Sep-14", "10-Sep-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-09-page-1-table-1.csv'})

for day in ["28-Jan-12", "29-Jan-12", "30-Jan-12", "31-Jan-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-01-page-4-table-1.csv'})

for day in ["1-Sep-02", "2-Sep-02", "3-Sep-02", "4-Sep-02", "5-Sep-02", "6-Sep-02", "7-Sep-02", "8-Sep-02", "9-Sep-02", "10-Sep-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-09-page-1-table-1.csv'})

for day in ["1-Aug-13", "2-Aug-13", "3-Aug-13", "4-Aug-13", "5-Aug-13", "6-Aug-13", "7-Aug-13", "8-Aug-13", "9-Aug-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-08-page-1-table-1.csv'})

for day in ["10-Sep-12", "11-Sep-12", "12-Sep-12", "13-Sep-12", "14-Sep-12", "15-Sep-12", "16-Sep-12", "17-Sep-12", "18-Sep-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-09-page-2-table-1.csv'})

for day in ["13-Aug-03", "14-Aug-03", "15-Aug-03", "16-Aug-03", "17-Aug-03", "18-Aug-03", "19-Aug-03", "20-Aug-03", "21-Aug-03", "22-Aug-03", "23-Aug-03", "24-Aug-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-08-page-2-table-1.csv'})

for day in ["1-Dec-12", "2-Dec-12", "3-Dec-12", "4-Dec-12", "5-Dec-12", "6-Dec-12", "7-Dec-12", "8-Dec-12", "9-Dec-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-12-page-1-table-1.csv'})

for day in ["20-Aug-16", "21-Aug-16", "22-Aug-16", "23-Aug-16", "24-Aug-16", "25-Aug-16", "26-Aug-16", "27-Aug-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-08-page-3-table-1.csv'})

for day in ["19-Sep-07", "20-Sep-07", "21-Sep-07", "22-Sep-07", "23-Sep-07", "24-Sep-07", "25-Sep-07", "26-Sep-07", "27-Sep-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-09-page-3-table-1.csv'})

for day in ["10-Apr-12", "11-Apr-12", "12-Apr-12", "13-Apr-12", "14-Apr-12", "15-Apr-12", "16-Apr-12", "17-Apr-12", "18-Apr-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-04-page-2-table-1.csv'})

for day in ["14-May-03", "15-May-03", "16-May-03", "17-May-03", "18-May-03", "19-May-03", "20-May-03", "21-May-03", "22-May-03", "23-May-03", "24-May-03", "25-May-03", "26-May-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-05-page-2-table-1.csv'})

for day in ["1-Apr-02", "2-Apr-02", "3-Apr-02", "4-Apr-02", "5-Apr-02", "6-Apr-02", "7-Apr-02", "8-Apr-02", "9-Apr-02", "10-Apr-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-04-page-1-table-1.csv'})

for day in ["1-May-13", "2-May-13", "3-May-13", "4-May-13", "5-May-13", "6-May-13", "7-May-13", "8-May-13", "9-May-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-05-page-1-table-1.csv'})

for day in ["19-May-16", "20-May-16", "21-May-16", "22-May-16", "23-May-16", "24-May-16", "25-May-16", "26-May-16", "27-May-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-05-page-3-table-1.csv'})

for day in ["19-Apr-07", "20-Apr-07", "21-Apr-07", "22-Apr-07", "23-Apr-07", "24-Apr-07", "25-Apr-07", "26-Apr-07", "27-Apr-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-04-page-3-table-1.csv'})

for day in ["28-Mar-09", "29-Mar-09", "30-Mar-09", "31-Mar-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-03-page-4-table-1.csv'})

for day in ["28-May-11", "29-May-11", "30-May-11", "31-May-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-05-page-4-table-1.csv'})

for day in ["10-Jan-16", "11-Jan-16", "12-Jan-16", "13-Jan-16", "14-Jan-16", "15-Jan-16", "16-Jan-16", "17-Jan-16", "18-Jan-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-01-page-2-table-1.csv'})

for day in ["1-Jan-06", "2-Jan-06", "3-Jan-06", "4-Jan-06", "5-Jan-06", "6-Jan-06", "7-Jan-06", "8-Jan-06", "9-Jan-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-01-page-1-table-1.csv'})

for day in ["28-Aug-11", "29-Aug-11", "30-Aug-11", "31-Aug-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-08-page-4-table-1.csv'})

for day in ["27-Jan-03", "28-Jan-03", "29-Jan-03", "30-Jan-03", "31-Jan-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-01-page-3-table-1.csv'})

for day in ["28-Dec-10", "29-Dec-10", "30-Dec-10", "31-Dec-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-12-page-4-table-1.csv'})

for day in ["28-Dec-06", "29-Dec-06", "30-Dec-06", "31-Dec-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-12-page-4-table-1.csv'})

for day in ["19-Jan-15", "20-Jan-15", "21-Jan-15", "22-Jan-15", "23-Jan-15", "24-Jan-15", "25-Jan-15", "26-Jan-15", "27-Jan-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-01-page-3-table-1.csv'})

for day in ["28-Aug-07", "29-Aug-07", "30-Aug-07", "31-Aug-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-08-page-4-table-1.csv'})

for day in ["28-Sep-16", "29-Sep-16", "30-Sep-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-09-page-4-table-1.csv'})

for day in ['1-Jan-10', '2-Jan-10', '3-Jan-10', '4-Jan-10', '5-Jan-10', '6-Jan-10', '7-Jan-10', '8-Jan-10', '9-Jan-10']:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-01-page-1-table-1.csv'})

for day in ["19-Feb-09", "20-Feb-09", "21-Feb-09", "22-Feb-09", "23-Feb-09", "24-Feb-09", "25-Feb-09", "26-Feb-09", "27-Feb-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-02-page-3-table-1.csv'})

for day in ["28-May-07", "29-May-07", "30-May-07", "31-May-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-05-page-4-table-1.csv'})

for day in ["28-Apr-16", "29-Apr-16", "30-Apr-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-04-page-4-table-1.csv'})

for day in ["27-Nov-03", "28-Nov-03", "29-Nov-03", "30-Nov-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-11-page-3-table-1.csv'})

for day in ["19-Oct-12", "20-Oct-12", "21-Oct-12", "22-Oct-12", "23-Oct-12", "24-Oct-12", "25-Oct-12", "26-Oct-12", "27-Oct-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-10-page-3-table-1.csv'})

for day in ["28-Feb-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-02-page-4-table-1.csv'})

for day in ["10-Oct-07", "11-Oct-07", "12-Oct-07", "13-Oct-07", "14-Oct-07", "15-Oct-07", "16-Oct-07", "17-Oct-07", "18-Oct-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-10-page-2-table-1.csv'})

for day in ["11-Nov-16", "12-Nov-16", "13-Nov-16", "14-Nov-16", "15-Nov-16", "16-Nov-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-11-page-2-table-1.csv'})

for day in ["1-Oct-17", "2-Oct-17", "3-Oct-17", "4-Oct-17", "5-Oct-17", "6-Oct-17", "7-Oct-17", "8-Oct-17", "9-Oct-17", "10-Oct-17", "11-Oct-17", "12-Oct-17", "13-Oct-17", "14-Oct-17", "15-Oct-17", "16-Oct-17", "17-Oct-17", "18-Oct-17", "19-Oct-17", "20-Oct-17", "21-Oct-17", "22-Oct-17", "23-Oct-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-10-page-1-table-1.csv'})

for day in ["1-Nov-06", "2-Nov-06", "3-Nov-06", "4-Nov-06", "5-Nov-06", "6-Nov-06", "7-Nov-06", "8-Nov-06", "9-Nov-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-11-page-1-table-1.csv'})

for day in ["1-Jul-16", "2-Jul-16", "3-Jul-16", "4-Jul-16", "5-Jul-16", "6-Jul-16", "7-Jul-16", "8-Jul-16", "9-Jul-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-07-page-1-table-1.csv'})

for day in ["1-Jun-07", "2-Jun-07", "3-Jun-07", "4-Jun-07", "5-Jun-07", "6-Jun-07", "7-Jun-07", "8-Jun-07", "9-Jun-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-06-page-1-table-1.csv'})

for day in ["10-Jul-06", "11-Jul-06", "12-Jul-06", "13-Jul-06", "14-Jul-06", "15-Jul-06", "16-Jul-06", "17-Jul-06", "18-Jul-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-07-page-2-table-1.csv'})

for day in ["11-Jun-17", "12-Jun-17", "13-Jun-17", "14-Jun-17", "15-Jun-17", "16-Jun-17", "17-Jun-17", "18-Jun-17", "19-Jun-17", "20-Jun-17", "21-Jun-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-06-page-2-table-1.csv'})

for day in ["21-Jun-02", "22-Jun-02", "23-Jun-02", "24-Jun-02", "25-Jun-02", "26-Jun-02", "27-Jun-02", "28-Jun-02", "29-Jun-02", "30-Jun-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-06-page-3-table-1.csv'})

for day in ["19-Jul-13", "20-Jul-13", "21-Jul-13", "22-Jul-13", "23-Jul-13", "24-Jul-13", "25-Jul-13", "26-Jul-13", "27-Jul-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-07-page-3-table-1.csv'})

for day in ["19-Dec-09", "20-Dec-09", "21-Dec-09", "22-Dec-09", "23-Dec-09", "24-Dec-09", "25-Dec-09", "26-Dec-09", "27-Dec-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-12-page-3-table-1.csv'})

for day in ["27-Jul-05", "28-Jul-05", "29-Jul-05", "30-Jul-05", "31-Jul-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-07-page-3-table-1.csv'})

for day in ["22-Jun-14", "23-Jun-14", "24-Jun-14", "25-Jun-14", "26-Jun-14", "27-Jun-14", "28-Jun-14", "29-Jun-14", "30-Jun-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-06-page-3-table-1.csv'})

for day in ["19-Aug-08", "20-Aug-08", "21-Aug-08", "22-Aug-08", "23-Aug-08", "24-Aug-08", "25-Aug-08", "26-Aug-08", "27-Aug-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-08-page-3-table-1.csv'})

for day in ["11-Jun-01", "12-Jun-01", "13-Jun-01", "14-Jun-01", "15-Jun-01", "16-Jun-01", "17-Jun-01", "18-Jun-01", "19-Jun-01", "20-Jun-01"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2001-06-page-2-table-1.csv'})

for day in ["10-Jul-10", "11-Jul-10", "12-Jul-10", "13-Jul-10", "14-Jul-10", "15-Jul-10", "16-Jul-10", "17-Jul-10", "18-Jul-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-07-page-2-table-1.csv'})

for day in ["1-Jun-11", "2-Jun-11", "3-Jun-11", "4-Jun-11", "5-Jun-11", "6-Jun-11", "7-Jun-11", "8-Jun-11", "9-Jun-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-06-page-1-table-1.csv'})

for day in ["1-Nov-10", "2-Nov-10", "3-Nov-10", "4-Nov-10", "5-Nov-10", "6-Nov-10", "7-Nov-10", "8-Nov-10", "9-Nov-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-11-page-1-table-1.csv'})

for day in ["1-Oct-01", "2-Oct-01", "3-Oct-01", "4-Oct-01", "5-Oct-01", "6-Oct-01", "7-Oct-01", "8-Oct-01", "9-Oct-01", "10-Oct-01"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2001-10-page-1-table-1.csv'})

for day in ["10-Oct-11", "11-Oct-11", "12-Oct-11", "13-Oct-11", "14-Oct-11", "15-Oct-11", "16-Oct-11", "17-Oct-11", "18-Oct-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-10-page-2-table-1.csv'})

for day in ["28-Feb-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-02-page-4-table-1.csv'})

for day in ["19-May-08", "20-May-08", "21-May-08", "22-May-08", "23-May-08", "24-May-08", "25-May-08", "26-May-08", "27-May-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-05-page-3-table-1.csv'})

for day in ["19-Nov-15", "20-Nov-15", "21-Nov-15", "22-Nov-15", "23-Nov-15", "24-Nov-15", "25-Nov-15", "26-Nov-15", "27-Nov-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-11-page-3-table-1.csv'})

for day in ["11-May-17", "Capacity", "11-May-17", "12-May-17", "13-May-17", "14-May-17", "15-May-17", "16-May-17", "17-May-17", "18-May-17", "19-May-17", "20-May-17", "21-May-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-05-page-2-table-1.csv'})

for day in ["10-Apr-06", "11-Apr-06", "12-Apr-06", "13-Apr-06", "14-Apr-06", "15-Apr-06", "16-Apr-06", "17-Apr-06", "18-Apr-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-04-page-2-table-1.csv'})

for day in ["1-May-07", "2-May-07", "3-May-07", "4-May-07", "5-May-07", "6-May-07", "7-May-07", "8-May-07", "9-May-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-05-page-1-table-1.csv'})

for day in ["1-Apr-16", "2-Apr-16", "3-Apr-16", "4-Apr-16", "5-Apr-16", "6-Apr-16", "7-Apr-16", "8-Apr-16", "9-Apr-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-04-page-1-table-1.csv'})

for day in ["19-Apr-13", "20-Apr-13", "21-Apr-13", "22-Apr-13", "23-Apr-13", "24-Apr-13", "25-Apr-13", "26-Apr-13", "27-Apr-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-04-page-3-table-1.csv'})

for day in ["21-May-02", "22-May-02", "23-May-02", "24-May-02", "25-May-02", "26-May-02", "27-May-02", "28-May-02", "29-May-02", "30-May-02", "31-May-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-05-page-3-table-1.csv'})

for day in ["1-Aug-07", "2-Aug-07", "3-Aug-07", "4-Aug-07", "5-Aug-07", "6-Aug-07", "7-Aug-07", "8-Aug-07", "9-Aug-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-08-page-1-table-1.csv'})

for day in ["1-Sep-16", "2-Sep-16", "3-Sep-16", "4-Sep-16", "5-Sep-16", "6-Sep-16", "7-Sep-16", "8-Sep-16", "9-Sep-16", "10-Sep-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-09-page-1-table-1.csv'})

for day in ['28-Jan-10', '29-Jan-10', '30-Jan-10', '31-Jan-10']:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-01-page-4-table-1.csv'})

for day in ["18-Aug-17", "19-Aug-17", "20-Aug-17", "21-Aug-17", "22-Aug-17", "23-Aug-17", "24-Aug-17", "25-Aug-17", "26-Aug-17", "27-Aug-17", "28-Aug-17", "29-Aug-17", "30-Aug-17", "31-Aug-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-08-page-2-table-1.csv'})

for day in ["10-Sep-06", "11-Sep-06", "12-Sep-06", "13-Sep-06", "14-Sep-06", "15-Sep-06", "16-Sep-06", "17-Sep-06", "18-Sep-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-09-page-2-table-1.csv'})

for day in ["27-Dec-03", "28-Dec-03", "29-Dec-03", "30-Dec-03", "31-Dec-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-12-page-3-table-1.csv'})

for day in ["1-Dec-06", "2-Dec-06", "3-Dec-06", "4-Dec-06", "5-Dec-06", "6-Dec-06", "7-Dec-06", "8-Dec-06", "9-Dec-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-12-page-1-table-1.csv'})

for day in ["11-Dec-16", "12-Dec-16", "13-Dec-16", "14-Dec-16", "15-Dec-16", "16-Dec-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-12-page-2-table-1.csv'})

for day in ["19-Sep-13", "20-Sep-13", "21-Sep-13", "22-Sep-13", "23-Sep-13", "24-Sep-13", "25-Sep-13", "26-Sep-13", "27-Sep-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-09-page-3-table-1.csv'})

for day in ["21-Aug-02", "22-Aug-02", "23-Aug-02", "24-Aug-02", "25-Aug-02", "26-Aug-02", "27-Aug-02", "28-Aug-02", "29-Aug-02", "30-Aug-02", "31-Aug-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-08-page-3-table-1.csv'})

for day in ["22-Aug-14", "23-Aug-14", "24-Aug-14", "25-Aug-14", "26-Aug-14", "27-Aug-14", "28-Aug-14", "29-Aug-14", "30-Aug-14", "31-Aug-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-08-page-3-table-1.csv'})

for day in ["27-Sep-05", "28-Sep-05", "29-Sep-05", "30-Sep-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-09-page-3-table-1.csv'})

for day in ["1-Dec-10", "2-Dec-10", "3-Dec-10", "4-Dec-10", "5-Dec-10", "6-Dec-10", "7-Dec-10", "8-Dec-10", "9-Dec-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-12-page-1-table-1.csv'})

for day in ["10-Sep-10", "11-Sep-10", "12-Sep-10", "13-Sep-10", "14-Sep-10", "15-Sep-10", "16-Sep-10", "17-Sep-10", "18-Sep-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-09-page-2-table-1.csv'})

for day in ["19-Dec-15", "20-Dec-15", "21-Dec-15", "22-Dec-15", "23-Dec-15", "24-Dec-15", "25-Dec-15", "26-Dec-15", "27-Dec-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-12-page-3-table-1.csv'})

for day in ["19-Jun-08", "20-Jun-08", "21-Jun-08", "22-Jun-08", "23-Jun-08", "24-Jun-08", "25-Jun-08", "26-Jun-08", "27-Jun-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-06-page-3-table-1.csv'})

for day in ["11-Aug-01", "12-Aug-01", "13-Aug-01", "14-Aug-01", "15-Aug-01", "16-Aug-01", "17-Aug-01", "18-Aug-01", "19-Aug-01", "20-Aug-01"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2001-08-page-2-table-1.csv'})

for day in ["28-Jan-06", "29-Jan-06", "30-Jan-06", "31-Jan-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-01-page-4-table-1.csv'})

for day in ["1-Aug-11", "2-Aug-11", "3-Aug-11", "4-Aug-11", "5-Aug-11", "6-Aug-11", "7-Aug-11", "8-Aug-11", "9-Aug-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-08-page-1-table-1.csv'})

for day in ["22-May-14", "23-May-14", "24-May-14", "25-May-14", "26-May-14", "27-May-14", "28-May-14", "29-May-14", "30-May-14", "31-May-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-05-page-3-table-1.csv'})

for day in ["19-Nov-09", "20-Nov-09", "21-Nov-09", "22-Nov-09", "23-Nov-09", "24-Nov-09", "25-Nov-09", "26-Nov-09", "27-Nov-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-11-page-3-table-1.csv'})

for day in ["27-Apr-05", "28-Apr-05", "29-Apr-05", "30-Apr-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-04-page-3-table-1.csv'})

for day in ["1-May-11", "2-May-11", "3-May-11", "4-May-11", "5-May-11", "6-May-11", "7-May-11", "8-May-11", "9-May-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-05-page-1-table-1.csv'})

for day in ["10-Apr-10", "11-Apr-10", "12-Apr-10", "13-Apr-10", "14-Apr-10", "15-Apr-10", "16-Apr-10", "17-Apr-10", "18-Apr-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-04-page-2-table-1.csv'})

for day in ["11-May-01", "12-May-01", "13-May-01", "14-May-01", "15-May-01", "16-May-01", "17-May-01", "18-May-01", "19-May-01", "20-May-01"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2001-05-page-2-table-1.csv'})

for day in ["1-Mar-17", "2-Mar-17", "3-Mar-17", "4-Mar-17", "5-Mar-17", "6-Mar-17", "7-Mar-17", "8-Mar-17", "9-Mar-17", "10-Mar-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-03-page-1-table-1.csv'})

for day in ["1-Feb-06", "2-Feb-06", "3-Feb-06", "4-Feb-06", "5-Feb-06", "6-Feb-06", "7-Feb-06", "8-Feb-06", "9-Feb-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-02-page-1-table-1.csv'})

for day in ["10-Mar-07", "11-Mar-07", "12-Mar-07", "13-Mar-07", "14-Mar-07", "15-Mar-07", "16-Mar-07", "17-Mar-07", "18-Mar-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-03-page-2-table-1.csv'})

for day in ["10-Feb-16", "11-Feb-16", "12-Feb-16", "13-Feb-16", "14-Feb-16", "15-Feb-16", "16-Feb-16", "17-Feb-16", "18-Feb-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-02-page-2-table-1.csv'})

for day in ["28-Nov-10", "29-Nov-10", "30-Nov-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-11-page-4-table-1.csv'})

for day in ["24-Feb-03", "25-Feb-03", "26-Feb-03", "27-Feb-03", "28-Feb-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-02-page-3-table-1.csv'})

for day in ["19-Mar-12", "20-Mar-12", "21-Mar-12", "22-Mar-12", "23-Mar-12", "24-Mar-12", "25-Mar-12", "26-Mar-12", "27-Mar-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-03-page-3-table-1.csv'})

for day in ["28-Jun-11", "29-Jun-11", "30-Jun-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-06-page-4-table-1.csv'})

for day in ["26-Jul-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-07-page-4-table-1.csv'})

for day in ["28-Jun-07", "29-Jun-07", "30-Jun-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-06-page-4-table-1.csv'})

for day in ["19-Jan-09", "20-Jan-09", "21-Jan-09", "22-Jan-09", "23-Jan-09", "24-Jan-09", "25-Jan-09", "26-Jan-09", "27-Jan-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-01-page-3-table-1.csv'})

for day in ["27-Mar-04", "28-Mar-04", "29-Mar-04", "30-Mar-04", "31-Mar-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-03-page-3-table-1.csv'})

for day in ["19-Feb-15", "20-Feb-15", "21-Feb-15", "22-Feb-15", "23-Feb-15", "24-Feb-15", "25-Feb-15", "26-Feb-15", "27-Feb-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-02-page-3-table-1.csv'})

for day in ["28-Nov-06", "29-Nov-06", "30-Nov-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-11-page-4-table-1.csv'})

for day in ["10-Mar-11", "11-Mar-11", "12-Mar-11", "13-Mar-11", "14-Mar-11", "15-Mar-11", "16-Mar-11", "17-Mar-11", "18-Mar-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-03-page-2-table-1.csv'})

for day in ["1-Feb-10", "2-Feb-10", "3-Feb-10", "4-Feb-10", "5-Feb-10", "6-Feb-10", "7-Feb-10", "8-Feb-10", "9-Feb-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-02-page-1-table-1.csv'})

for day in ["1-May-19", "2-May-19", "3-May-19", "4-May-19", "5-May-19", "6-May-19", "7-May-19", "8-May-19", "9-May-19", "10-May-19", "11-May-19", "12-May-19", "13-May-19", "14-May-19", "15-May-19", "16-May-19", "17-May-19"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2019-05-page-1-table-1.csv'})

for day in ["1-Oct-15", "2-Oct-15", "3-Oct-15", "4-Oct-15", "5-Oct-15", "6-Oct-15", "7-Oct-15", "8-Oct-15", "9-Oct-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-10-page-1-table-1.csv'})

for day in ["1-Apr-08", "2-Apr-08", "3-Apr-08", "4-Apr-08", "5-Apr-08", "6-Apr-08", "7-Apr-08", "8-Apr-08", "9-Apr-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-04-page-1-table-1.csv'})

for day in ["1-Nov-04", "2-Nov-04", "3-Nov-04", "4-Nov-04", "5-Nov-04", "6-Nov-04", "7-Nov-04", "8-Nov-04", "9-Nov-04", "10-Nov-04", "11-Nov-04", "12-Nov-04", "13-Nov-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-11-page-1-table-1.csv'})

for day in ["10-May-09", "11-May-09", "12-May-09", "13-May-09", "14-May-09", "15-May-09", "16-May-09", "17-May-09", "18-May-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-05-page-2-table-1.csv'})

for day in ["14-Oct-05", "15-Oct-05", "16-Oct-05", "17-Oct-05", "18-Oct-05", "19-Oct-05", "20-Oct-05", "21-Oct-05", "22-Oct-05", "23-Oct-05", "24-Oct-05", "25-Oct-05", "26-Oct-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-10-page-2-table-1.csv'})

for day in ["18-Apr-18", "19-Apr-18", "20-Apr-18", "21-Apr-18", "22-Apr-18", "23-Apr-18", "24-Apr-18", "25-Apr-18", "26-Apr-18", "27-Apr-18", "28-Apr-18", "29-Apr-18", "30-Apr-18"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2018-04-page-2-table-1.csv'})

for day in ["10-Nov-14", "11-Nov-14", "12-Nov-14", "13-Nov-14", "14-Nov-14", "15-Nov-14", "16-Nov-14", "17-Nov-14", "18-Nov-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-11-page-2-table-1.csv'})

for day in ["28-Feb-12", "29-Feb-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-02-page-4-table-1.csv'})

for day in ["21-Nov-01", "22-Nov-01", "23-Nov-01", "24-Nov-01", "25-Nov-01", "26-Nov-01", "27-Nov-01", "28-Nov-01", "29-Nov-01", "30-Nov-01"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2001-11-page-3-table-1.csv'})

for day in ["19-Oct-10", "20-Oct-10", "21-Oct-10", "22-Oct-10", "23-Oct-10", "24-Oct-10", "25-Oct-10", "26-Oct-10", "27-Oct-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-10-page-3-table-1.csv'})

for day in ["10-Aug-09", "11-Aug-09", "12-Aug-09", "13-Aug-09", "14-Aug-09", "15-Aug-09", "16-Aug-09", "17-Aug-09", "18-Aug-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-08-page-2-table-1.csv'})

for day in ["19-Jul-11", "20-Jul-11", "21-Jul-11", "22-Jul-11", "23-Jul-11", "24-Jul-11", "25-Jul-11", "26-Jul-11", "27-Jul-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-07-page-3-table-1.csv'})

for day in ["18-Sep-18", "19-Sep-18", "20-Sep-18", "21-Sep-18", "22-Sep-18", "23-Sep-18", "24-Sep-18", "25-Sep-18", "26-Sep-18", "27-Sep-18", "28-Sep-18", "29-Sep-18", "30-Sep-18"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2018-09-page-2-table-1.csv'})

for day in ["1-Aug-19", "2-Aug-19", "3-Aug-19", "4-Aug-19", "5-Aug-19", "6-Aug-19", "7-Aug-19", "8-Aug-19", "9-Aug-19", "10-Aug-19", "11-Aug-19", "12-Aug-19", "13-Aug-19", "14-Aug-19", "15-Aug-19", "16-Aug-19", "17-Aug-19"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2019-08-page-1-table-1.csv'})

for day in ["1-Sep-08", "2-Sep-08", "3-Sep-08", "4-Sep-08", "5-Sep-08", "6-Sep-08", "7-Sep-08", "8-Sep-08", "9-Sep-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-09-page-1-table-1.csv'})

for day in ["10-Dec-08", "11-Dec-08", "12-Dec-08", "13-Dec-08", "14-Dec-08", "15-Dec-08", "16-Dec-08", "17-Dec-08", "18-Dec-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-12-page-2-table-1.csv'})

for day in ["14-Jul-04", "15-Jul-04", "16-Jul-04", "17-Jul-04", "18-Jul-04", "19-Jul-04", "20-Jul-04", "21-Jul-04", "22-Jul-04", "23-Jul-04", "24-Jul-04", "25-Jul-04", "26-Jul-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-07-page-2-table-1.csv'})

for day in ["10-Jun-15", "11-Jun-15", "12-Jun-15", "13-Jun-15", "14-Jun-15", "15-Jun-15", "16-Jun-15", "17-Jun-15", "18-Jun-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-06-page-2-table-1.csv'})

for day in ["1-Dec-18", "2-Dec-18", "3-Dec-18", "4-Dec-18", "5-Dec-18", "6-Dec-18", "7-Dec-18", "8-Dec-18", "9-Dec-18", "10-Dec-18", "11-Dec-18", "12-Dec-18", "13-Dec-18", "14-Dec-18", "15-Dec-18", "16-Dec-18", "17-Dec-18", "18-Dec-18", "19-Dec-18"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2018-12-page-1-table-1.csv'})

for day in ["1-Jul-14", "2-Jul-14", "3-Jul-14", "4-Jul-14", "5-Jul-14", "6-Jul-14", "7-Jul-14", "8-Jul-14", "9-Jul-14", "10-Jul-14", "11-Jul-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-07-page-1-table-1.csv'})

for day in ["1-Jun-05", "2-Jun-05", "3-Jun-05", "4-Jun-05", "5-Jun-05", "6-Jun-05", "7-Jun-05", "8-Jun-05", "9-Jun-05", "10-Jun-05", "11-Jun-05", "12-Jun-05", "13-Jun-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-06-page-1-table-1.csv'})

for day in ["1-Jun-13", "2-Jun-13", "3-Jun-13", "4-Jun-13", "5-Jun-13", "6-Jun-13", "7-Jun-13", "8-Jun-13", "9-Jun-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-06-page-1-table-1.csv'})

for day in ["13-Jun-03", "14-Jun-03", "15-Jun-03", "16-Jun-03", "17-Jun-03", "18-Jun-03", "19-Jun-03", "20-Jun-03", "21-Jun-03", "22-Jun-03", "23-Jun-03", "24-Jun-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-06-page-2-table-1.csv'})

for day in ["10-Jul-12", "11-Jul-12", "12-Jul-12", "13-Jul-12", "14-Jul-12", "15-Jul-12", "16-Jul-12", "17-Jul-12", "18-Jul-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-07-page-2-table-1.csv'})

for day in ["19-Jul-07", "20-Jul-07", "21-Jul-07", "22-Jul-07", "23-Jul-07", "24-Jul-07", "25-Jul-07", "26-Jul-07", "27-Jul-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-07-page-3-table-1.csv'})

for day in ["19-Jun-16", "20-Jun-16", "21-Jun-16", "22-Jun-16", "23-Jun-16", "24-Jun-16", "25-Jun-16", "26-Jun-16", "27-Jun-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-06-page-3-table-1.csv'})

for day in ["19-Oct-06", "20-Oct-06", "21-Oct-06", "22-Oct-06", "23-Oct-06", "24-Oct-06", "25-Oct-06", "26-Oct-06", "27-Oct-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-10-page-3-table-1.csv'})

for day in ["28-Mar-15", "29-Mar-15", "30-Mar-15", "31-Mar-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-03-page-4-table-1.csv'})

for day in ["11-Nov-02", "12-Nov-02", "13-Nov-02", "14-Nov-02", "15-Nov-02", "16-Nov-02", "17-Nov-02", "18-Nov-02", "19-Nov-02", "20-Nov-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-11-page-2-table-1.csv'})

for day in ["10-Oct-13", "11-Oct-13", "12-Oct-13", "13-Oct-13", "14-Oct-13", "15-Oct-13", "16-Oct-13", "17-Oct-13", "18-Oct-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-10-page-2-table-1.csv'})

for day in ["1-Nov-12", "2-Nov-12", "3-Nov-12", "4-Nov-12", "5-Nov-12", "6-Nov-12", "7-Nov-12", "8-Nov-12", "9-Nov-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-11-page-1-table-1.csv'})

for day in ["1-Oct-03", "2-Oct-03", "3-Oct-03", "4-Oct-03", "5-Oct-03", "6-Oct-03", "7-Oct-03", "8-Oct-03", "9-Oct-03", "10-Oct-03", "11-Oct-03", "12-Oct-03", "13-Oct-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-10-page-1-table-1.csv'})

for day in ["18-Mar-19", "19-Mar-19", "20-Mar-19", "21-Mar-19", "22-Mar-19", "23-Mar-19", "24-Mar-19", "25-Mar-19", "26-Mar-19", "27-Mar-19", "28-Mar-19", "29-Mar-19", "30-Mar-19", "31-Mar-19"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2019-03-page-2-table-1.csv'})

for day in ["10-Feb-08", "11-Feb-08", "12-Feb-08", "13-Feb-08", "14-Feb-08", "15-Feb-08", "16-Feb-08", "17-Feb-08", "18-Feb-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-02-page-2-table-1.csv'})

for day in ["1-Mar-09", "2-Mar-09", "3-Mar-09", "4-Mar-09", "5-Mar-09", "6-Mar-09", "7-Mar-09", "8-Mar-09", "9-Mar-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-03-page-1-table-1.csv'})

for day in ["1-Feb-18", "2-Feb-18", "3-Feb-18", "4-Feb-18", "5-Feb-18", "6-Feb-18", "7-Feb-18", "8-Feb-18", "9-Feb-18", "10-Feb-18", "11-Feb-18", "12-Feb-18", "13-Feb-18", "14-Feb-18", "15-Feb-18", "16-Feb-18", "17-Feb-18"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2018-02-page-1-table-1.csv'})

for day in ["28-May-13", "29-May-13", "30-May-13", "31-May-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-05-page-4-table-1.csv'})

for day in ["28-Dec-12", "29-Dec-12", "30-Dec-12", "31-Dec-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-12-page-4-table-1.csv'})

for day in ["1-Jan-04", "2-Jan-04", "3-Jan-04", "4-Jan-04", "5-Jan-04", "6-Jan-04", "7-Jan-04", "8-Jan-04", "9-Jan-04", "10-Jan-04", "11-Jan-04", "12-Jan-04", "13-Jan-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-01-page-1-table-1.csv'})

for day in ["28-Aug-13", "29-Aug-13", "30-Aug-13", "31-Aug-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-08-page-4-table-1.csv'})

for day in ["10-Jan-14", "11-Jan-14", "12-Jan-14", "13-Jan-14", "14-Jan-14", "15-Jan-14", "16-Jan-14", "17-Jan-14", "18-Jan-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-01-page-2-table-1.csv'})

for day in ["11-Jan-02", "12-Jan-02", "13-Jan-02", "14-Jan-02", "15-Jan-02", "16-Jan-02", "17-Jan-02", "18-Jan-02", "19-Jan-02", "20-Jan-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-01-page-2-table-1.csv'})

for day in ["1-Jan-12", "2-Jan-12", "3-Jan-12", "4-Jan-12", "5-Jan-12", "6-Jan-12", "7-Jan-12", "8-Jan-12", "9-Jan-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-01-page-1-table-1.csv'})

for day in ['28-Jul-08', '29-Jul-08', '30-Jul-08', '31-Jul-08']:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-07-page-4-table-1.csv'})

for day in ["28-Oct-09", "29-Oct-09", "30-Oct-09", "31-Oct-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-10-page-4-table-1.csv'})

for day in ["19-Jan-07", "20-Jan-07", "21-Jan-07", "22-Jan-07", "23-Jan-07", "24-Jan-07", "25-Jan-07", "26-Jan-07", "27-Jan-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-01-page-3-table-1.csv'})

for day in ["28-Dec-14", "29-Dec-14", "30-Dec-14", "31-Dec-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-12-page-4-table-1.csv'})

for day in ["28-Jun-09", "29-Jun-09", "30-Jun-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-06-page-4-table-1.csv'})

for day in ["10-Jan-12", "11-Jan-12", "12-Jan-12", "13-Jan-12", "14-Jan-12", "15-Jan-12", "16-Jan-12", "17-Jan-12", "18-Jan-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-01-page-2-table-1.csv'})

for day in ["28-Aug-15", "29-Aug-15", "30-Aug-15", "31-Aug-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-08-page-4-table-1.csv'})

for day in ["1-Jan-02", "2-Jan-02", "3-Jan-02", "4-Jan-02", "5-Jan-02", "6-Jan-02", "7-Jan-02", "8-Jan-02", "9-Jan-02", "10-Jan-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-01-page-1-table-1.csv'})

for day in ["28-May-15", "29-May-15", "30-May-15", "31-May-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-05-page-4-table-1.csv'})

for day in ["28-Nov-08", "29-Nov-08", "30-Nov-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-11-page-4-table-1.csv'})

for day in ["28-Apr-12", "29-Apr-12", "30-Apr-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-04-page-4-table-1.csv'})

for day in ["10-Mar-09", "11-Mar-09", "12-Mar-09", "13-Mar-09", "14-Mar-09", "15-Mar-09", "16-Mar-09", "17-Mar-09", "18-Mar-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-03-page-2-table-1.csv'})

for day in ["18-Feb-18", "19-Feb-18", "20-Feb-18", "21-Feb-18", "22-Feb-18", "23-Feb-18", "24-Feb-18", "25-Feb-18", "26-Feb-18", "27-Feb-18", "28-Feb-18"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2018-02-page-2-table-1.csv'})

for day in ["1-Mar-19", "2-Mar-19", "3-Mar-19", "4-Mar-19", "5-Mar-19", "6-Mar-19", "7-Mar-19", "8-Mar-19", "9-Mar-19", "10-Mar-19", "11-Mar-19", "12-Mar-19", "13-Mar-19", "14-Mar-19", "15-Mar-19", "16-Mar-19", "17-Mar-19"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2019-03-page-1-table-1.csv'})

for day in ["1-Feb-08", "2-Feb-08", "3-Feb-08", "4-Feb-08", "5-Feb-08", "6-Feb-08", "7-Feb-08", "8-Feb-08", "9-Feb-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-02-page-1-table-1.csv'})

for day in ["28-Sep-12", "29-Sep-12", "30-Sep-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-09-page-4-table-1.csv'})

for day in ["1-Jan-14", "2-Jan-14", "3-Jan-14", "4-Jan-14", "5-Jan-14", "6-Jan-14", "7-Jan-14", "8-Jan-14", "9-Jan-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-01-page-1-table-1.csv'})

for day in ["14-Jan-04", "15-Jan-04", "16-Jan-04", "17-Jan-04", "18-Jan-04", "19-Jan-04", "20-Jan-04", "21-Jan-04", "22-Jan-04", "23-Jan-04", "24-Jan-04", "25-Jan-04", "26-Jan-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-01-page-2-table-1.csv'})

for day in ["19-Jan-11", "20-Jan-11", "21-Jan-11", "22-Jan-11", "23-Jan-11", "24-Jan-11", "25-Jan-11", "26-Jan-11", "27-Jan-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-01-page-3-table-1.csv'})

for day in ["28-Jan-08", "29-Jan-08", "30-Jan-08", "31-Jan-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-01-page-4-table-1.csv'})

for day in ["19-Jun-06", "20-Jun-06", "21-Jun-06", "22-Jun-06", "23-Jun-06", "24-Jun-06", "25-Jun-06", "26-Jun-06", "27-Jun-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-06-page-3-table-1.csv'})

for day in ["1-Jun-03", "2-Jun-03", "3-Jun-03", "4-Jun-03", "5-Jun-03", "6-Jun-03", "7-Jun-03", "8-Jun-03", "9-Jun-03", "10-Jun-03", "11-Jun-03", "12-Jun-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-06-page-1-table-1.csv'})

for day in ["1-Jul-12", "2-Jul-12", "3-Jul-12", "4-Jul-12", "5-Jul-12", "6-Jul-12", "7-Jul-12", "8-Jul-12", "9-Jul-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-07-page-1-table-1.csv'})

for day in ["10-Jun-13", "11-Jun-13", "12-Jun-13", "13-Jun-13", "14-Jun-13", "15-Jun-13", "16-Jun-13", "17-Jun-13", "18-Jun-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-06-page-2-table-1.csv'})

for day in ["10-Nov-12", "11-Nov-12", "12-Nov-12", "13-Nov-12", "14-Nov-12", "15-Nov-12", "16-Nov-12", "17-Nov-12", "18-Nov-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-11-page-2-table-1.csv'})

for day in ["14-Oct-03", "15-Oct-03", "16-Oct-03", "17-Oct-03", "18-Oct-03", "19-Oct-03", "20-Oct-03", "21-Oct-03", "22-Oct-03", "23-Oct-03", "24-Oct-03", "25-Oct-03", "26-Oct-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-10-page-2-table-1.csv'})

for day in ["1-Nov-02", "2-Nov-02", "3-Nov-02", "4-Nov-02", "5-Nov-02", "6-Nov-02", "7-Nov-02", "8-Nov-02", "9-Nov-02", "10-Nov-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-11-page-1-table-1.csv'})

for day in ["1-Oct-13", "2-Oct-13", "3-Oct-13", "4-Oct-13", "5-Oct-13", "6-Oct-13", "7-Oct-13", "8-Oct-13", "9-Oct-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-10-page-1-table-1.csv'})

for day in ["17-Oct-16", "18-Oct-16", "19-Oct-16", "20-Oct-16", "21-Oct-16", "22-Oct-16", "23-Oct-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-10-page-3-table-1.csv'})

for day in ["19-Nov-07", "20-Nov-07", "21-Nov-07", "22-Nov-07", "23-Nov-07", "24-Nov-07", "25-Nov-07", "26-Nov-07", "27-Nov-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-11-page-3-table-1.csv'})

for day in ["28-Mar-13", "29-Mar-13", "30-Mar-13", "31-Mar-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-03-page-4-table-1.csv'})

for day in ["19-Nov-11", "20-Nov-11", "21-Nov-11", "22-Nov-11", "23-Nov-11", "24-Nov-11", "25-Nov-11", "26-Nov-11", "27-Nov-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-11-page-3-table-1.csv'})

for day in ["1-Oct-05", "2-Oct-05", "3-Oct-05", "4-Oct-05", "5-Oct-05", "6-Oct-05", "7-Oct-05", "8-Oct-05", "9-Oct-05", "10-Oct-05", "11-Oct-05", "12-Oct-05", "13-Oct-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-10-page-1-table-1.csv'})

for day in ["1-May-09", "2-May-09", "3-May-09", "4-May-09", "5-May-09", "6-May-09", "7-May-09", "8-May-09", "9-May-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-05-page-1-table-1.csv'})

for day in ["1-Nov-14", "2-Nov-14", "3-Nov-14", "4-Nov-14", "5-Nov-14", "6-Nov-14", "7-Nov-14", "8-Nov-14", "9-Nov-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-11-page-1-table-1.csv'})

for day in ["1-Apr-18", "2-Apr-18", "3-Apr-18", "4-Apr-18", "5-Apr-18", "6-Apr-18", "7-Apr-18", "8-Apr-18", "9-Apr-18", "10-Apr-18", "11-Apr-18", "12-Apr-18", "13-Apr-18", "14-Apr-18", "15-Apr-18", "16-Apr-18", "17-Apr-18"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2018-04-page-1-table-1.csv'})

for day in ["10-Oct-15", "11-Oct-15", "12-Oct-15", "13-Oct-15", "14-Oct-15", "15-Oct-15", "16-Oct-15", "17-Oct-15", "18-Oct-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-10-page-2-table-1.csv'})

for day in ["18-May-19", "19-May-19", "20-May-19", "21-May-19", "22-May-19", "23-May-19", "24-May-19", "25-May-19", "26-May-19", "27-May-19", "28-May-19", "29-May-19", "30-May-19", "31-May-19"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2019-05-page-2-table-1.csv'})

for day in ["14-Nov-04", "15-Nov-04", "16-Nov-04", "17-Nov-04", "18-Nov-04", "19-Nov-04", "20-Nov-04", "21-Nov-04", "22-Nov-04", "23-Nov-04", "24-Nov-04", "25-Nov-04", "26-Nov-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-11-page-2-table-1.csv'})

for day in ["10-Apr-08", "11-Apr-08", "12-Apr-08", "13-Apr-08", "14-Apr-08", "15-Apr-08", "16-Apr-08", "17-Apr-08", "18-Apr-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-04-page-2-table-1.csv'})

for day in ["12-Jul-14", "13-Jul-14", "14-Jul-14", "15-Jul-14", "16-Jul-14", "17-Jul-14", "18-Jul-14", "19-Jul-14", "20-Jul-14", "21-Jul-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-07-page-2-table-1.csv'})

for day in ["20-Dec-18", "21-Dec-18", "22-Dec-18", "23-Dec-18", "24-Dec-18", "25-Dec-18", "26-Dec-18", "27-Dec-18", "28-Dec-18", "29-Dec-18", "30-Dec-18", "31-Dec-18"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2018-12-page-2-table-1.csv'})

for day in ["14-Jun-05", "15-Jun-05", "16-Jun-05", "17-Jun-05", "18-Jun-05", "19-Jun-05", "20-Jun-05", "21-Jun-05", "22-Jun-05", "23-Jun-05", "24-Jun-05", "25-Jun-05", "26-Jun-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-06-page-2-table-1.csv'})

for day in ["1-Jul-04", "2-Jul-04", "3-Jul-04", "4-Jul-04", "5-Jul-04", "6-Jul-04", "7-Jul-04", "8-Jul-04", "9-Jul-04", "10-Jul-04", "11-Jul-04", "12-Jul-04", "13-Jul-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-07-page-1-table-1.csv'})

for day in ["1-Dec-08", "2-Dec-08", "3-Dec-08", "4-Dec-08", "5-Dec-08", "6-Dec-08", "7-Dec-08", "8-Dec-08", "9-Dec-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-12-page-1-table-1.csv'})

for day in ["1-Jun-15", "2-Jun-15", "3-Jun-15", "4-Jun-15", "5-Jun-15", "6-Jun-15", "7-Jun-15", "8-Jun-15", "9-Jun-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-06-page-1-table-1.csv'})

for day in ["19-Jun-10", "20-Jun-10", "21-Jun-10", "22-Jun-10", "23-Jun-10", "24-Jun-10", "25-Jun-10", "26-Jun-10", "27-Jun-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-06-page-3-table-1.csv'})

for day in ["18-Aug-19", "19-Aug-19", "20-Aug-19", "21-Aug-19", "22-Aug-19", "23-Aug-19", "24-Aug-19", "25-Aug-19", "26-Aug-19", "27-Aug-19", "28-Aug-19", "29-Aug-19", "30-Aug-19", "31-Aug-19"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2019-08-page-2-table-1.csv'})

for day in ["10-Sep-08", "11-Sep-08", "12-Sep-08", "13-Sep-08", "14-Sep-08", "15-Sep-08", "16-Sep-08", "17-Sep-08", "18-Sep-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-09-page-2-table-1.csv'})

for day in ["21-Jul-01", "22-Jul-01", "23-Jul-01", "24-Jul-01", "25-Jul-01", "26-Jul-01", "Capacity", "27-Jul-01", "28-Jul-01", "29-Jul-01", "30-Jul-01", "31-Jul-01"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2001-07-page-3-table-1.csv'})

for day in ["1-Aug-09", "2-Aug-09", "3-Aug-09", "4-Aug-09", "5-Aug-09", "6-Aug-09", "7-Aug-09", "8-Aug-09", "9-Aug-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-08-page-1-table-1.csv'})

for day in ["1-Sep-18", "2-Sep-18", "3-Sep-18", "4-Sep-18", "5-Sep-18", "6-Sep-18", "7-Sep-18", "8-Sep-18", "9-Sep-18", "10-Sep-18", "11-Sep-18", "12-Sep-18", "13-Sep-18", "14-Sep-18", "15-Sep-18", "16-Sep-18", "17-Sep-18"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2018-09-page-1-table-1.csv'})

for day in ["28-Jul-06", "29-Jul-06", "30-Jul-06", "31-Jul-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-07-page-4-table-1.csv'})

for day in ["10-Feb-10", "11-Feb-10", "12-Feb-10", "13-Feb-10", "14-Feb-10", "15-Feb-10", "16-Feb-10", "17-Feb-10", "18-Feb-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-02-page-2-table-1.csv'})

for day in ["1-Mar-11", "2-Mar-11", "3-Mar-11", "4-Mar-11", "5-Mar-11", "6-Mar-11", "7-Mar-11", "8-Mar-11", "9-Mar-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-03-page-1-table-1.csv'})

for day in ["22-Mar-14", "23-Mar-14", "24-Mar-14", "25-Mar-14", "26-Mar-14", "27-Mar-14", "28-Mar-14", "29-Mar-14", "30-Mar-14", "31-Mar-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-03-page-3-table-1.csv'})

for day in ["25-Feb-05", "26-Feb-05", "27-Feb-05", "28-Feb-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-02-page-3-table-1.csv'})

for day in ["28-Oct-07", "29-Oct-07", "30-Oct-07", "31-Oct-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-10-page-4-table-1.csv'})

for day in ["24-Nov-16", "25-Nov-16", "26-Nov-16", "27-Nov-16", "28-Nov-16", "29-Nov-16", "30-Nov-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-11-page-4-table-1.csv'})

for day in ["28-Oct-11", "29-Oct-11", "30-Oct-11", "31-Oct-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-10-page-4-table-1.csv'})

for day in ["19-Feb-13", "20-Feb-13", "21-Feb-13", "22-Feb-13", "23-Feb-13", "24-Feb-13", "25-Feb-13", "26-Feb-13", "27-Feb-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-02-page-3-table-1.csv'})

for day in ["21-Mar-02", "22-Mar-02", "23-Mar-02", "24-Mar-02", "25-Mar-02", "26-Mar-02", "27-Mar-02", "28-Mar-02", "29-Mar-02", "30-Mar-02", "31-Mar-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-03-page-3-table-1.csv'})

for day in ["1-Mar-07", "2-Mar-07", "3-Mar-07", "4-Mar-07", "5-Mar-07", "6-Mar-07", "7-Mar-07", "8-Mar-07", "9-Mar-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-03-page-1-table-1.csv'})

for day in ["1-Feb-16", "2-Feb-16", "3-Feb-16", "4-Feb-16", "5-Feb-16", "6-Feb-16", "7-Feb-16", "8-Feb-16", "9-Feb-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-02-page-1-table-1.csv'})

for day in ["11-Mar-17", "12-Mar-17", "13-Mar-17", "14-Mar-17", "15-Mar-17", "16-Mar-17", "17-Mar-17", "18-Mar-17", "19-Mar-17", "20-Mar-17", "21-Mar-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-03-page-2-table-1.csv'})

for day in ["10-Feb-06", "11-Feb-06", "12-Feb-06", "13-Feb-06", "14-Feb-06", "15-Feb-06", "16-Feb-06", "17-Feb-06", "18-Feb-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-02-page-2-table-1.csv'})

for day in ["28-Jul-10", "29-Jul-10", "30-Jul-10", "31-Jul-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-07-page-4-table-1.csv'})

for day in ["27-Dec-05", "28-Dec-05", "29-Dec-05", "30-Dec-05", "31-Dec-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-12-page-3-table-1.csv'})

for day in ["19-Jul-09", "20-Jul-09", "21-Jul-09", "22-Jul-09", "23-Jul-09", "24-Jul-09", "25-Jul-09", "26-Jul-09", "27-Jul-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-07-page-3-table-1.csv'})

for day in ["10-Aug-11", "11-Aug-11", "12-Aug-11", "13-Aug-11", "14-Aug-11", "15-Aug-11", "16-Aug-11", "17-Aug-11", "18-Aug-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-08-page-2-table-1.csv'})

for day in ["1-Sep-10", "2-Sep-10", "3-Sep-10", "4-Sep-10", "5-Sep-10", "6-Sep-10", "7-Sep-10", "8-Sep-10", "9-Sep-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-09-page-1-table-1.csv'})

for day in ["28-Jan-16", "29-Jan-16", "30-Jan-16", "31-Jan-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-01-page-4-table-1.csv'})

for day in ["1-Aug-01", "2-Aug-01", "3-Aug-01", "4-Aug-01", "5-Aug-01", "6-Aug-01", "7-Aug-01", "8-Aug-01", "9-Aug-01", "10-Aug-01"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2001-08-page-1-table-1.csv'})

for day in ["27-Aug-04", "28-Aug-04", "29-Aug-04", "30-Aug-04", "31-Aug-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-08-page-3-table-1.csv'})

for day in ["19-Sep-15", "20-Sep-15", "21-Sep-15", "22-Sep-15", "23-Sep-15", "24-Sep-15", "25-Sep-15", "26-Sep-15", "27-Sep-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-09-page-3-table-1.csv'})

for day in ["10-Dec-10", "11-Dec-10", "12-Dec-10", "13-Dec-10", "14-Dec-10", "15-Dec-10", "16-Dec-10", "17-Dec-10", "18-Dec-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-12-page-2-table-1.csv'})

for day in ["1-Apr-10", "2-Apr-10", "3-Apr-10", "4-Apr-10", "5-Apr-10", "6-Apr-10", "7-Apr-10", "8-Apr-10", "9-Apr-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-04-page-1-table-1.csv'})

for day in ["1-May-01", "2-May-01", "3-May-01", "4-May-01", "5-May-01", "6-May-01", "7-May-01", "8-May-01", "9-May-01", "10-May-01"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2001-05-page-1-table-1.csv'})

for day in ["10-May-11", "11-May-11", "12-May-11", "13-May-11", "14-May-11", "15-May-11", "16-May-11", "17-May-11", "18-May-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-05-page-2-table-1.csv'})

for day in ["27-May-04", "28-May-04", "29-May-04", "30-May-04", "31-May-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-05-page-3-table-1.csv'})

for day in ["19-Oct-08", "20-Oct-08", "21-Oct-08", "22-Oct-08", "23-Oct-08", "24-Oct-08", "25-Oct-08", "26-Oct-08", "27-Oct-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-10-page-3-table-1.csv'})

for day in ["19-Apr-15", "20-Apr-15", "21-Apr-15", "22-Apr-15", "23-Apr-15", "24-Apr-15", "25-Apr-15", "26-Apr-15", "27-Apr-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-04-page-3-table-1.csv'})

for day in ["24-Apr-03", "25-Apr-03", "26-Apr-03", "27-Apr-03", "28-Apr-03", "29-Apr-03", "30-Apr-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-04-page-3-table-1.csv'})

for day in ["19-May-12", "20-May-12", "21-May-12", "22-May-12", "23-May-12", "24-May-12", "25-May-12", "26-May-12", "27-May-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-05-page-3-table-1.csv'})

for day in ["10-May-07", "11-May-07", "12-May-07", "13-May-07", "14-May-07", "15-May-07", "16-May-07", "17-May-07", "18-May-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-05-page-2-table-1.csv'})

for day in ["10-Apr-16", "11-Apr-16", "12-Apr-16", "13-Apr-16", "14-Apr-16", "15-Apr-16", "16-Apr-16", "17-Apr-16", "18-Apr-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-04-page-2-table-1.csv'})

for day in ["1-May-17", "2-May-17", "3-May-17", "4-May-17", "5-May-17", "6-May-17", "7-May-17", "8-May-17", "9-May-17", "10-May-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-05-page-1-table-1.csv'})

for day in ["1-Apr-06", "2-Apr-06", "3-Apr-06", "4-Apr-06", "5-Apr-06", "6-Apr-06", "7-Apr-06", "8-Apr-06", "9-Apr-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-04-page-1-table-1.csv'})

for day in ["1-Dec-16", "2-Dec-16", "3-Dec-16", "4-Dec-16", "5-Dec-16", "6-Dec-16", "7-Dec-16", "8-Dec-16", "9-Dec-16", "10-Dec-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-12-page-1-table-1.csv'})

for day in ["27-Sep-03", "28-Sep-03", "29-Sep-03", "30-Sep-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-09-page-3-table-1.csv'})

for day in ["10-Dec-06", "11-Dec-06", "12-Dec-06", "13-Dec-06", "14-Dec-06", "15-Dec-06", "16-Dec-06", "17-Dec-06", "18-Dec-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-12-page-2-table-1.csv'})

for day in ["19-Aug-12", "20-Aug-12", "21-Aug-12", "22-Aug-12", "23-Aug-12", "24-Aug-12", "25-Aug-12", "26-Aug-12", "27-Aug-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-08-page-3-table-1.csv'})

for day in ["1-Aug-17", "2-Aug-17", "3-Aug-17", "4-Aug-17", "5-Aug-17", "6-Aug-17", "7-Aug-17", "8-Aug-17", "9-Aug-17", "10-Aug-17", "11-Aug-17", "12-Aug-17", "13-Aug-17", "14-Aug-17", "15-Aug-17", "16-Aug-17", "17-Aug-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-08-page-1-table-1.csv'})

for day in ["1-Sep-06", "2-Sep-06", "3-Sep-06", "4-Sep-06", "5-Sep-06", "6-Sep-06", "7-Sep-06", "8-Sep-06", "9-Sep-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-09-page-1-table-1.csv'})

for day in ["10-Aug-07", "11-Aug-07", "12-Aug-07", "13-Aug-07", "14-Aug-07", "15-Aug-07", "16-Aug-07", "17-Aug-07", "18-Aug-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-08-page-2-table-1.csv'})

for day in ["19-Dec-13", "20-Dec-13", "21-Dec-13", "22-Dec-13", "23-Dec-13", "24-Dec-13", "25-Dec-13", "26-Dec-13", "27-Dec-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-12-page-3-table-1.csv'})

for day in ["11-Sep-16", "12-Sep-16", "13-Sep-16", "14-Sep-16", "15-Sep-16", "16-Sep-16", "17-Sep-16", "18-Sep-16", "19-Sep-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-09-page-2-table-1.csv'})

for day in ["10-Jun-11", "11-Jun-11", "12-Jun-11", "13-Jun-11", "14-Jun-11", "15-Jun-11", "16-Jun-11", "17-Jun-11", "18-Jun-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-06-page-2-table-1.csv'})

for day in ["19-Sep-09", "20-Sep-09", "21-Sep-09", "22-Sep-09", "23-Sep-09", "24-Sep-09", "25-Sep-09", "26-Sep-09", "27-Sep-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-09-page-3-table-1.csv'})

for day in ["1-Jun-01", "2-Jun-01", "3-Jun-01", "4-Jun-01", "5-Jun-01", "6-Jun-01", "7-Jun-01", "8-Jun-01", "9-Jun-01", "10-Jun-01"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2001-06-page-1-table-1.csv'})

for day in ["1-Jul-10", "2-Jul-10", "3-Jul-10", "4-Jul-10", "5-Jul-10", "6-Jul-10", "7-Jul-10", "8-Jul-10", "9-Jul-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-07-page-1-table-1.csv'})

for day in ["19-Jul-15", "20-Jul-15", "21-Jul-15", "22-Jul-15", "23-Jul-15", "24-Jul-15", "25-Jul-15", "26-Jul-15", "27-Jul-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-07-page-3-table-1.csv'})

for day in ["27-Jun-04", "28-Jun-04", "29-Jun-04", "30-Jun-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-06-page-3-table-1.csv'})

for day in ["28-Mar-07", "29-Mar-07", "30-Mar-07", "31-Mar-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-03-page-4-table-1.csv'})

for day in ["28-Feb-16", "29-Feb-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-02-page-4-table-1.csv'})

for day in ["19-Oct-14", "20-Oct-14", "21-Oct-14", "22-Oct-14", "23-Oct-14", "24-Oct-14", "25-Oct-14", "26-Oct-14", "27-Oct-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-10-page-3-table-1.csv'})

for day in ["27-Nov-05", "28-Nov-05", "29-Nov-05", "30-Nov-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-11-page-3-table-1.csv'})

for day in ["19-Apr-09", "20-Apr-09", "21-Apr-09", "22-Apr-09", "23-Apr-09", "24-Apr-09", "25-Apr-09", "26-Apr-09", "27-Apr-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-04-page-3-table-1.csv'})

for day in ["1-Oct-11", "2-Oct-11", "3-Oct-11", "4-Oct-11", "5-Oct-11", "6-Oct-11", "7-Oct-11", "8-Oct-11", "9-Oct-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-10-page-1-table-1.csv'})

for day in ["10-Nov-10", "11-Nov-10", "12-Nov-10", "13-Nov-10", "14-Nov-10", "15-Nov-10", "16-Nov-10", "17-Nov-10", "18-Nov-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-11-page-2-table-1.csv'})

for day in ["11-Oct-01", "12-Oct-01", "13-Oct-01", "14-Oct-01", "15-Oct-01", "16-Oct-01", "17-Oct-01", "18-Oct-01", "19-Oct-01", "20-Oct-01"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2001-10-page-2-table-1.csv'})

for day in ["24-Oct-17", "25-Oct-17", "26-Oct-17", "27-Oct-17", "28-Oct-17", "29-Oct-17", "30-Oct-17", "31-Oct-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-10-page-2-table-1.csv'})

for day in ["10-Nov-06", "11-Nov-06", "12-Nov-06", "13-Nov-06", "14-Nov-06", "15-Nov-06", "16-Nov-06", "17-Nov-06", "18-Nov-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-11-page-2-table-1.csv'})

for day in ["1-Oct-07", "2-Oct-07", "3-Oct-07", "4-Oct-07", "5-Oct-07", "6-Oct-07", "7-Oct-07", "8-Oct-07", "9-Oct-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-10-page-1-table-1.csv'})

for day in ["1-Nov-16", "2-Nov-16", "3-Nov-16", "4-Nov-16", "5-Nov-16", "6-Nov-16", "7-Nov-16", "8-Nov-16", "9-Nov-16", "10-Nov-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-11-page-1-table-1.csv'})

for day in ["19-Nov-13", "20-Nov-13", "21-Nov-13", "22-Nov-13", "23-Nov-13", "24-Nov-13", "25-Nov-13", "26-Nov-13", "27-Nov-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-11-page-3-table-1.csv'})

for day in ["21-Oct-02", "22-Oct-02", "23-Oct-02", "24-Oct-02", "25-Oct-02", "26-Oct-02", "27-Oct-02", "28-Oct-02", "29-Oct-02", "30-Oct-02", "31-Oct-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-10-page-3-table-1.csv'})

for day in ["28-Mar-11", "29-Mar-11", "30-Mar-11", "31-Mar-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-03-page-4-table-1.csv'})

for day in ["19-Jun-12", "20-Jun-12", "21-Jun-12", "22-Jun-12", "23-Jun-12", "24-Jun-12", "25-Jun-12", "26-Jun-12", "27-Jun-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-06-page-3-table-1.csv'})

for day in ["27-Jul-03", "28-Jul-03", "29-Jul-03", "30-Jul-03", "31-Jul-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-07-page-3-table-1.csv'})

for day in ["1-Jul-06", "2-Jul-06", "3-Jul-06", "4-Jul-06", "5-Jul-06", "6-Jul-06", "7-Jul-06", "8-Jul-06", "9-Jul-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-07-page-1-table-1.csv'})

for day in ["1-Jun-17", "2-Jun-17", "3-Jun-17", "4-Jun-17", "5-Jun-17", "6-Jun-17", "7-Jun-17", "8-Jun-17", "9-Jun-17", "10-Jun-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-06-page-1-table-1.csv'})

for day in ["10-Jul-16", "11-Jul-16", "12-Jul-16", "13-Jul-16", "14-Jul-16", "15-Jul-16", "16-Jul-16", "17-Jul-16", "18-Jul-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-07-page-2-table-1.csv'})

for day in ["10-Jun-07", "11-Jun-07", "12-Jun-07", "13-Jun-07", "14-Jun-07", "15-Jun-07", "16-Jun-07", "17-Jun-07", "18-Jun-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-06-page-2-table-1.csv'})

for day in ["28-Sep-06", "29-Sep-06", "30-Sep-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-09-page-4-table-1.csv'})

for day in ['10-Jan-10', '11-Jan-10', '12-Jan-10', '13-Jan-10', '14-Jan-10', '15-Jan-10', '16-Jan-10', '17-Jan-10', '18-Jan-10']:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-01-page-2-table-1.csv'})

for day in ["24-Dec-16", "25-Dec-16", "26-Dec-16", "27-Dec-16", "28-Dec-16", "29-Dec-16", "30-Dec-16", "31-Dec-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-12-page-4-table-1.csv'})

for day in ["27-Jan-05", "28-Jan-05", "29-Jan-05", "30-Jan-05", "31-Jan-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-01-page-3-table-1.csv'})

for day in ["19-Mar-08", "20-Mar-08", "21-Mar-08", "22-Mar-08", "23-Mar-08", "24-Mar-08", "25-Mar-08", "26-Mar-08", "27-Mar-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-03-page-3-table-1.csv'})

for day in ["28-Apr-06", "29-Apr-06", "30-Apr-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-04-page-4-table-1.csv'})

for day in ["28-Apr-10", "29-Apr-10", "30-Apr-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-04-page-4-table-1.csv'})

for day in ["19-Jan-13", "20-Jan-13", "21-Jan-13", "22-Jan-13", "23-Jan-13", "24-Jan-13", "25-Jan-13", "26-Jan-13", "27-Jan-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-01-page-3-table-1.csv'})

for day in ["10-Jan-06", "11-Jan-06", "12-Jan-06", "13-Jan-06", "14-Jan-06", "15-Jan-06", "16-Jan-06", "17-Jan-06", "18-Jan-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-01-page-2-table-1.csv'})

for day in ["28-Sep-10", "29-Sep-10", "30-Sep-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-09-page-4-table-1.csv'})

for day in ["1-Jan-16", "2-Jan-16", "3-Jan-16", "4-Jan-16", "5-Jan-16", "6-Jan-16", "7-Jan-16", "8-Jan-16", "9-Jan-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-01-page-1-table-1.csv'})

for day in ["19-Aug-06", "20-Aug-06", "21-Aug-06", "22-Aug-06", "23-Aug-06", "24-Aug-06", "25-Aug-06", "26-Aug-06", "27-Aug-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-08-page-3-table-1.csv'})

for day in ["10-Dec-12", "11-Dec-12", "12-Dec-12", "13-Dec-12", "14-Dec-12", "15-Dec-12", "16-Dec-12", "17-Dec-12", "18-Dec-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-12-page-2-table-1.csv'})

for day in ["1-Sep-12", "2-Sep-12", "3-Sep-12", "4-Sep-12", "5-Sep-12", "6-Sep-12", "7-Sep-12", "8-Sep-12", "9-Sep-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-09-page-1-table-1.csv'})

for day in ["28-Jan-14", "29-Jan-14", "30-Jan-14", "31-Jan-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-01-page-4-table-1.csv'})

for day in ["1-Aug-03", "2-Aug-03", "3-Aug-03", "4-Aug-03", "5-Aug-03", "6-Aug-03", "7-Aug-03", "8-Aug-03", "9-Aug-03", "10-Aug-03", "11-Aug-03", "12-Aug-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-08-page-1-table-1.csv'})

for day in ["11-Sep-02", "12-Sep-02", "13-Sep-02", "14-Sep-02", "15-Sep-02", "16-Sep-02", "17-Sep-02", "18-Sep-02", "19-Sep-02", "20-Sep-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-09-page-2-table-1.csv'})

for day in ["19-Dec-07", "20-Dec-07", "21-Dec-07", "22-Dec-07", "23-Dec-07", "24-Dec-07", "25-Dec-07", "26-Dec-07", "27-Dec-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-12-page-3-table-1.csv'})

for day in ["10-Aug-13", "11-Aug-13", "12-Aug-13", "13-Aug-13", "14-Aug-13", "15-Aug-13", "16-Aug-13", "17-Aug-13", "18-Aug-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-08-page-2-table-1.csv'})

for day in ["19-May-06", "20-May-06", "21-May-06", "22-May-06", "23-May-06", "24-May-06", "25-May-06", "26-May-06", "27-May-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-05-page-3-table-1.csv'})

for day in ["22-Apr-17", "23-Apr-17", "24-Apr-17", "25-Apr-17", "26-Apr-17", "27-Apr-17", "28-Apr-17", "29-Apr-17", "30-Apr-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-04-page-3-table-1.csv'})

for day in ["28-Feb-08", "29-Feb-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-02-page-4-table-1.csv'})

for day in ["11-Apr-02", "12-Apr-02", "13-Apr-02", "14-Apr-02", "15-Apr-02", "16-Apr-02", "17-Apr-02", "18-Apr-02", "19-Apr-02", "20-Apr-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-04-page-2-table-1.csv'})

for day in ["10-May-13", "11-May-13", "12-May-13", "13-May-13", "14-May-13", "15-May-13", "16-May-13", "17-May-13", "18-May-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-05-page-2-table-1.csv'})

for day in ["1-Apr-12", "2-Apr-12", "3-Apr-12", "4-Apr-12", "5-Apr-12", "6-Apr-12", "7-Apr-12", "8-Apr-12", "9-Apr-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-04-page-1-table-1.csv'})

for day in ["1-May-03", "2-May-03", "3-May-03", "4-May-03", "5-May-03", "6-May-03", "7-May-03", "8-May-03", "9-May-03", "10-May-03", "11-May-03", "12-May-03", "13-May-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-05-page-1-table-1.csv'})

for day in ["1-May-15", "2-May-15", "3-May-15", "4-May-15", "5-May-15", "6-May-15", "7-May-15", "8-May-15", "9-May-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-05-page-1-table-1.csv'})

for day in ["1-Oct-19", "2-Oct-19", "3-Oct-19", "4-Oct-19", "5-Oct-19", "6-Oct-19", "7-Oct-19", "8-Oct-19", "9-Oct-19", "10-Oct-19", "11-Oct-19", "12-Oct-19", "13-Oct-19", "14-Oct-19", "15-Oct-19", "16-Oct-19", "17-Oct-19"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2019-10-page-1-table-1.csv'})

for day in ["1-Apr-04", "2-Apr-04", "3-Apr-04", "4-Apr-04", "5-Apr-04", "6-Apr-04", "7-Apr-04", "8-Apr-04", "9-Apr-04", "10-Apr-04", "11-Apr-04", "12-Apr-04", "13-Apr-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-04-page-1-table-1.csv'})

for day in ["1-Nov-08", "2-Nov-08", "3-Nov-08", "4-Nov-08", "5-Nov-08", "6-Nov-08", "7-Nov-08", "8-Nov-08", "9-Nov-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-11-page-1-table-1.csv'})

for day in ["14-May-05", "15-May-05", "16-May-05", "17-May-05", "18-May-05", "19-May-05", "20-May-05", "21-May-05", "22-May-05", "23-May-05", "24-May-05", "25-May-05", "26-May-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-05-page-2-table-1.csv'})

for day in ["10-Oct-09", "11-Oct-09", "12-Oct-09", "13-Oct-09", "14-Oct-09", "15-Oct-09", "16-Oct-09", "17-Oct-09", "18-Oct-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-10-page-2-table-1.csv'})

for day in ["11-Apr-14", "12-Apr-14", "13-Apr-14", "14-Apr-14", "15-Apr-14", "16-Apr-14", "17-Apr-14", "18-Apr-14", "19-Apr-14", "20-Apr-14", "21-Apr-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-04-page-2-table-1.csv'})

for day in ["20-Nov-18", "21-Nov-18", "22-Nov-18", "23-Nov-18", "24-Nov-18", "25-Nov-18", "26-Nov-18", "27-Nov-18", "28-Nov-18", "29-Nov-18", "30-Nov-18"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2018-11-page-2-table-1.csv'})

for day in ["19-May-10", "20-May-10", "21-May-10", "22-May-10", "23-May-10", "24-May-10", "25-May-10", "26-May-10", "27-May-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-05-page-3-table-1.csv'})

for day in ["14-Aug-05", "15-Aug-05", "16-Aug-05", "17-Aug-05", "18-Aug-05", "19-Aug-05", "20-Aug-05", "21-Aug-05", "22-Aug-05", "23-Aug-05", "24-Aug-05", "25-Aug-05", "26-Aug-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-08-page-2-table-1.csv'})

for day in ["11-Sep-14", "12-Sep-14", "13-Sep-14", "14-Sep-14", "15-Sep-14", "16-Sep-14", "17-Sep-14", "18-Sep-14", "19-Sep-14", "20-Sep-14", "21-Sep-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-09-page-2-table-1.csv'})

for day in ["19-Dec-11", "20-Dec-11", "21-Dec-11", "22-Dec-11", "23-Dec-11", "24-Dec-11", "25-Dec-11", "26-Dec-11", "27-Dec-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-12-page-3-table-1.csv'})

for day in ["1-Aug-15", "2-Aug-15", "3-Aug-15", "4-Aug-15", "5-Aug-15", "6-Aug-15", "7-Aug-15", "8-Aug-15", "9-Aug-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-08-page-1-table-1.csv'})

for day in ["1-Sep-04", "2-Sep-04", "3-Sep-04", "4-Sep-04", "5-Sep-04", "6-Sep-04", "7-Sep-04", "8-Sep-04", "9-Sep-04", "10-Sep-04", "11-Sep-04", "12-Sep-04", "13-Sep-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-09-page-1-table-1.csv'})

for day in ["14-Dec-04", "15-Dec-04", "16-Dec-04", "17-Dec-04", "18-Dec-04", "19-Dec-04", "20-Dec-04", "21-Dec-04", "22-Dec-04", "23-Dec-04", "24-Dec-04", "25-Dec-04", "26-Dec-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-12-page-2-table-1.csv'})

for day in ["10-Jul-08", "11-Jul-08", "12-Jul-08", "13-Jul-08", "14-Jul-08", "15-Jul-08", "16-Jul-08", "17-Jul-08", "18-Jul-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-07-page-2-table-1.csv'})

for day in ["21-Sep-01", "22-Sep-01", "23-Sep-01", "24-Sep-01", "25-Sep-01", "26-Sep-01", "27-Sep-01", "28-Sep-01", "29-Sep-01", "30-Sep-01"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2001-09-page-3-table-1.csv'})

for day in ["19-Aug-10", "20-Aug-10", "21-Aug-10", "22-Aug-10", "23-Aug-10", "24-Aug-10", "25-Aug-10", "26-Aug-10", "27-Aug-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-08-page-3-table-1.csv'})

for day in ["21-Jun-19", "22-Jun-19", "23-Jun-19", "24-Jun-19", "25-Jun-19", "26-Jun-19", "27-Jun-19", "28-Jun-19", "29-Jun-19", "30-Jun-19"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2019-06-page-2-table-1.csv'})

for day in ["1-Dec-14", "2-Dec-14", "3-Dec-14", "4-Dec-14", "5-Dec-14", "6-Dec-14", "7-Dec-14", "8-Dec-14", "9-Dec-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-12-page-1-table-1.csv'})

for day in ["1-Jul-18", "2-Jul-18", "3-Jul-18", "4-Jul-18", "5-Jul-18", "6-Jul-18", "7-Jul-18", "8-Jul-18", "9-Jul-18", "10-Jul-18", "11-Jul-18", "12-Jul-18", "13-Jul-18", "14-Jul-18", "15-Jul-18", "16-Jul-18", "17-Jul-18"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2018-07-page-1-table-1.csv'})

for day in ["1-Jun-09", "2-Jun-09", "3-Jun-09", "4-Jun-09", "5-Jun-09", "6-Jun-09", "7-Jun-09", "8-Jun-09", "9-Jun-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-06-page-1-table-1.csv'})

for day in ["28-Aug-09", "29-Aug-09", "30-Aug-09", "31-Aug-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-08-page-4-table-1.csv'})

for day in ["28-Dec-08", "29-Dec-08", "30-Dec-08", "31-Dec-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-12-page-4-table-1.csv'})

for day in ["28-Jun-15", "29-Jun-15", "30-Jun-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-06-page-4-table-1.csv'})

for day in ["28-May-09", "29-May-09", "30-May-09", "31-May-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-05-page-4-table-1.csv'})

for day in ["28-Nov-14", "29-Nov-14", "30-Nov-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-11-page-4-table-1.csv'})

for day in ["19-Mar-16", "20-Mar-16", "21-Mar-16", "22-Mar-16", "23-Mar-16", "24-Mar-16", "25-Mar-16", "26-Mar-16", "27-Mar-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-03-page-3-table-1.csv'})

for day in ["19-Feb-07", "20-Feb-07", "21-Feb-07", "22-Feb-07", "23-Feb-07", "24-Feb-07", "25-Feb-07", "26-Feb-07", "27-Feb-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-02-page-3-table-1.csv'})

for day in ["1-Feb-02", "2-Feb-02", "3-Feb-02", "4-Feb-02", "5-Feb-02", "6-Feb-02", "7-Feb-02", "8-Feb-02", "9-Feb-02", "10-Feb-02", "11-Feb-02", "12-Feb-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-02-page-1-table-1.csv'})

for day in ["1-Mar-13", "2-Mar-13", "3-Mar-13", "4-Mar-13", "5-Mar-13", "6-Mar-13", "7-Mar-13", "8-Mar-13", "9-Mar-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-03-page-1-table-1.csv'})

for day in ["10-Feb-12", "11-Feb-12", "12-Feb-12", "13-Feb-12", "14-Feb-12", "15-Feb-12", "16-Feb-12", "17-Feb-12", "18-Feb-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-02-page-2-table-1.csv'})

for day in ["14-Mar-03", "15-Mar-03", "16-Mar-03", "17-Mar-03", "18-Mar-03", "19-Mar-03", "20-Mar-03", "21-Mar-03", "22-Mar-03", "23-Mar-03", "24-Mar-03", "25-Mar-03", "26-Mar-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-03-page-2-table-1.csv'})

for day in ["10-Mar-15", "11-Mar-15", "12-Mar-15", "13-Mar-15", "14-Mar-15", "15-Mar-15", "16-Mar-15", "17-Mar-15", "18-Mar-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-03-page-2-table-1.csv'})

for day in ["13-Feb-04", "14-Feb-04", "15-Feb-04", "16-Feb-04", "17-Feb-04", "18-Feb-04", "19-Feb-04", "20-Feb-04", "21-Feb-04", "22-Feb-04", "23-Feb-04", "24-Feb-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-02-page-2-table-1.csv'})

for day in ["1-Mar-05", "2-Mar-05", "3-Mar-05", "4-Mar-05", "5-Mar-05", "6-Mar-05", "7-Mar-05", "8-Mar-05", "9-Mar-05", "10-Mar-05", "11-Mar-05", "12-Mar-05", "13-Mar-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-03-page-1-table-1.csv'})

for day in ["1-Feb-14", "2-Feb-14", "3-Feb-14", "4-Feb-14", "5-Feb-14", "6-Feb-14", "7-Feb-14", "8-Feb-14", "9-Feb-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-02-page-1-table-1.csv'})

for day in ["19-Feb-11", "20-Feb-11", "21-Feb-11", "22-Feb-11", "23-Feb-11", "24-Feb-11", "25-Feb-11", "26-Feb-11", "27-Feb-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-02-page-3-table-1.csv'})

for day in ["28-Oct-13", "29-Oct-13", "30-Oct-13", "31-Oct-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-10-page-4-table-1.csv'})

for day in ["28-Jul-12", "29-Jul-12", "30-Jul-12", "31-Jul-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-07-page-4-table-1.csv'})

for day in ["1-Jan-08", "2-Jan-08", "3-Jan-08", "4-Jan-08", "5-Jan-08", "6-Jan-08", "7-Jan-08", "8-Jan-08", "9-Jan-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-01-page-1-table-1.csv'})

for day in ["18-Jan-18", "19-Jan-18", "20-Jan-18", "21-Jan-18", "22-Jan-18", "23-Jan-18", "24-Jan-18", "25-Jan-18", "26-Jan-18", "27-Jan-18", "28-Jan-18", "29-Jan-18", "30-Jan-18", "31-Jan-18"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2018-01-page-2-table-1.csv'})

for day in ["19-Jan-14", "20-Jan-14", "21-Jan-14", "22-Jan-14", "23-Jan-14", "24-Jan-14", "25-Jan-14", "26-Jan-14", "27-Jan-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-01-page-3-table-1.csv'})

for day in ["28-Dec-07", "29-Dec-07", "30-Dec-07", "31-Dec-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-12-page-4-table-1.csv'})

for day in ["1-Jan-11", "2-Jan-11", "3-Jan-11", "4-Jan-11", "5-Jan-11", "6-Jan-11", "7-Jan-11", "8-Jan-11", "9-Jan-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-01-page-1-table-1.csv'})

for day in ["28-Aug-06", "29-Aug-06", "30-Aug-06", "31-Aug-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-08-page-4-table-1.csv'})

for day in ["28-May-06", "29-May-06", "30-May-06", "31-May-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-05-page-4-table-1.csv'})

for day in ["19-Feb-08", "20-Feb-08", "21-Feb-08", "22-Feb-08", "23-Feb-08", "24-Feb-08", "25-Feb-08", "26-Feb-08", "27-Feb-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-02-page-3-table-1.csv'})

for day in ["28-May-09", "29-May-09", "30-May-09", "31-May-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-05-page-4-table-1.csv'})

for day in ["28-Aug-10", "29-Aug-10", "30-Aug-10", "31-Aug-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-08-page-4-table-1.csv'})

for day in ["1-Jan-07", "2-Jan-07", "3-Jan-07", "4-Jan-07", "5-Jan-07", "6-Jan-07", "7-Jan-07", "8-Jan-07", "9-Jan-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-01-page-1-table-1.csv'})

for day in ["19-Jan-17", "20-Jan-17", "21-Jan-17", "22-Jan-17", "23-Jan-17", "24-Jan-17", "25-Jan-17", "26-Jan-17", "27-Jan-17", "28-Jan-17", "29-Jan-17", "30-Jan-17", "31-Jan-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-01-page-2-table-1.csv'})

for day in ["28-Dec-11", "29-Dec-11", "30-Dec-11", "31-Dec-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-12-page-4-table-1.csv'})

for day in ["21-Jan-02", "22-Jan-02", "23-Jan-02", "24-Jan-02", "25-Jan-02", "26-Jan-02", "27-Jan-02", "28-Jan-02", "29-Jan-02", "30-Jan-02", "31-Jan-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-01-page-3-table-1.csv'})

for day in ["19-Jun-15", "20-Jun-15", "21-Jun-15", "22-Jun-15", "23-Jun-15", "24-Jun-15", "25-Jun-15", "26-Jun-15", "27-Jun-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-06-page-3-table-1.csv'})

for day in ["19-Dec-08", "20-Dec-08", "21-Dec-08", "22-Dec-08", "23-Dec-08", "24-Dec-08", "25-Dec-08", "26-Dec-08", "27-Dec-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-12-page-3-table-1.csv'})

for day in ["27-Jul-04", "28-Jul-04", "29-Jul-04", "30-Jul-04", "31-Jul-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-07-page-3-table-1.csv'})

for day in ["1-Jul-01", "2-Jul-01", "3-Jul-01", "4-Jul-01", "5-Jul-01", "6-Jul-01", "7-Jul-01", "8-Jul-01", "9-Jul-01", "10-Jul-01"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2001-07-page-1-table-1.csv'})

for day in ["1-Jun-10", "2-Jun-10", "3-Jun-10", "4-Jun-10", "5-Jun-10", "6-Jun-10", "7-Jun-10", "8-Jun-10", "9-Jun-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-06-page-1-table-1.csv'})

for day in ["10-Jul-11", "11-Jul-11", "12-Jul-11", "13-Jul-11", "14-Jul-11", "15-Jul-11", "16-Jul-11", "17-Jul-11", "18-Jul-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-07-page-2-table-1.csv'})

for day in ["19-Aug-09", "20-Aug-09", "21-Aug-09", "22-Aug-09", "23-Aug-09", "24-Aug-09", "25-Aug-09", "26-Aug-09", "27-Aug-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-08-page-3-table-1.csv'})

for day in ["10-Oct-10", "11-Oct-10", "12-Oct-10", "13-Oct-10", "14-Oct-10", "15-Oct-10", "16-Oct-10", "17-Oct-10", "18-Oct-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-10-page-2-table-1.csv'})

for day in ["11-Nov-01", "12-Nov-01", "13-Nov-01", "14-Nov-01", "15-Nov-01", "16-Nov-01", "17-Nov-01", "18-Nov-01", "19-Nov-01", "20-Nov-01"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2001-11-page-2-table-1.csv'})

for day in ["1-Nov-11", "2-Nov-11", "3-Nov-11", "4-Nov-11", "5-Nov-11", "6-Nov-11", "7-Nov-11", "8-Nov-11", "9-Nov-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-11-page-1-table-1.csv'})

for day in ["19-Nov-14", "20-Nov-14", "Capacity", "21-Nov-14", "22-Nov-14", "23-Nov-14", "24-Nov-14", "25-Nov-14", "26-Nov-14", "27-Nov-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-11-page-3-table-1.csv'})

for day in ["19-May-09", "20-May-09", "21-May-09", "22-May-09", "23-May-09", "24-May-09", "25-May-09", "26-May-09", "27-May-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-05-page-3-table-1.csv'})

for day in ["27-Oct-05", "28-Oct-05", "29-Oct-05", "30-Oct-05", "31-Oct-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-10-page-3-table-1.csv'})

for day in ["28-Feb-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-02-page-4-table-1.csv'})

for day in ["28-Mar-16", "29-Mar-16", "30-Mar-16", "31-Mar-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-03-page-4-table-1.csv'})

for day in ["28-Feb-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-02-page-4-table-1.csv'})

for day in ["19-Oct-13", "20-Oct-13", "21-Oct-13", "22-Oct-13", "23-Oct-13", "24-Oct-13", "25-Oct-13", "26-Oct-13", "27-Oct-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-10-page-3-table-1.csv'})

for day in ["21-Nov-02", "22-Nov-02", "23-Nov-02", "24-Nov-02", "25-Nov-02", "26-Nov-02", "27-Nov-02", "28-Nov-02", "29-Nov-02", "30-Nov-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-11-page-3-table-1.csv'})

for day in ["1-Nov-07", "2-Nov-07", "3-Nov-07", "4-Nov-07", "5-Nov-07", "6-Nov-07", "7-Nov-07", "8-Nov-07", "9-Nov-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-11-page-1-table-1.csv'})

for day in ["1-Oct-16", "2-Oct-16", "3-Oct-16", "4-Oct-16", "5-Oct-16", "6-Oct-16", "7-Oct-16", "8-Oct-16", "9-Oct-16", "10-Oct-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-10-page-1-table-1.csv'})

for day in ["18-Nov-17", "19-Nov-17", "20-Nov-17", "21-Nov-17", "22-Nov-17", "23-Nov-17", "24-Nov-17", "25-Nov-17", "26-Nov-17", "27-Nov-17", "28-Nov-17", "29-Nov-17", "30-Nov-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-11-page-2-table-1.csv'})

for day in ["10-Oct-06", "11-Oct-06", "12-Oct-06", "13-Oct-06", "14-Oct-06", "15-Oct-06", "16-Oct-06", "17-Oct-06", "18-Oct-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-10-page-2-table-1.csv'})

for day in ["10-Jun-16", "11-Jun-16", "12-Jun-16", "13-Jun-16", "14-Jun-16", "15-Jun-16", "16-Jun-16", "17-Jun-16", "18-Jun-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-06-page-2-table-1.csv'})

for day in ["10-Jul-07", "11-Jul-07", "12-Jul-07", "13-Jul-07", "14-Jul-07", "15-Jul-07", "16-Jul-07", "17-Jul-07", "18-Jul-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-07-page-2-table-1.csv'})

for day in ["1-Jun-06", "2-Jun-06", "3-Jun-06", "4-Jun-06", "5-Jun-06", "6-Jun-06", "7-Jun-06", "8-Jun-06", "9-Jun-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-06-page-1-table-1.csv'})

for day in ["1-Jul-17", "2-Jul-17", "3-Jul-17", "4-Jul-17", "5-Jul-17", "6-Jul-17", "7-Jul-17", "8-Jul-17", "9-Jul-17", "10-Jul-17", "11-Jul-17", "12-Jul-17", "13-Jul-17", "14-Jul-17", "15-Jul-17", "16-Jul-17", "17-Jul-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-07-page-1-table-1.csv'})

for day in ["19-Jul-12", "20-Jul-12", "21-Jul-12", "22-Jul-12", "23-Jul-12", "24-Jul-12", "25-Jul-12", "26-Jul-12", "27-Jul-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-07-page-3-table-1.csv'})

for day in ["25-Jun-03", "26-Jun-03", "27-Jun-03", "28-Jun-03", "29-Jun-03", "30-Jun-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-06-page-3-table-1.csv'})

for day in ["28-Jul-15", "29-Jul-15", "30-Jul-15", "31-Jul-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-07-page-4-table-1.csv'})

for day in ["28-Sep-09", "29-Sep-09", "30-Sep-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-09-page-4-table-1.csv'})

for day in ["10-Mar-12", "11-Mar-12", "12-Mar-12", "13-Mar-12", "14-Mar-12", "15-Mar-12", "16-Mar-12", "17-Mar-12", "18-Mar-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-03-page-2-table-1.csv'})

for day in ["13-Feb-03", "14-Feb-03", "15-Feb-03", "16-Feb-03", "17-Feb-03", "18-Feb-03", "19-Feb-03", "20-Feb-03", "21-Feb-03", "22-Feb-03", "23-Feb-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-02-page-2-table-1.csv'})

for day in ["1-Mar-02", "2-Mar-02", "3-Mar-02", "4-Mar-02", "5-Mar-02", "6-Mar-02", "7-Mar-02", "8-Mar-02", "9-Mar-02", "10-Mar-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-03-page-1-table-1.csv'})

for day in ["1-Feb-13", "2-Feb-13", "3-Feb-13", "4-Feb-13", "5-Feb-13", "6-Feb-13", "7-Feb-13", "8-Feb-13", "9-Feb-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-02-page-1-table-1.csv'})

for day in ["19-Feb-16", "20-Feb-16", "21-Feb-16", "22-Feb-16", "23-Feb-16", "24-Feb-16", "25-Feb-16", "26-Feb-16", "27-Feb-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-02-page-3-table-1.csv'})

for day in ["19-Mar-07", "20-Mar-07", "21-Mar-07", "22-Mar-07", "23-Mar-07", "24-Mar-07", "25-Mar-07", "26-Mar-07", "27-Mar-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-03-page-3-table-1.csv'})

for day in ["28-Apr-09", "29-Apr-09", "30-Apr-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-04-page-4-table-1.csv'})

for day in ["28-Oct-14", "29-Oct-14", "30-Oct-14", "31-Oct-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-10-page-4-table-1.csv'})

for day in ["28-Nov-13", "29-Nov-13", "30-Nov-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-11-page-4-table-1.csv'})

for day in ["19-Mar-11", "20-Mar-11", "21-Mar-11", "22-Mar-11", "23-Mar-11", "24-Mar-11", "25-Mar-11", "26-Mar-11", "27-Mar-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-03-page-3-table-1.csv'})

for day in ["1-Feb-05", "2-Feb-05", "3-Feb-05", "4-Feb-05", "5-Feb-05", "6-Feb-05", "7-Feb-05", "8-Feb-05", "9-Feb-05", "10-Feb-05", "11-Feb-05", "12-Feb-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-02-page-1-table-1.csv'})

for day in ["1-Mar-14", "2-Mar-14", "3-Mar-14", "4-Mar-14", "5-Mar-14", "6-Mar-14", "7-Mar-14", "8-Mar-14", "9-Mar-14", "10-Mar-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-03-page-1-table-1.csv'})

for day in ["10-Feb-15", "11-Feb-15", "12-Feb-15", "13-Feb-15", "14-Feb-15", "15-Feb-15", "16-Feb-15", "17-Feb-15", "18-Feb-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-02-page-2-table-1.csv'})

for day in ["14-Mar-04", "15-Mar-04", "16-Mar-04", "17-Mar-04", "18-Mar-04", "19-Mar-04", "20-Mar-04", "21-Mar-04", "22-Mar-04", "23-Mar-04", "24-Mar-04", "25-Mar-04", "26-Mar-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-03-page-2-table-1.csv'})

for day in ["10-Jan-09", "11-Jan-09", "12-Jan-09", "13-Jan-09", "14-Jan-09", "15-Jan-09", "16-Jan-09", "17-Jan-09", "18-Jan-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-01-page-2-table-1.csv'})

for day in ["1-Jan-19", "2-Jan-19", "3-Jan-19", "4-Jan-19", "5-Jan-19", "6-Jan-19", "7-Jan-19", "8-Jan-19", "9-Jan-19", "10-Jan-19", "11-Jan-19", "12-Jan-19", "13-Jan-19", "14-Jan-19", "15-Jan-19", "16-Jan-19", "17-Jan-19"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2019-01-page-1-table-1.csv'})

for day in ["27-Jul-16", "28-Jul-16", "29-Jul-16", "30-Jul-16", "31-Jul-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-07-page-5-table-1.csv'})

for day in ["28-Jun-12", "29-Jun-12", "30-Jun-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-06-page-4-table-1.csv'})

for day in ["11-Aug-02", "12-Aug-02", "13-Aug-02", "14-Aug-02", "15-Aug-02", "16-Aug-02", "17-Aug-02", "18-Aug-02", "19-Aug-02", "20-Aug-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-08-page-2-table-1.csv'})

for day in ["17-Dec-16", "18-Dec-16", "19-Dec-16", "20-Dec-16", "21-Dec-16", "22-Dec-16", "23-Dec-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-12-page-3-table-1.csv'})

for day in ["10-Sep-13", "11-Sep-13", "12-Sep-13", "13-Sep-13", "14-Sep-13", "15-Sep-13", "16-Sep-13", "17-Sep-13", "18-Sep-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-09-page-2-table-1.csv'})

for day in ["1-Aug-12", "2-Aug-12", "3-Aug-12", "4-Aug-12", "5-Aug-12", "6-Aug-12", "7-Aug-12", "8-Aug-12", "9-Aug-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-08-page-1-table-1.csv'})

for day in ["1-Sep-03", "2-Sep-03", "3-Sep-03", "4-Sep-03", "5-Sep-03", "6-Sep-03", "7-Sep-03", "8-Sep-03", "9-Sep-03", "10-Sep-03", "11-Sep-03", "12-Sep-03", "13-Sep-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-09-page-1-table-1.csv'})

for day in ["19-Sep-06", "20-Sep-06", "21-Sep-06", "22-Sep-06", "23-Sep-06", "24-Sep-06", "25-Sep-06", "26-Sep-06", "27-Sep-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-09-page-3-table-1.csv'})

for day in ["14-Dec-03", "15-Dec-03", "16-Dec-03", "17-Dec-03", "18-Dec-03", "19-Dec-03", "20-Dec-03", "21-Dec-03", "22-Dec-03", "23-Dec-03", "24-Dec-03", "25-Dec-03", "26-Dec-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-12-page-2-table-1.csv'})

for day in ["1-Dec-13", "2-Dec-13", "3-Dec-13", "4-Dec-13", "5-Dec-13", "6-Dec-13", "7-Dec-13", "8-Dec-13", "9-Dec-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-12-page-1-table-1.csv'})

for day in ["1-May-12", "2-May-12", "3-May-12", "4-May-12", "5-May-12", "6-May-12", "7-May-12", "8-May-12", "9-May-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-05-page-1-table-1.csv'})

for day in ["1-Apr-03", "2-Apr-03", "3-Apr-03", "4-Apr-03", "5-Apr-03", "6-Apr-03", "7-Apr-03", "8-Apr-03", "9-Apr-03", "10-Apr-03", "11-Apr-03", "12-Apr-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-04-page-1-table-1.csv'})

for day in ["11-May-02", "12-May-02", "13-May-02", "14-May-02", "15-May-02", "16-May-02", "17-May-02", "18-May-02", "19-May-02", "20-May-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-05-page-2-table-1.csv'})

for day in ["10-Apr-13", "11-Apr-13", "12-Apr-13", "13-Apr-13", "14-Apr-13", "15-Apr-13", "16-Apr-13", "17-Apr-13", "18-Apr-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-04-page-2-table-1.csv'})

for day in ["28-Mar-08", "29-Mar-08", "30-Mar-08", "31-Mar-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-03-page-4-table-1.csv'})

for day in ["19-Apr-06", "20-Apr-06", "21-Apr-06", "22-Apr-06", "23-Apr-06", "24-Apr-06", "25-Apr-06", "26-Apr-06", "27-Apr-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-04-page-3-table-1.csv'})

for day in ["22-May-17", "23-May-17", "24-May-17", "25-May-17", "26-May-17", "27-May-17", "28-May-17", "29-May-17", "30-May-17", "31-May-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-05-page-3-table-1.csv'})

for day in ["21-May-01", "22-May-01", "23-May-01", "24-May-01", "25-May-01", "26-May-01", "27-May-01", "28-May-01", "29-May-01", "30-May-01", "31-May-01"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2001-05-page-3-table-1.csv'})

for day in ["19-Apr-10", "20-Apr-10", "21-Apr-10", "22-Apr-10", "23-Apr-10", "24-Apr-10", "25-Apr-10", "26-Apr-10", "27-Apr-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-04-page-3-table-1.csv'})

for day in ["10-Nov-09", "11-Nov-09", "12-Nov-09", "13-Nov-09", "14-Nov-09", "15-Nov-09", "16-Nov-09", "17-Nov-09", "18-Nov-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-11-page-2-table-1.csv'})

for day in ["14-Apr-05", "15-Apr-05", "16-Apr-05", "17-Apr-05", "18-Apr-05", "19-Apr-05", "20-Apr-05", "21-Apr-05", "22-Apr-05", "23-Apr-05", "24-Apr-05", "25-Apr-05", "26-Apr-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-04-page-2-table-1.csv'})

for day in ["18-Oct-18", "19-Oct-18", "20-Oct-18", "21-Oct-18", "22-Oct-18", "23-Oct-18", "24-Oct-18", "25-Oct-18", "26-Oct-18", "27-Oct-18", "28-Oct-18", "29-Oct-18", "30-Oct-18", "31-Oct-18"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2018-10-page-2-table-1.csv'})

for day in ["11-May-14", "12-May-14", "13-May-14", "14-May-14", "15-May-14", "16-May-14", "17-May-14", "18-May-14", "19-May-14", "20-May-14", "21-May-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-05-page-2-table-1.csv'})

for day in ["1-Apr-15", "2-Apr-15", "3-Apr-15", "4-Apr-15", "5-Apr-15", "6-Apr-15", "7-Apr-15", "8-Apr-15", "9-Apr-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-04-page-1-table-1.csv'})

for day in ["1-Oct-08", "2-Oct-08", "3-Oct-08", "4-Oct-08", "5-Oct-08", "6-Oct-08", "7-Oct-08", "8-Oct-08", "9-Oct-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-10-page-1-table-1.csv'})

for day in ["1-May-04", "2-May-04", "3-May-04", "4-May-04", "5-May-04", "6-May-04", "7-May-04", "8-May-04", "9-May-04", "10-May-04", "11-May-04", "12-May-04", "13-May-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-05-page-1-table-1.csv'})

for day in ["1-Jun-18", "2-Jun-18", "3-Jun-18", "4-Jun-18", "5-Jun-18", "6-Jun-18", "7-Jun-18", "8-Jun-18", "9-Jun-18", "10-Jun-18", "11-Jun-18", "12-Jun-18", "13-Jun-18", "14-Jun-18", "15-Jun-18", "16-Jun-18", "17-Jun-18"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2018-06-page-1-table-1.csv'})

for day in ["1-Jul-09", "2-Jul-09", "3-Jul-09", "4-Jul-09", "5-Jul-09", "6-Jul-09", "7-Jul-09", "8-Jul-09", "9-Jul-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-07-page-1-table-1.csv'})

for day in ["1-Dec-05", "2-Dec-05", "3-Dec-05", "4-Dec-05", "5-Dec-05", "6-Dec-05", "7-Dec-05", "8-Dec-05", "9-Dec-05", "10-Dec-05", "11-Dec-05", "12-Dec-05", "13-Dec-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-12-page-1-table-1.csv'})

for day in ["21-Aug-01", "22-Aug-01", "23-Aug-01", "24-Aug-01", "25-Aug-01", "26-Aug-01", "27-Aug-01", "28-Aug-01", "29-Aug-01", "30-Aug-01", "31-Aug-01"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2001-08-page-3-table-1.csv'})

for day in ["10-Jun-08", "11-Jun-08", "12-Jun-08", "13-Jun-08", "14-Jun-08", "15-Jun-08", "16-Jun-08", "17-Jun-08", "18-Jun-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-06-page-2-table-1.csv'})

for day in ["18-Jul-19", "19-Jul-19", "20-Jul-19", "21-Jul-19", "22-Jul-19", "23-Jul-19", "24-Jul-19", "25-Jul-19", "26-Jul-19", "27-Jul-19", "28-Jul-19", "29-Jul-19", "30-Jul-19", "31-Jul-19"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2019-07-page-2-table-1.csv'})

for day in ["19-Sep-10", "20-Sep-10", "21-Sep-10", "22-Sep-10", "23-Sep-10", "24-Sep-10", "25-Sep-10", "26-Sep-10", "27-Sep-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-09-page-3-table-1.csv'})

for day in ["10-Dec-15", "11-Dec-15", "12-Dec-15", "13-Dec-15", "14-Dec-15", "15-Dec-15", "16-Dec-15", "17-Dec-15", "18-Dec-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-12-page-2-table-1.csv'})

for day in ["28-Jan-13", "29-Jan-13", "30-Jan-13", "31-Jan-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-01-page-4-table-1.csv'})

for day in ["1-Sep-15", "2-Sep-15", "3-Sep-15", "4-Sep-15", "5-Sep-15", "6-Sep-15", "7-Sep-15", "8-Sep-15", "9-Sep-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-09-page-1-table-1.csv'})

for day in ["1-Aug-04", "2-Aug-04", "3-Aug-04", "4-Aug-04", "5-Aug-04", "6-Aug-04", "7-Aug-04", "8-Aug-04", "9-Aug-04", "10-Aug-04", "11-Aug-04", "12-Aug-04", "13-Aug-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-08-page-1-table-1.csv'})

for day in ["14-Sep-05", "15-Sep-05", "16-Sep-05", "17-Sep-05", "18-Sep-05", "19-Sep-05", "20-Sep-05", "21-Sep-05", "22-Sep-05", "23-Sep-05", "24-Sep-05", "25-Sep-05", "26-Sep-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-09-page-2-table-1.csv'})

for day in ["11-Aug-14", "12-Aug-14", "13-Aug-14", "14-Aug-14", "15-Aug-14", "16-Aug-14", "17-Aug-14", "18-Aug-14", "19-Aug-14", "20-Aug-14", "21-Aug-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-08-page-2-table-1.csv'})

for day in ["10-Jul-13", "11-Jul-13", "12-Jul-13", "13-Jul-13", "14-Jul-13", "15-Jul-13", "16-Jul-13", "17-Jul-13", "18-Jul-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-07-page-2-table-1.csv'})

for day in ["11-Jun-02", "12-Jun-02", "13-Jun-02", "14-Jun-02", "15-Jun-02", "16-Jun-02", "17-Jun-02", "18-Jun-02", "19-Jun-02", "20-Jun-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-06-page-2-table-1.csv'})

for day in ["1-Jul-03", "2-Jul-03", "3-Jul-03", "4-Jul-03", "5-Jul-03", "6-Jul-03", "7-Jul-03", "8-Jul-03", "9-Jul-03", "10-Jul-03", "11-Jul-03", "12-Jul-03", "13-Jul-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-07-page-1-table-1.csv'})

for day in ["1-Jun-12", "2-Jun-12", "3-Jun-12", "4-Jun-12", "5-Jun-12", "6-Jun-12", "7-Jun-12", "8-Jun-12", "9-Jun-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-06-page-1-table-1.csv'})

for day in ["22-Jun-17", "23-Jun-17", "24-Jun-17", "25-Jun-17", "26-Jun-17", "27-Jun-17", "28-Jun-17", "29-Jun-17", "30-Jun-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-06-page-3-table-1.csv'})

for day in ["19-Jul-06", "20-Jul-06", "21-Jul-06", "22-Jul-06", "23-Jul-06", "24-Jul-06", "25-Jul-06", "26-Jul-06", "27-Jul-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-07-page-3-table-1.csv'})

for day in ["Area", "Capacity", "17-Nov-16", "18-Nov-16", "19-Nov-16", "20-Nov-16", "21-Nov-16", "22-Nov-16", "23-Nov-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-11-page-3-table-1.csv'})

for day in ["19-Oct-07", "20-Oct-07", "21-Oct-07", "22-Oct-07", "23-Oct-07", "24-Oct-07", "25-Oct-07", "26-Oct-07", "27-Oct-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-10-page-3-table-1.csv'})

for day in ["1-Oct-02", "2-Oct-02", "3-Oct-02", "4-Oct-02", "5-Oct-02", "6-Oct-02", "7-Oct-02", "8-Oct-02", "9-Oct-02", "10-Oct-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-10-page-1-table-1.csv'})

for day in ["1-Nov-13", "2-Nov-13", "3-Nov-13", "4-Nov-13", "5-Nov-13", "6-Nov-13", "7-Nov-13", "8-Nov-13", "9-Nov-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-11-page-1-table-1.csv'})

for day in ["10-Oct-12", "11-Oct-12", "12-Oct-12", "13-Oct-12", "14-Oct-12", "15-Oct-12", "16-Oct-12", "17-Oct-12", "18-Oct-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-10-page-2-table-1.csv'})

for day in ["14-Nov-03", "15-Nov-03", "16-Nov-03", "17-Nov-03", "18-Nov-03", "19-Nov-03", "20-Nov-03", "21-Nov-03", "22-Nov-03", "23-Nov-03", "24-Nov-03", "25-Nov-03", "26-Nov-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-11-page-2-table-1.csv'})

for day in ["18-Apr-19", "19-Apr-19", "20-Apr-19", "21-Apr-19", "22-Apr-19", "23-Apr-19", "24-Apr-19", "25-Apr-19", "26-Apr-19", "27-Apr-19", "28-Apr-19", "29-Apr-19", "30-Apr-19"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2019-04-page-2-table-1.csv'})

for day in ["10-Nov-15", "11-Nov-15", "12-Nov-15", "13-Nov-15", "14-Nov-15", "15-Nov-15", "16-Nov-15", "17-Nov-15", "18-Nov-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-11-page-2-table-1.csv'})

for day in ["10-May-08", "11-May-08", "12-May-08", "13-May-08", "14-May-08", "15-May-08", "16-May-08", "17-May-08", "18-May-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-05-page-2-table-1.csv'})

for day in ["19-Oct-04", "20-Oct-04", "21-Oct-04", "22-Oct-04", "23-Oct-04", "24-Oct-04", "25-Oct-04", "26-Oct-04", "27-Oct-04", "28-Oct-04", "29-Oct-04", "30-Oct-04", "31-Oct-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-10-page-2-table-1.csv'})

for day in ["1-Apr-09", "2-Apr-09", "3-Apr-09", "4-Apr-09", "5-Apr-09", "6-Apr-09", "7-Apr-09", "8-Apr-09", "9-Apr-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-04-page-1-table-1.csv'})

for day in ["1-Nov-05", "2-Nov-05", "3-Nov-05", "4-Nov-05", "5-Nov-05", "6-Nov-05", "7-Nov-05", "8-Nov-05", "9-Nov-05", "10-Nov-05", "11-Nov-05", "12-Nov-05", "13-Nov-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-11-page-1-table-1.csv'})

for day in ["1-May-18", "2-May-18", "3-May-18", "4-May-18", "5-May-18", "6-May-18", "7-May-18", "8-May-18", "9-May-18", "10-May-18", "11-May-18", "12-May-18", "13-May-18", "14-May-18", "15-May-18", "16-May-18", "17-May-18"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2018-05-page-1-table-1.csv'})

for day in ["1-Oct-14", "2-Oct-14", "3-Oct-14", "4-Oct-14", "5-Oct-14", "6-Oct-14", "7-Oct-14", "8-Oct-14", "9-Oct-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-10-page-1-table-1.csv'})

for day in ["19-Oct-11", "20-Oct-11", "21-Oct-11", "22-Oct-11", "23-Oct-11", "24-Oct-11", "25-Oct-11", "26-Oct-11", "27-Oct-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-10-page-3-table-1.csv'})

for day in ["28-Feb-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-02-page-4-table-1.csv'})

for day in ["1-Sep-09", "2-Sep-09", "3-Sep-09", "4-Sep-09", "5-Sep-09", "6-Sep-09", "7-Sep-09", "8-Sep-09", "9-Sep-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-09-page-1-table-1.csv'})

for day in ["1-Aug-18", "2-Aug-18", "3-Aug-18", "4-Aug-18", "5-Aug-18", "6-Aug-18", "7-Aug-18", "8-Aug-18", "9-Aug-18", "10-Aug-18", "11-Aug-18", "12-Aug-18", "13-Aug-18", "14-Aug-18", "15-Aug-18", "16-Aug-18", "17-Aug-18"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2018-08-page-1-table-1.csv'})

for day in ["18-Sep-19", "19-Sep-19", "20-Sep-19", "21-Sep-19", "22-Sep-19", "23-Sep-19", "24-Sep-19", "25-Sep-19", "26-Sep-19", "27-Sep-19", "28-Sep-19", "29-Sep-19", "30-Sep-19"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2019-09-page-2-table-1.csv'})

for day in ["19-Jul-10", "20-Jul-10", "21-Jul-10", "22-Jul-10", "23-Jul-10", "24-Jul-10", "25-Jul-10", "26-Jul-10", "27-Jul-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-07-page-3-table-1.csv'})

for day in ["21-Jun-01", "22-Jun-01", "23-Jun-01", "24-Jun-01", "25-Jun-01", "26-Jun-01", "27-Jun-01", "28-Jun-01", "29-Jun-01", "30-Jun-01"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2001-06-page-3-table-1.csv'})

for day in ["10-Aug-08", "11-Aug-08", "12-Aug-08", "13-Aug-08", "14-Aug-08", "15-Aug-08", "16-Aug-08", "17-Aug-08", "18-Aug-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-08-page-2-table-1.csv'})

for day in ["1-Jun-04", "2-Jun-04", "3-Jun-04", "4-Jun-04", "5-Jun-04", "6-Jun-04", "7-Jun-04", "8-Jun-04", "9-Jun-04", "10-Jun-04", "11-Jun-04", "12-Jun-04", "13-Jun-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-06-page-1-table-1.csv'})

for day in ["1-Jul-15", "2-Jul-15", "3-Jul-15", "4-Jul-15", "5-Jul-15", "6-Jul-15", "7-Jul-15", "8-Jul-15", "9-Jul-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-07-page-1-table-1.csv'})

for day in ["12-Jun-14", "13-Jun-14", "14-Jun-14", "15-Jun-14", "16-Jun-14", "17-Jun-14", "18-Jun-14", "19-Jun-14", "20-Jun-14", "21-Jun-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-06-page-2-table-1.csv'})

for day in ["10-Dec-09", "11-Dec-09", "12-Dec-09", "13-Dec-09", "14-Dec-09", "15-Dec-09", "16-Dec-09", "17-Dec-09", "18-Dec-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-12-page-2-table-1.csv'})

for day in ["14-Jul-05", "15-Jul-05", "16-Jul-05", "17-Jul-05", "18-Jul-05", "19-Jul-05", "20-Jul-05", "21-Jul-05", "22-Jul-05", "23-Jul-05", "24-Jul-05", "25-Jul-05", "26-Jul-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-07-page-2-table-1.csv'})

for day in ["1-Jan-13", "2-Jan-13", "3-Jan-13", "4-Jan-13", "5-Jan-13", "6-Jan-13", "7-Jan-13", "8-Jan-13", "9-Jan-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-01-page-1-table-1.csv'})

for day in ["28-Sep-15", "29-Sep-15", "30-Sep-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-09-page-4-table-1.csv'})

for day in ["14-Jan-03", "15-Jan-03", "16-Jan-03", "17-Jan-03", "18-Jan-03", "19-Jan-03", "20-Jan-03", "21-Jan-03", "22-Jan-03", "23-Jan-03", "24-Jan-03", "25-Jan-03", "26-Jan-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-01-page-2-table-1.csv'})

for day in ["28-Jul-09", "29-Jul-09", "30-Jul-09", "31-Jul-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-07-page-4-table-1.csv'})

for day in ["19-Jan-16", "20-Jan-16", "21-Jan-16", "22-Jan-16", "23-Jan-16", "24-Jan-16", "25-Jan-16", "26-Jan-16", "27-Jan-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-01-page-3-table-1.csv'})

for day in ["28-Apr-15", "29-Apr-15", "30-Apr-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-04-page-4-table-1.csv'})

for day in ["28-Oct-08", "29-Oct-08", "30-Oct-08", "31-Oct-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-10-page-4-table-1.csv'})

for day in ["1-Feb-19", "2-Feb-19", "3-Feb-19", "4-Feb-19", "5-Feb-19", "6-Feb-19", "7-Feb-19", "8-Feb-19", "9-Feb-19", "10-Feb-19", "11-Feb-19", "12-Feb-19", "13-Feb-19", "14-Feb-19", "15-Feb-19", "16-Feb-19", "17-Feb-19"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2019-02-page-1-table-1.csv'})

for day in ["1-Mar-08", "2-Mar-08", "3-Mar-08", "4-Mar-08", "5-Mar-08", "6-Mar-08", "7-Mar-08", "8-Mar-08", "9-Mar-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-03-page-1-table-1.csv'})

for day in ["10-Feb-09", "11-Feb-09", "12-Feb-09", "13-Feb-09", "14-Feb-09", "15-Feb-09", "16-Feb-09", "17-Feb-09", "18-Feb-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-02-page-2-table-1.csv'})

for day in ["18-Mar-18", "19-Mar-18", "20-Mar-18", "21-Mar-18", "22-Mar-18", "23-Mar-18", "24-Mar-18", "25-Mar-18", "26-Mar-18", "27-Mar-18", "28-Mar-18", "29-Mar-18", "30-Mar-18", "31-Mar-18"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2018-03-page-2-table-1.csv'})

for day in ["28-May-12", "29-May-12", "30-May-12", "31-May-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-05-page-4-table-1.csv'})

for day in ["28-Dec-13", "29-Dec-13", "30-Dec-13", "31-Dec-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-12-page-4-table-1.csv'})

for day in ["10-Jan-15", "11-Jan-15", "12-Jan-15", "13-Jan-15", "14-Jan-15", "15-Jan-15", "16-Jan-15", "17-Jan-15", "18-Jan-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-01-page-2-table-1.csv'})

for day in ["28-Aug-12", "29-Aug-12", "30-Aug-12", "31-Aug-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-08-page-4-table-1.csv'})

for day in ["1-Jan-05", "2-Jan-05", "3-Jan-05", "4-Jan-05", "5-Jan-05", "6-Jan-05", "7-Jan-05", "8-Jan-05", "9-Jan-05", "10-Jan-05", "11-Jan-05", "12-Jan-05", "13-Jan-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-01-page-1-table-1.csv'})

for day in ["1-Dec-11", "2-Dec-11", "3-Dec-11", "4-Dec-11", "5-Dec-11", "6-Dec-11", "7-Dec-11", "8-Dec-11", "9-Dec-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-12-page-1-table-1.csv'})

for day in ["11-Dec-01", "12-Dec-01", "13-Dec-01", "14-Dec-01", "15-Dec-01", "16-Dec-01", "17-Dec-01", "18-Dec-01", "19-Dec-01", "20-Dec-01"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2001-12-page-2-table-1.csv'})

for day in ["27-Sep-04", "28-Sep-04", "29-Sep-04", "30-Sep-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-09-page-3-table-1.csv'})

for day in ["19-Aug-15", "20-Aug-15", "21-Aug-15", "22-Aug-15", "23-Aug-15", "24-Aug-15", "25-Aug-15", "26-Aug-15", "27-Aug-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-08-page-3-table-1.csv'})

for day in ["1-Aug-10", "2-Aug-10", "3-Aug-10", "4-Aug-10", "5-Aug-10", "6-Aug-10", "7-Aug-10", "8-Aug-10", "9-Aug-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-08-page-1-table-1.csv'})

for day in ["1-Sep-01", "2-Sep-01", "3-Sep-01", "4-Sep-01", "5-Sep-01", "6-Sep-01", "7-Sep-01", "8-Sep-01", "9-Sep-01", "10-Sep-01"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2001-09-page-1-table-1.csv'})

for day in ["28-Jan-07", "29-Jan-07", "30-Jan-07", "31-Jan-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-01-page-4-table-1.csv'})

for day in ["19-Jun-09", "20-Jun-09", "21-Jun-09", "22-Jun-09", "23-Jun-09", "24-Jun-09", "25-Jun-09", "26-Jun-09", "27-Jun-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-06-page-3-table-1.csv'})

for day in ["10-Sep-11", "11-Sep-11", "12-Sep-11", "13-Sep-11", "14-Sep-11", "15-Sep-11", "16-Sep-11", "17-Sep-11", "18-Sep-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-09-page-2-table-1.csv'})

for day in ["19-Dec-14", "20-Dec-14", "21-Dec-14", "22-Dec-14", "23-Dec-14", "24-Dec-14", "25-Dec-14", "26-Dec-14", "27-Dec-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-12-page-3-table-1.csv'})

for day in ["19-Nov-08", "20-Nov-08", "21-Nov-08", "22-Nov-08", "23-Nov-08", "24-Nov-08", "25-Nov-08", "26-Nov-08", "27-Nov-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-11-page-3-table-1.csv'})

for day in ["27-Apr-04", "28-Apr-04", "29-Apr-04", "30-Apr-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-04-page-3-table-1.csv'})

for day in ["19-May-15", "20-May-15", "21-May-15", "22-May-15", "23-May-15", "24-May-15", "25-May-15", "26-May-15", "27-May-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-05-page-3-table-1.csv'})

for day in ["10-Apr-11", "11-Apr-11", "12-Apr-11", "13-Apr-11", "14-Apr-11", "15-Apr-11", "16-Apr-11", "17-Apr-11", "18-Apr-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-04-page-2-table-1.csv'})

for day in ["1-May-10", "2-May-10", "3-May-10", "4-May-10", "5-May-10", "6-May-10", "7-May-10", "8-May-10", "9-May-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-05-page-1-table-1.csv'})

for day in ["1-Apr-17", "2-Apr-17", "3-Apr-17", "4-Apr-17", "5-Apr-17", "6-Apr-17", "7-Apr-17", "8-Apr-17", "9-Apr-17", "10-Apr-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-04-page-1-table-1.csv'})

for day in ["1-May-06", "2-May-06", "3-May-06", "4-May-06", "5-May-06", "6-May-06", "7-May-06", "8-May-06", "9-May-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-05-page-1-table-1.csv'})

for day in ["10-Apr-07", "11-Apr-07", "12-Apr-07", "13-Apr-07", "14-Apr-07", "15-Apr-07", "16-Apr-07", "17-Apr-07", "18-Apr-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-04-page-2-table-1.csv'})

for day in ["10-May-16", "11-May-16", "12-May-16", "13-May-16", "14-May-16", "15-May-16", "16-May-16", "17-May-16", "18-May-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-05-page-2-table-1.csv'})

for day in ["27-May-03", "28-May-03", "29-May-03", "30-May-03", "31-May-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-05-page-3-table-1.csv'})

for day in ["19-Apr-12", "20-Apr-12", "21-Apr-12", "22-Apr-12", "23-Apr-12", "24-Apr-12", "25-Apr-12", "26-Apr-12", "27-Apr-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-04-page-3-table-1.csv'})

for day in ["10-Sep-07", "11-Sep-07", "12-Sep-07", "13-Sep-07", "14-Sep-07", "15-Sep-07", "16-Sep-07", "17-Sep-07", "18-Sep-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-09-page-2-table-1.csv'})

for day in ["11-Aug-16", "12-Aug-16", "13-Aug-16", "14-Aug-16", "15-Aug-16", "16-Aug-16", "17-Aug-16", "18-Aug-16", "19-Aug-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-08-page-2-table-1.csv'})

for day in ["28-Jan-11", "29-Jan-11", "30-Jan-11", "31-Jan-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-01-page-4-table-1.csv'})

for day in ["1-Sep-17", "2-Sep-17", "3-Sep-17", "4-Sep-17", "5-Sep-17", "6-Sep-17", "7-Sep-17", "8-Sep-17", "9-Sep-17", "10-Sep-17", "11-Sep-17", "12-Sep-17", "13-Sep-17", "14-Sep-17", "15-Sep-17", "16-Sep-17", "17-Sep-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-09-page-1-table-1.csv'})

for day in ["1-Aug-06", "2-Aug-06", "3-Aug-06", "4-Aug-06", "5-Aug-06", "6-Aug-06", "7-Aug-06", "8-Aug-06", "9-Aug-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-08-page-1-table-1.csv'})

for day in ["25-Aug-03", "26-Aug-03", "27-Aug-03", "28-Aug-03", "29-Aug-03", "30-Aug-03", "31-Aug-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-08-page-3-table-1.csv'})

for day in ["18-Dec-17", "19-Dec-17", "20-Dec-17", "21-Dec-17", "22-Dec-17", "23-Dec-17", "24-Dec-17", "25-Dec-17", "26-Dec-17", "27-Dec-17", "28-Dec-17", "29-Dec-17", "30-Dec-17", "31-Dec-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-12-page-2-table-1.csv'})

for day in ["19-Sep-12", "20-Sep-12", "21-Sep-12", "22-Sep-12", "23-Sep-12", "24-Sep-12", "25-Sep-12", "26-Sep-12", "27-Sep-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-09-page-3-table-1.csv'})

for day in ["1-Dec-07", "2-Dec-07", "3-Dec-07", "4-Dec-07", "5-Dec-07", "6-Dec-07", "7-Dec-07", "8-Dec-07", "9-Dec-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-12-page-1-table-1.csv'})

for day in ["19-Jan-08", "20-Jan-08", "21-Jan-08", "22-Jan-08", "23-Jan-08", "24-Jan-08", "25-Jan-08", "26-Jan-08", "27-Jan-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-01-page-3-table-1.csv'})

for day in ["28-Jun-06", "29-Jun-06", "30-Jun-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-06-page-4-table-1.csv'})

for day in ["28-Nov-07", "29-Nov-07", "30-Nov-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-11-page-4-table-1.csv'})

for day in ["24-Oct-16", "25-Oct-16", "26-Oct-16", "27-Oct-16", "28-Oct-16", "29-Oct-16", "30-Oct-16", "31-Oct-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-10-page-4-table-1.csv'})

for day in ["19-Feb-14", "20-Feb-14", "21-Feb-14", "22-Feb-14", "23-Feb-14", "24-Feb-14", "25-Feb-14", "26-Feb-14", "27-Feb-14", "28-Feb-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-02-page-3-table-1.csv'})

for day in ["27-Mar-05", "28-Mar-05", "29-Mar-05", "30-Mar-05", "31-Mar-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-03-page-3-table-1.csv'})

for day in ["1-Feb-11", "2-Feb-11", "3-Feb-11", "4-Feb-11", "5-Feb-11", "6-Feb-11", "7-Feb-11", "8-Feb-11", "9-Feb-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-02-page-1-table-1.csv'})

for day in ["10-Mar-10", "11-Mar-10", "12-Mar-10", "13-Mar-10", "14-Mar-10", "15-Mar-10", "16-Mar-10", "17-Mar-10", "18-Mar-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-03-page-2-table-1.csv'})

for day in ["11-Feb-17", "12-Feb-17", "13-Feb-17", "14-Feb-17", "15-Feb-17", "16-Feb-17", "17-Feb-17", "18-Feb-17", "19-Feb-17", "20-Feb-17", "21-Feb-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-02-page-2-table-1.csv'})

for day in ["10-Mar-06", "11-Mar-06", "12-Mar-06", "13-Mar-06", "14-Mar-06", "15-Mar-06", "16-Mar-06", "17-Mar-06", "18-Mar-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-03-page-2-table-1.csv'})

for day in ["1-Feb-07", "2-Feb-07", "3-Feb-07", "4-Feb-07", "5-Feb-07", "6-Feb-07", "7-Feb-07", "8-Feb-07", "9-Feb-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-02-page-1-table-1.csv'})

for day in ["1-Mar-16", "2-Mar-16", "3-Mar-16", "4-Mar-16", "5-Mar-16", "6-Mar-16", "7-Mar-16", "8-Mar-16", "9-Mar-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-03-page-1-table-1.csv'})

for day in ["19-Mar-13", "20-Mar-13", "21-Mar-13", "22-Mar-13", "23-Mar-13", "24-Mar-13", "25-Mar-13", "26-Mar-13", "27-Mar-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-03-page-3-table-1.csv'})

for day in ["25-Feb-02", "26-Feb-02", "27-Feb-02", "28-Feb-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-02-page-3-table-1.csv'})

for day in ["28-Nov-11", "29-Nov-11", "30-Nov-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-11-page-4-table-1.csv'})

for day in ["28-Jun-10", "29-Jun-10", "30-Jun-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-06-page-4-table-1.csv'})

for day in ["27-Mar-03", "28-Mar-03", "29-Mar-03", "30-Mar-03", "31-Mar-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-03-page-3-table-1.csv'})

for day in ["19-Feb-12", "20-Feb-12", "21-Feb-12", "22-Feb-12", "23-Feb-12", "24-Feb-12", "25-Feb-12", "26-Feb-12", "27-Feb-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-02-page-3-table-1.csv'})

for day in ["28-Oct-10", "29-Oct-10", "30-Oct-10", "31-Oct-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-10-page-4-table-1.csv'})

for day in ["10-Feb-07", "11-Feb-07", "12-Feb-07", "13-Feb-07", "14-Feb-07", "15-Feb-07", "16-Feb-07", "17-Feb-07", "18-Feb-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-02-page-2-table-1.csv'})

for day in ["10-Mar-16", "11-Mar-16", "12-Mar-16", "13-Mar-16", "14-Mar-16", "15-Mar-16", "16-Mar-16", "17-Mar-16", "18-Mar-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-03-page-2-table-1.csv'})

for day in ["1-Feb-17", "2-Feb-17", "3-Feb-17", "4-Feb-17", "5-Feb-17", "6-Feb-17", "7-Feb-17", "8-Feb-17", "9-Feb-17", "10-Feb-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-02-page-1-table-1.csv'})

for day in ["1-Mar-06", "2-Mar-06", "3-Mar-06", "4-Mar-06", "5-Mar-06", "6-Mar-06", "7-Mar-06", "8-Mar-06", "9-Mar-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-03-page-1-table-1.csv'})

for day in ["28-Jul-11", "29-Jul-11", "30-Jul-11", "31-Jul-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-07-page-4-table-1.csv'})

for day in ["28-Jun-16", "29-Jun-16", "30-Jun-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-06-page-4-table-1.csv'})

for day in ["28-Jul-07", "29-Jul-07", "30-Jul-07", "31-Jul-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-07-page-4-table-1.csv'})

for day in ["1-Mar-10", "2-Mar-10", "3-Mar-10", "4-Mar-10", "5-Mar-10", "6-Mar-10", "7-Mar-10", "8-Mar-10", "9-Mar-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-03-page-1-table-1.csv'})

for day in ["10-Feb-11", "11-Feb-11", "12-Feb-11", "13-Feb-11", "14-Feb-11", "15-Feb-11", "16-Feb-11", "17-Feb-11", "18-Feb-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-02-page-2-table-1.csv'})

for day in ["28-Oct-06", "29-Oct-06", "30-Oct-06", "31-Oct-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-10-page-4-table-1.csv'})

for day in ["25-Feb-04", "26-Feb-04", "27-Feb-04", "28-Feb-04", "29-Feb-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-02-page-3-table-1.csv'})

for day in ["19-Mar-15", "20-Mar-15", "21-Mar-15", "22-Mar-15", "23-Mar-15", "24-Mar-15", "25-Mar-15", "26-Mar-15", "27-Mar-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-03-page-3-table-1.csv'})

for day in ["19-May-13", "20-May-13", "21-May-13", "22-May-13", "23-May-13", "24-May-13", "25-May-13", "26-May-13", "27-May-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-05-page-3-table-1.csv'})

for day in ["21-Apr-02", "22-Apr-02", "23-Apr-02", "24-Apr-02", "25-Apr-02", "26-Apr-02", "27-Apr-02", "28-Apr-02", "29-Apr-02", "30-Apr-02", "1-May-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-04-page-3-table-1.csv'})

for day in ["1-Apr-07", "2-Apr-07", "3-Apr-07", "4-Apr-07", "5-Apr-07", "6-Apr-07", "7-Apr-07", "8-Apr-07", "9-Apr-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-04-page-1-table-1.csv'})

for day in ["1-May-16", "2-May-16", "3-May-16", "4-May-16", "5-May-16", "6-May-16", "7-May-16", "8-May-16", "9-May-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-05-page-1-table-1.csv'})

for day in ["11-Apr-17", "12-Apr-17", "13-Apr-17", "14-Apr-17", "15-Apr-17", "16-Apr-17", "17-Apr-17", "18-Apr-17", "19-Apr-17", "20-Apr-17", "21-Apr-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-04-page-2-table-1.csv'})

for day in ["10-May-06", "11-May-06", "12-May-06", "13-May-06", "14-May-06", "15-May-06", "16-May-06", "17-May-06", "18-May-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-05-page-2-table-1.csv'})

for day in ["19-Aug-13", "20-Aug-13", "21-Aug-13", "22-Aug-13", "23-Aug-13", "24-Aug-13", "25-Aug-13", "26-Aug-13", "27-Aug-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-08-page-3-table-1.csv'})

for day in ["21-Sep-02", "22-Sep-02", "23-Sep-02", "24-Sep-02", "25-Sep-02", "26-Sep-02", "27-Sep-02", "28-Sep-02", "29-Sep-02", "30-Sep-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-09-page-3-table-1.csv'})

for day in ["10-Dec-07", "11-Dec-07", "12-Dec-07", "13-Dec-07", "14-Dec-07", "15-Dec-07", "16-Dec-07", "17-Dec-07", "18-Dec-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-12-page-2-table-1.csv'})

for day in ["1-Dec-17", "2-Dec-17", "3-Dec-17", "4-Dec-17", "5-Dec-17", "6-Dec-17", "7-Dec-17", "8-Dec-17", "9-Dec-17", "10-Dec-17", "11-Dec-17", "12-Dec-17", "13-Dec-17", "14-Dec-17", "15-Dec-17", "16-Dec-17", "17-Dec-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-12-page-1-table-1.csv'})

for day in ["19-Dec-12", "20-Dec-12", "21-Dec-12", "22-Dec-12", "23-Dec-12", "24-Dec-12", "25-Dec-12", "26-Dec-12", "27-Dec-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-12-page-3-table-1.csv'})

for day in ["18-Sep-17", "19-Sep-17", "20-Sep-17", "21-Sep-17", "22-Sep-17", "23-Sep-17", "24-Sep-17", "25-Sep-17", "26-Sep-17", "27-Sep-17", "28-Sep-17", "29-Sep-17", "30-Sep-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-09-page-2-table-1.csv'})

for day in ["10-Aug-06", "11-Aug-06", "12-Aug-06", "13-Aug-06", "14-Aug-06", "15-Aug-06", "16-Aug-06", "17-Aug-06", "18-Aug-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-08-page-2-table-1.csv'})

for day in ["1-Sep-07", "2-Sep-07", "3-Sep-07", "4-Sep-07", "5-Sep-07", "6-Sep-07", "7-Sep-07", "8-Sep-07", "9-Sep-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-09-page-1-table-1.csv'})

for day in ["1-Aug-16", "2-Aug-16", "3-Aug-16", "4-Aug-16", "5-Aug-16", "6-Aug-16", "7-Aug-16", "8-Aug-16", "9-Aug-16", "10-Aug-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-08-page-1-table-1.csv'})

for day in ["1-Sep-11", "2-Sep-11", "3-Sep-11", "4-Sep-11", "5-Sep-11", "6-Sep-11", "7-Sep-11", "8-Sep-11", "9-Sep-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-09-page-1-table-1.csv'})

for day in ["10-Aug-10", "11-Aug-10", "12-Aug-10", "13-Aug-10", "14-Aug-10", "15-Aug-10", "16-Aug-10", "17-Aug-10", "18-Aug-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-08-page-2-table-1.csv'})

for day in ["27-Dec-04", "28-Dec-04", "29-Dec-04", "30-Dec-04", "31-Dec-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-12-page-3-table-1.csv'})

for day in ["11-Sep-01", "12-Sep-01", "13-Sep-01", "14-Sep-01", "15-Sep-01", "16-Sep-01", "17-Sep-01", "18-Sep-01", "19-Sep-01", "20-Sep-01"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2001-09-page-2-table-1.csv'})

for day in ["19-Jul-08", "20-Jul-08", "21-Jul-08", "22-Jul-08", "23-Jul-08", "24-Jul-08", "25-Jul-08", "26-Jul-08", "27-Jul-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-07-page-3-table-1.csv'})

for day in ["1-Dec-01", "2-Dec-01", "3-Dec-01", "4-Dec-01", "5-Dec-01", "6-Dec-01", "7-Dec-01", "8-Dec-01", "9-Dec-01", "10-Dec-01"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2001-12-page-1-table-1.csv'})

for day in ["22-Sep-14", "23-Sep-14", "24-Sep-14", "25-Sep-14", "26-Sep-14", "27-Sep-14", "28-Sep-14", "29-Sep-14", "30-Sep-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-09-page-3-table-1.csv'})

for day in ["10-Dec-11", "11-Dec-11", "12-Dec-11", "13-Dec-11", "14-Dec-11", "15-Dec-11", "16-Dec-11", "17-Dec-11", "18-Dec-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-12-page-2-table-1.csv'})

for day in ["27-Aug-05", "28-Aug-05", "29-Aug-05", "30-Aug-05", "31-Aug-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-08-page-3-table-1.csv'})

for day in ["10-May-10", "11-May-10", "12-May-10", "13-May-10", "14-May-10", "15-May-10", "16-May-10", "17-May-10", "18-May-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-05-page-2-table-1.csv'})

for day in ["1-Apr-11", "2-Apr-11", "3-Apr-11", "4-Apr-11", "5-Apr-11", "6-Apr-11", "7-Apr-11", "8-Apr-11", "9-Apr-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-04-page-1-table-1.csv'})

for day in ["22-Apr-14", "23-Apr-14", "24-Apr-14", "25-Apr-14", "26-Apr-14", "27-Apr-14", "28-Apr-14", "29-Apr-14", "30-Apr-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-04-page-3-table-1.csv'})

for day in ["27-May-05", "28-May-05", "29-May-05", "30-May-05", "31-May-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-05-page-3-table-1.csv'})

for day in ["19-Oct-09", "20-Oct-09", "21-Oct-09", "22-Oct-09", "23-Oct-09", "24-Oct-09", "25-Oct-09", "26-Oct-09", "27-Oct-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-10-page-3-table-1.csv'})

for day in ["28-Apr-13", "29-Apr-13", "30-Apr-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-04-page-4-table-1.csv'})

for day in ["1-Feb-09", "2-Feb-09", "3-Feb-09", "4-Feb-09", "5-Feb-09", "6-Feb-09", "7-Feb-09", "8-Feb-09", "9-Feb-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-02-page-1-table-1.csv'})

for day in ["1-Mar-18", "2-Mar-18", "3-Mar-18", "4-Mar-18", "5-Mar-18", "6-Mar-18", "7-Mar-18", "8-Mar-18", "9-Mar-18", "10-Mar-18", "11-Mar-18", "12-Mar-18", "13-Mar-18", "14-Mar-18", "15-Mar-18", "16-Mar-18", "17-Mar-18"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2018-03-page-1-table-1.csv'})

for day in ["18-Feb-19", "19-Feb-19", "20-Feb-19", "21-Feb-19", "22-Feb-19", "23-Feb-19", "24-Feb-19", "25-Feb-19", "26-Feb-19", "27-Feb-19", "28-Feb-19"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2019-02-page-2-table-1.csv'})

for day in ["10-Mar-08", "11-Mar-08", "12-Mar-08", "13-Mar-08", "14-Mar-08", "15-Mar-08", "16-Mar-08", "17-Mar-08", "18-Mar-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-03-page-2-table-1.csv'})

for day in ["14-Jan-05", "15-Jan-05", "16-Jan-05", "17-Jan-05", "18-Jan-05", "19-Jan-05", "20-Jan-05", "21-Jan-05", "22-Jan-05", "23-Jan-05", "24-Jan-05", "25-Jan-05", "26-Jan-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-01-page-2-table-1.csv'})

for day in ["1-Jan-15", "2-Jan-15", "3-Jan-15", "4-Jan-15", "5-Jan-15", "6-Jan-15", "7-Jan-15", "8-Jan-15", "9-Jan-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-01-page-1-table-1.csv'})

for day in ["28-Sep-13", "29-Sep-13", "30-Sep-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-09-page-4-table-1.csv'})

for day in ['19-Jan-10', '20-Jan-10', '21-Jan-10', '22-Jan-10', '23-Jan-10', '24-Jan-10', '25-Jan-10', '26-Jan-10', '27-Jan-10']:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-01-page-3-table-1.csv'})

for day in ["28-Jun-08", "29-Jun-08", "30-Jun-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-06-page-4-table-1.csv'})

for day in ["28-Dec-15", "29-Dec-15", "30-Dec-15", "31-Dec-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-12-page-4-table-1.csv'})

for day in ["19-Jan-06", "20-Jan-06", "21-Jan-06", "22-Jan-06", "23-Jan-06", "24-Jan-06", "25-Jan-06", "26-Jan-06", "27-Jan-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-01-page-3-table-1.csv'})

for day in ["1-Jan-03", "2-Jan-03", "3-Jan-03", "4-Jan-03", "5-Jan-03", "6-Jan-03", "7-Jan-03", "8-Jan-03", "9-Jan-03", "10-Jan-03", "11-Jan-03", "12-Jan-03", "13-Jan-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-01-page-1-table-1.csv'})

for day in ["10-Jan-13", "11-Jan-13", "12-Jan-13", "13-Jan-13", "14-Jan-13", "15-Jan-13", "16-Jan-13", "17-Jan-13", "18-Jan-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-01-page-2-table-1.csv'})

for day in ["28-Nov-09", "29-Nov-09", "30-Nov-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-11-page-4-table-1.csv'})

for day in ["21-Oct-01", "22-Oct-01", "23-Oct-01", "24-Oct-01", "25-Oct-01", "26-Oct-01", "27-Oct-01", "28-Oct-01", "29-Oct-01", "30-Oct-01", "31-Oct-01"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2001-10-page-3-table-1.csv'})

for day in ["19-Nov-10", "20-Nov-10", "21-Nov-10", "22-Nov-10", "23-Nov-10", "24-Nov-10", "25-Nov-10", "26-Nov-10", "27-Nov-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-11-page-3-table-1.csv'})

for day in ["28-Mar-12", "29-Mar-12", "30-Mar-12", "31-Mar-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-03-page-4-table-1.csv'})

for day in ["14-Nov-05", "15-Nov-05", "16-Nov-05", "17-Nov-05", "18-Nov-05", "19-Nov-05", "20-Nov-05", "21-Nov-05", "22-Nov-05", "23-Nov-05", "24-Nov-05", "25-Nov-05", "26-Nov-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-11-page-2-table-1.csv'})

for day in ["10-Apr-09", "11-Apr-09", "12-Apr-09", "13-Apr-09", "14-Apr-09", "15-Apr-09", "16-Apr-09", "17-Apr-09", "18-Apr-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-04-page-2-table-1.csv'})

for day in ["10-Oct-14", "11-Oct-14", "12-Oct-14", "13-Oct-14", "14-Oct-14", "15-Oct-14", "16-Oct-14", "17-Oct-14", "18-Oct-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-10-page-2-table-1.csv'})

for day in ["18-May-18", "19-May-18", "20-May-18", "21-May-18", "22-May-18", "23-May-18", "24-May-18", "25-May-18", "26-May-18", "27-May-18", "28-May-18", "29-May-18", "30-May-18", "31-May-18"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2018-05-page-2-table-1.csv'})

for day in ["1-Nov-15", "2-Nov-15", "3-Nov-15", "4-Nov-15", "5-Nov-15", "6-Nov-15", "7-Nov-15", "8-Nov-15", "9-Nov-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-11-page-1-table-1.csv'})

for day in ["1-Apr-19", "2-Apr-19", "3-Apr-19", "4-Apr-19", "5-Apr-19", "6-Apr-19", "7-Apr-19", "8-Apr-19", "9-Apr-19", "10-Apr-19", "11-Apr-19", "12-Apr-19", "13-Apr-19", "14-Apr-19", "15-Apr-19", "16-Apr-19", "17-Apr-19"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2019-04-page-1-table-1.csv'})

for day in ["1-Oct-04", "2-Oct-04", "3-Oct-04", "4-Oct-04", "5-Oct-04", "6-Oct-04", "7-Oct-04", "8-Oct-04", "9-Oct-04", "10-Oct-04", "11-Oct-04", "12-Oct-04", "13-Oct-04", "14-Oct-04", "15-Oct-04", "16-Oct-04", "17-Oct-04", "18-Oct-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-10-page-1-table-1.csv'})

for day in ["1-May-08", "2-May-08", "3-May-08", "4-May-08", "5-May-08", "6-May-08", "7-May-08", "8-May-08", "9-May-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-05-page-1-table-1.csv'})

for day in ["1-Jun-14", "2-Jun-14", "3-Jun-14", "4-Jun-14", "5-Jun-14", "6-Jun-14", "7-Jun-14", "8-Jun-14", "9-Jun-14", "10-Jun-14", "11-Jun-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-06-page-1-table-1.csv'})

for day in ["1-Jul-05", "2-Jul-05", "3-Jul-05", "4-Jul-05", "5-Jul-05", "6-Jul-05", "7-Jul-05", "8-Jul-05", "9-Jul-05", "10-Jul-05", "11-Jul-05", "12-Jul-05", "13-Jul-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-07-page-1-table-1.csv'})

for day in ["1-Dec-09", "2-Dec-09", "3-Dec-09", "4-Dec-09", "5-Dec-09", "6-Dec-09", "7-Dec-09", "8-Dec-09", "9-Dec-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-12-page-1-table-1.csv'})

for day in ["14-Jun-04", "15-Jun-04", "16-Jun-04", "17-Jun-04", "18-Jun-04", "19-Jun-04", "20-Jun-04", "21-Jun-04", "22-Jun-04", "23-Jun-04", "24-Jun-04", "25-Jun-04", "26-Jun-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-06-page-2-table-1.csv'})

for day in ["10-Jul-15", "11-Jul-15", "12-Jul-15", "13-Jul-15", "14-Jul-15", "15-Jul-15", "16-Jul-15", "17-Jul-15", "18-Jul-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-07-page-2-table-1.csv'})

for day in ["1-Sep-19", "2-Sep-19", "3-Sep-19", "4-Sep-19", "5-Sep-19", "6-Sep-19", "7-Sep-19", "8-Sep-19", "9-Sep-19", "10-Sep-19", "11-Sep-19", "12-Sep-19", "13-Sep-19", "14-Sep-19", "15-Sep-19", "16-Sep-19", "17-Sep-19"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2019-09-page-1-table-1.csv'})

for day in ["1-Aug-08", "2-Aug-08", "3-Aug-08", "4-Aug-08", "5-Aug-08", "6-Aug-08", "7-Aug-08", "8-Aug-08", "9-Aug-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-08-page-1-table-1.csv'})

for day in ["10-Sep-09", "11-Sep-09", "12-Sep-09", "13-Sep-09", "14-Sep-09", "15-Sep-09", "16-Sep-09", "17-Sep-09", "18-Sep-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-09-page-2-table-1.csv'})

for day in ["18-Aug-18", "19-Aug-18", "20-Aug-18", "21-Aug-18", "22-Aug-18", "23-Aug-18", "24-Aug-18", "25-Aug-18", "26-Aug-18", "27-Aug-18", "28-Aug-18", "29-Aug-18", "30-Aug-18", "31-Aug-18"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2018-08-page-2-table-1.csv'})

for day in ["19-Jun-11", "20-Jun-11", "21-Jun-11", "22-Jun-11", "23-Jun-11", "24-Jun-11", "25-Jun-11", "26-Jun-11", "27-Jun-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-06-page-3-table-1.csv'})

for day in ["19-Jun-07", "20-Jun-07", "21-Jun-07", "22-Jun-07", "23-Jun-07", "24-Jun-07", "25-Jun-07", "26-Jun-07", "27-Jun-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-06-page-3-table-1.csv'})

for day in ["19-Jul-16", "20-Jul-16", "21-Jul-16", "22-Jul-16", "23-Jul-16", "24-Jul-16", "25-Jul-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-07-page-3-table-1.csv'})

for day in ["28-Jan-09", "29-Jan-09", "30-Jan-09", "31-Jan-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-01-page-4-table-1.csv'})

for day in ["14-Jul-03", "15-Jul-03", "16-Jul-03", "17-Jul-03", "18-Jul-03", "19-Jul-03", "20-Jul-03", "21-Jul-03", "22-Jul-03", "23-Jul-03", "24-Jul-03", "25-Jul-03", "26-Jul-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-07-page-2-table-1.csv'})

for day in ["10-Jun-12", "11-Jun-12", "12-Jun-12", "13-Jun-12", "14-Jun-12", "15-Jun-12", "16-Jun-12", "17-Jun-12", "18-Jun-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-06-page-2-table-1.csv'})

for day in ["1-Jul-13", "2-Jul-13", "3-Jul-13", "4-Jul-13", "5-Jul-13", "6-Jul-13", "7-Jul-13", "8-Jul-13", "9-Jul-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-07-page-1-table-1.csv'})

for day in ["1-Jun-02", "2-Jun-02", "3-Jun-02", "4-Jun-02", "5-Jun-02", "6-Jun-02", "7-Jun-02", "8-Jun-02", "9-Jun-02", "10-Jun-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-06-page-1-table-1.csv'})

for day in ["1-Oct-12", "2-Oct-12", "3-Oct-12", "4-Oct-12", "5-Oct-12", "6-Oct-12", "7-Oct-12", "8-Oct-12", "9-Oct-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-10-page-1-table-1.csv'})

for day in ["1-Nov-03", "2-Nov-03", "3-Nov-03", "4-Nov-03", "5-Nov-03", "6-Nov-03", "7-Nov-03", "8-Nov-03", "9-Nov-03", "10-Nov-03", "11-Nov-03", "12-Nov-03", "13-Nov-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-11-page-1-table-1.csv'})

for day in ["11-Oct-02", "12-Oct-02", "13-Oct-02", "14-Oct-02", "15-Oct-02", "16-Oct-02", "17-Oct-02", "18-Oct-02", "19-Oct-02", "20-Oct-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-10-page-2-table-1.csv'})

for day in ["10-Nov-13", "11-Nov-13", "12-Nov-13", "13-Nov-13", "14-Nov-13", "15-Nov-13", "16-Nov-13", "17-Nov-13", "18-Nov-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-11-page-2-table-1.csv'})

for day in ["28-Feb-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-02-page-4-table-1.csv'})

for day in ["19-Nov-06", "20-Nov-06", "21-Nov-06", "22-Nov-06", "23-Nov-06", "24-Nov-06", "25-Nov-06", "26-Nov-06", "27-Nov-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-11-page-3-table-1.csv'})

for day in ["10-Apr-15", "11-Apr-15", "12-Apr-15", "13-Apr-15", "14-Apr-15", "15-Apr-15", "16-Apr-15", "17-Apr-15", "18-Apr-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-04-page-2-table-1.csv'})

for day in ["14-May-04", "15-May-04", "16-May-04", "17-May-04", "18-May-04", "19-May-04", "20-May-04", "21-May-04", "22-May-04", "23-May-04", "24-May-04", "25-May-04", "26-May-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-05-page-2-table-1.csv'})

for day in ["10-Oct-08", "11-Oct-08", "12-Oct-08", "13-Oct-08", "14-Oct-08", "15-Oct-08", "16-Oct-08", "17-Oct-08", "18-Oct-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-10-page-2-table-1.csv'})

for day in ["1-Apr-05", "2-Apr-05", "3-Apr-05", "4-Apr-05", "5-Apr-05", "6-Apr-05", "7-Apr-05", "8-Apr-05", "9-Apr-05", "10-Apr-05", "11-Apr-05", "12-Apr-05", "13-Apr-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-04-page-1-table-1.csv'})

for day in ["1-Nov-09", "2-Nov-09", "3-Nov-09", "4-Nov-09", "5-Nov-09", "6-Nov-09", "7-Nov-09", "8-Nov-09", "9-Nov-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-11-page-1-table-1.csv'})

for day in ["1-May-14", "2-May-14", "3-May-14", "4-May-14", "5-May-14", "6-May-14", "7-May-14", "8-May-14", "9-May-14", "10-May-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-05-page-1-table-1.csv'})

for day in ["1-Oct-18", "2-Oct-18", "3-Oct-18", "4-Oct-18", "5-Oct-18", "6-Oct-18", "7-Oct-18", "8-Oct-18", "9-Oct-18", "10-Oct-18", "11-Oct-18", "12-Oct-18", "13-Oct-18", "14-Oct-18", "15-Oct-18", "16-Oct-18", "17-Oct-18"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2018-10-page-1-table-1.csv'})

for day in ["19-May-11", "20-May-11", "21-May-11", "22-May-11", "23-May-11", "24-May-11", "25-May-11", "26-May-11", "27-May-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-05-page-3-table-1.csv'})

for day in ["1-Sep-05", "2-Sep-05", "3-Sep-05", "4-Sep-05", "5-Sep-05", "6-Sep-05", "7-Sep-05", "8-Sep-05", "9-Sep-05", "10-Sep-05", "11-Sep-05", "12-Sep-05", "13-Sep-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-09-page-1-table-1.csv'})

for day in ["1-Aug-14", "2-Aug-14", "3-Aug-14", "4-Aug-14", "5-Aug-14", "6-Aug-14", "7-Aug-14", "8-Aug-14", "9-Aug-14", "10-Aug-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-08-page-1-table-1.csv'})

for day in ["10-Sep-15", "11-Sep-15", "12-Sep-15", "13-Sep-15", "14-Sep-15", "15-Sep-15", "16-Sep-15", "17-Sep-15", "18-Sep-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-09-page-2-table-1.csv'})

for day in ["19-Dec-10", "20-Dec-10", "21-Dec-10", "22-Dec-10", "23-Dec-10", "24-Dec-10", "25-Dec-10", "26-Dec-10", "27-Dec-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-12-page-3-table-1.csv'})

for day in ["14-Aug-04", "15-Aug-04", "16-Aug-04", "17-Aug-04", "18-Aug-04", "19-Aug-04", "20-Aug-04", "21-Aug-04", "22-Aug-04", "23-Aug-04", "24-Aug-04", "25-Aug-04", "26-Aug-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-08-page-2-table-1.csv'})

for day in ["1-Jun-08", "2-Jun-08", "3-Jun-08", "4-Jun-08", "5-Jun-08", "6-Jun-08", "7-Jun-08", "8-Jun-08", "9-Jun-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-06-page-1-table-1.csv'})

for day in ["1-Dec-15", "2-Dec-15", "3-Dec-15", "4-Dec-15", "5-Dec-15", "6-Dec-15", "7-Dec-15", "8-Dec-15", "9-Dec-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-12-page-1-table-1.csv'})

for day in ["1-Jul-19", "2-Jul-19", "3-Jul-19", "4-Jul-19", "5-Jul-19", "6-Jul-19", "7-Jul-19", "8-Jul-19", "9-Jul-19", "10-Jul-19", "11-Jul-19", "12-Jul-19", "13-Jul-19", "14-Jul-19", "15-Jul-19", "16-Jul-19", "17-Jul-19"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2019-07-page-1-table-1.csv'})

for day in ["18-Jun-18", "19-Jun-18", "20-Jun-18", "21-Jun-18", "22-Jun-18", "23-Jun-18", "24-Jun-18", "25-Jun-18", "26-Jun-18", "27-Jun-18", "28-Jun-18", "29-Jun-18", "30-Jun-18"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2018-06-page-2-table-1.csv'})

for day in ["19-Aug-11", "20-Aug-11", "21-Aug-11", "22-Aug-11", "23-Aug-11", "24-Aug-11", "25-Aug-11", "26-Aug-11", "27-Aug-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-08-page-3-table-1.csv'})

for day in ["14-Dec-05", "15-Dec-05", "16-Dec-05", "17-Dec-05", "18-Dec-05", "19-Dec-05", "20-Dec-05", "21-Dec-05", "22-Dec-05", "23-Dec-05", "24-Dec-05", "25-Dec-05", "26-Dec-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-12-page-2-table-1.csv'})

for day in ["10-Jul-09", "11-Jul-09", "12-Jul-09", "13-Jul-09", "14-Jul-09", "15-Jul-09", "16-Jul-09", "17-Jul-09", "18-Jul-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-07-page-2-table-1.csv'})

for day in ["10-Dec-13", "11-Dec-13", "12-Dec-13", "13-Dec-13", "14-Dec-13", "15-Dec-13", "16-Dec-13", "17-Dec-13", "18-Dec-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-12-page-2-table-1.csv'})

for day in ["20-Sep-16", "21-Sep-16", "22-Sep-16", "23-Sep-16", "24-Sep-16", "25-Sep-16", "26-Sep-16", "27-Sep-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-09-page-3-table-1.csv'})

for day in ["19-Aug-07", "20-Aug-07", "21-Aug-07", "22-Aug-07", "23-Aug-07", "24-Aug-07", "25-Aug-07", "26-Aug-07", "27-Aug-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-08-page-3-table-1.csv'})

for day in ["1-Dec-03", "2-Dec-03", "3-Dec-03", "4-Dec-03", "5-Dec-03", "6-Dec-03", "7-Dec-03", "8-Dec-03", "9-Dec-03", "10-Dec-03", "11-Dec-03", "12-Dec-03", "13-Dec-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-12-page-1-table-1.csv'})

for day in ["10-Aug-12", "11-Aug-12", "12-Aug-12", "13-Aug-12", "14-Aug-12", "15-Aug-12", "16-Aug-12", "17-Aug-12", "18-Aug-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-08-page-2-table-1.csv'})

for day in ["14-Sep-03", "15-Sep-03", "16-Sep-03", "17-Sep-03", "18-Sep-03", "19-Sep-03", "20-Sep-03", "21-Sep-03", "22-Sep-03", "23-Sep-03", "24-Sep-03", "25-Sep-03", "26-Sep-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-09-page-2-table-1.csv'})

for day in ["19-Dec-06", "20-Dec-06", "21-Dec-06", "22-Dec-06", "23-Dec-06", "24-Dec-06", "25-Dec-06", "26-Dec-06", "27-Dec-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-12-page-3-table-1.csv'})

for day in ["1-Aug-02", "2-Aug-02", "3-Aug-02", "4-Aug-02", "5-Aug-02", "6-Aug-02", "7-Aug-02", "8-Aug-02", "9-Aug-02", "10-Aug-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-08-page-1-table-1.csv'})

for day in ["28-Jan-15", "29-Jan-15", "30-Jan-15", "31-Jan-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-01-page-4-table-1.csv'})

for day in ["1-Sep-13", "2-Sep-13", "3-Sep-13", "4-Sep-13", "5-Sep-13", "6-Sep-13", "7-Sep-13", "8-Sep-13", "9-Sep-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-09-page-1-table-1.csv'})

for day in ["28-Feb-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-02-page-4-table-1.csv'})

for day in ["19-Apr-16", "20-Apr-16", "21-Apr-16", "22-Apr-16", "23-Apr-16", "24-Apr-16", "25-Apr-16", "26-Apr-16", "27-Apr-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-04-page-3-table-1.csv'})

for day in ["19-May-07", "20-May-07", "21-May-07", "22-May-07", "23-May-07", "24-May-07", "25-May-07", "26-May-07", "27-May-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-05-page-3-table-1.csv'})

for day in ["1-May-02", "2-May-02", "3-May-02", "4-May-02", "5-May-02", "6-May-02", "7-May-02", "8-May-02", "9-May-02", "10-May-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-05-page-1-table-1.csv'})

for day in ["1-Apr-13", "2-Apr-13", "3-Apr-13", "4-Apr-13", "5-Apr-13", "6-Apr-13", "7-Apr-13", "8-Apr-13", "9-Apr-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-04-page-1-table-1.csv'})

for day in ["10-May-12", "11-May-12", "12-May-12", "13-May-12", "14-May-12", "15-May-12", "16-May-12", "17-May-12", "18-May-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-05-page-2-table-1.csv'})

for day in ["13-Apr-03", "14-Apr-03", "15-Apr-03", "16-Apr-03", "17-Apr-03", "18-Apr-03", "19-Apr-03", "20-Apr-03", "21-Apr-03", "22-Apr-03", "23-Apr-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-04-page-2-table-1.csv'})

for day in ["1-Feb-15", "2-Feb-15", "3-Feb-15", "4-Feb-15", "5-Feb-15", "6-Feb-15", "7-Feb-15", "8-Feb-15", "9-Feb-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-02-page-1-table-1.csv'})

for day in ["1-Mar-04", "2-Mar-04", "3-Mar-04", "4-Mar-04", "5-Mar-04", "6-Mar-04", "7-Mar-04", "8-Mar-04", "9-Mar-04", "10-Mar-04", "11-Mar-04", "12-Mar-04", "13-Mar-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-03-page-1-table-1.csv'})

for day in ["13-Feb-05", "14-Feb-05", "15-Feb-05", "16-Feb-05", "17-Feb-05", "18-Feb-05", "19-Feb-05", "20-Feb-05", "21-Feb-05", "22-Feb-05", "23-Feb-05", "24-Feb-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-02-page-2-table-1.csv'})

for day in ["11-Mar-14", "12-Mar-14", "13-Mar-14", "14-Mar-14", "15-Mar-14", "16-Mar-14", "17-Mar-14", "18-Mar-14", "19-Mar-14", "20-Mar-14", "21-Mar-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-03-page-2-table-1.csv'})

for day in ["28-Oct-12", "29-Oct-12", "30-Oct-12", "31-Oct-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-10-page-4-table-1.csv'})

for day in ["19-Feb-10", "20-Feb-10", "21-Feb-10", "22-Feb-10", "23-Feb-10", "24-Feb-10", "25-Feb-10", "26-Feb-10", "27-Feb-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-02-page-3-table-1.csv'})

for day in ["28-Jul-13", "29-Jul-13", "30-Jul-13", "31-Jul-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-07-page-4-table-1.csv'})

for day in ["18-Jan-19", "19-Jan-19", "20-Jan-19", "21-Jan-19", "22-Jan-19", "23-Jan-19", "24-Jan-19", "25-Jan-19", "26-Jan-19", "27-Jan-19", "28-Jan-19", "29-Jan-19", "30-Jan-19", "31-Jan-19"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2019-01-page-2-table-1.csv'})

for day in ["1-Jan-09", "2-Jan-09", "3-Jan-09", "4-Jan-09", "5-Jan-09", "6-Jan-09", "7-Jan-09", "8-Jan-09", "9-Jan-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-01-page-1-table-1.csv'})

for day in ["28-Aug-08", "29-Aug-08", "30-Aug-08", "31-Aug-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-08-page-4-table-1.csv'})

for day in ["28-Dec-09", "29-Dec-09", "30-Dec-09", "31-Dec-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-12-page-4-table-1.csv'})

for day in ["19-Feb-06", "20-Feb-06", "21-Feb-06", "22-Feb-06", "23-Feb-06", "24-Feb-06", "25-Feb-06", "26-Feb-06", "27-Feb-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-02-page-3-table-1.csv'})

for day in ["22-Mar-17", "23-Mar-17", "24-Mar-17", "25-Mar-17", "26-Mar-17", "27-Mar-17", "28-Mar-17", "29-Mar-17", "30-Mar-17", "31-Mar-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-03-page-3-table-1.csv'})

for day in ["28-Nov-15", "29-Nov-15", "30-Nov-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-11-page-4-table-1.csv'})

for day in ["28-May-08", "29-May-08", "30-May-08", "31-May-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-05-page-4-table-1.csv'})

for day in ["11-Mar-02", "12-Mar-02", "13-Mar-02", "14-Mar-02", "15-Mar-02", "16-Mar-02", "17-Mar-02", "18-Mar-02", "19-Mar-02", "20-Mar-02"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2002-03-page-2-table-1.csv'})

for day in ["10-Feb-13", "11-Feb-13", "12-Feb-13", "13-Feb-13", "14-Feb-13", "15-Feb-13", "16-Feb-13", "17-Feb-13", "18-Feb-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-02-page-2-table-1.csv'})

for day in ["1-Mar-12", "2-Mar-12", "3-Mar-12", "4-Mar-12", "5-Mar-12", "6-Mar-12", "7-Mar-12", "8-Mar-12", "9-Mar-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-03-page-1-table-1.csv'})

for day in ["1-Feb-03", "2-Feb-03", "3-Feb-03", "4-Feb-03", "5-Feb-03", "6-Feb-03", "7-Feb-03", "8-Feb-03", "9-Feb-03", "10-Feb-03", "11-Feb-03", "12-Feb-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-02-page-1-table-1.csv'})

for day in ["1-Nov-17", "2-Nov-17", "3-Nov-17", "4-Nov-17", "5-Nov-17", "6-Nov-17", "7-Nov-17", "8-Nov-17", "9-Nov-17", "10-Nov-17", "11-Nov-17", "12-Nov-17", "13-Nov-17", "14-Nov-17", "15-Nov-17", "16-Nov-17", "17-Nov-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-11-page-1-table-1.csv'})

for day in ["1-Oct-06", "2-Oct-06", "3-Oct-06", "4-Oct-06", "5-Oct-06", "6-Oct-06", "7-Oct-06", "8-Oct-06", "9-Oct-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-10-page-1-table-1.csv'})

for day in ["10-Nov-07", "11-Nov-07", "12-Nov-07", "13-Nov-07", "14-Nov-07", "15-Nov-07", "16-Nov-07", "17-Nov-07", "18-Nov-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-11-page-2-table-1.csv'})

for day in ["11-Oct-16", "12-Oct-16", "13-Oct-16", "14-Oct-16", "15-Oct-16", "16-Oct-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-10-page-2-table-1.csv'})

for day in ['28-Mar-10', '29-Mar-10', '30-Mar-10', '31-Mar-10']:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-03-page-4-table-1.csv'})

for day in ["27-Oct-03", "28-Oct-03", "29-Oct-03", "30-Oct-03", "31-Oct-03"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2003-10-page-3-table-1.csv'})

for day in ["19-Nov-12", "20-Nov-12", "21-Nov-12", "22-Nov-12", "23-Nov-12", "24-Nov-12", "25-Nov-12", "26-Nov-12", "27-Nov-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-11-page-3-table-1.csv'})

for day in ["19-Jun-13", "20-Jun-13", "21-Jun-13", "22-Jun-13", "23-Jun-13", "24-Jun-13", "25-Jun-13", "26-Jun-13", "27-Jun-13"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2013-06-page-3-table-1.csv'})

for day in ["10-Jun-06", "11-Jun-06", "12-Jun-06", "13-Jun-06", "14-Jun-06", "15-Jun-06", "16-Jun-06", "17-Jun-06", "18-Jun-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-06-page-2-table-1.csv'})

for day in ["18-Jul-17", "19-Jul-17", "20-Jul-17", "21-Jul-17", "22-Jul-17", "23-Jul-17", "24-Jul-17", "25-Jul-17", "26-Jul-17", "27-Jul-17", "28-Jul-17", "29-Jul-17", "30-Jul-17", "31-Jul-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-07-page-2-table-1.csv'})

for day in ["1-Jun-16", "2-Jun-16", "3-Jun-16", "4-Jun-16", "5-Jun-16", "6-Jun-16", "7-Jun-16", "8-Jun-16", "9-Jun-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-06-page-1-table-1.csv'})

for day in ["1-Jul-07", "2-Jul-07", "3-Jul-07", "4-Jul-07", "5-Jul-07", "6-Jul-07", "7-Jul-07", "8-Jul-07", "9-Jul-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-07-page-1-table-1.csv'})

for day in ["1-Jul-11", "2-Jul-11", "3-Jul-11", "4-Jul-11", "5-Jul-11", "6-Jul-11", "7-Jul-11", "8-Jul-11", "9-Jul-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-07-page-1-table-1.csv'})

for day in ["11-Jul-01", "12-Jul-01", "13-Jul-01", "14-Jul-01", "15-Jul-01", "16-Jul-01", "17-Jul-01", "18-Jul-01", "19-Jul-01", "20-Jul-01"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2001-07-page-2-table-1.csv'})

for day in ["19-Sep-08", "20-Sep-08", "21-Sep-08", "22-Sep-08", "23-Sep-08", "24-Sep-08", "25-Sep-08", "26-Sep-08", "27-Sep-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-09-page-3-table-1.csv'})

for day in ["10-Jun-10", "11-Jun-10", "12-Jun-10", "13-Jun-10", "14-Jun-10", "15-Jun-10", "16-Jun-10", "17-Jun-10", "18-Jun-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-06-page-2-table-1.csv'})

for day in ["27-Jun-05", "28-Jun-05", "29-Jun-05", "30-Jun-05"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2005-06-page-3-table-1.csv'})

for day in ["22-Jul-14", "23-Jul-14", "24-Jul-14", "25-Jul-14", "26-Jul-14", "27-Jul-14", "28-Jul-14", "29-Jul-14", "30-Jul-14", "31-Jul-14"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2014-07-page-3-table-1.csv'})

for day in ["27-Nov-04", "28-Nov-04", "29-Nov-04", "30-Nov-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-11-page-3-table-1.csv'})

for day in ["19-Apr-08", "20-Apr-08", "21-Apr-08", "22-Apr-08", "23-Apr-08", "24-Apr-08", "25-Apr-08", "26-Apr-08", "27-Apr-08"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2008-04-page-3-table-1.csv'})

for day in ["19-Oct-15", "20-Oct-15", "21-Oct-15", "22-Oct-15", "23-Oct-15", "24-Oct-15", "25-Oct-15", "26-Oct-15", "27-Oct-15"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2015-10-page-3-table-1.csv'})

for day in ["28-Mar-06", "29-Mar-06", "30-Mar-06", "31-Mar-06"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2006-03-page-4-table-1.csv'})

for day in ["10-Nov-11", "11-Nov-11", "12-Nov-11", "13-Nov-11", "14-Nov-11", "15-Nov-11", "16-Nov-11", "17-Nov-11", "18-Nov-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-11-page-2-table-1.csv'})

for day in ["1-Oct-10", "2-Oct-10", "3-Oct-10", "4-Oct-10", "5-Oct-10", "6-Oct-10", "7-Oct-10", "8-Oct-10", "9-Oct-10"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2010-10-page-1-table-1.csv'})

for day in ["1-Nov-01", "2-Nov-01", "3-Nov-01", "4-Nov-01", "5-Nov-01", "6-Nov-01", "7-Nov-01", "8-Nov-01", "9-Nov-01", "10-Nov-01"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2001-11-page-1-table-1.csv'})

for day in ["28-Apr-11", "29-Apr-11", "30-Apr-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-04-page-4-table-1.csv'})

for day in ["19-Jan-12", "20-Jan-12", "21-Jan-12", "22-Jan-12", "23-Jan-12", "24-Jan-12", "25-Jan-12", "26-Jan-12", "27-Jan-12"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2012-01-page-3-table-1.csv'})

for day in ["1-Jan-17", "2-Jan-17", "3-Jan-17", "4-Jan-17", "5-Jan-17", "6-Jan-17", "7-Jan-17", "8-Jan-17", "9-Jan-17", "10-Jan-17", "11-Jan-17", "12-Jan-17", "13-Jan-17", "14-Jan-17", "15-Jan-17", "16-Jan-17", "17-Jan-17", "18-Jan-17"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2017-01-page-1-table-1.csv'})

for day in ["28-Sep-11", "29-Sep-11", "30-Sep-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-09-page-4-table-1.csv'})

for day in ["10-Jan-07", "11-Jan-07", "12-Jan-07", "13-Jan-07", "14-Jan-07", "15-Jan-07", "16-Jan-07", "17-Jan-07", "18-Jan-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-01-page-2-table-1.csv'})

for day in ["10-Jan-11", "11-Jan-11", "12-Jan-11", "13-Jan-11", "14-Jan-11", "15-Jan-11", "16-Jan-11", "17-Jan-11", "18-Jan-11"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2011-01-page-2-table-1.csv'})

for day in ["28-Sep-07", "29-Sep-07", "30-Sep-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-09-page-4-table-1.csv'})

for day in ["28-Aug-16", "29-Aug-16", "30-Aug-16", "31-Aug-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-08-page-4-table-1.csv'})

for day in ["27-Jan-04", "28-Jan-04", "29-Jan-04", "30-Jan-04", "31-Jan-04"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2004-01-page-3-table-1.csv'})

for day in ["28-Apr-07", "29-Apr-07", "30-Apr-07"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2007-04-page-4-table-1.csv'})

for day in ["28-May-16", "29-May-16", "30-May-16", "31-May-16"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2016-05-page-4-table-1.csv'})

for day in ["19-Mar-09", "20-Mar-09", "21-Mar-09", "22-Mar-09", "23-Mar-09", "24-Mar-09", "25-Mar-09", "26-Mar-09", "27-Mar-09"]:
    rec = airtab.match('raw_date', day)
    if rec:
        airtab.update(rec['id'], {'citation': '2009-03-page-3-table-1.csv'})
