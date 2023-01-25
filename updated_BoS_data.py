#!/usr/bin/env python
import os
import time

from airtable import Airtable
import requests
from bs4 import BeautifulSoup

airtab_mcj_counties = Airtable(os.environ['bos_db'], 'counties', os.environ['AIRTABLE_API_KEY'])
list_of_dicts = []
root_url = 'https://www.mssupervisors.org'

def get_county_urls():
    main_url = (root_url + '/ms-counties/adams')
    r = requests.get(main_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    list_of_links = soup.find("ul", id="countylist")
    county_links = list_of_links.find_all('a')
    for county_link in county_links:
        this_dict = {'county': county_link.string}
        this_dict['url'] = root_url + county_link.get('href')
        list_of_dicts.append(this_dict)
    
def scrape_county_data():
    for dict in list_of_dicts:
        r = requests.get(dict['url'])
        soup = BeautifulSoup(r.text, 'html.parser')
        county_table = soup.find("tbody")
        county_table_rows = county_table.find_all('tr')
        for county_table_row in county_table_rows:
            row_cells = county_table_row.find_all('td')
            if len(row_cells) == 2:
                this_key = row_cells[0].get_text(strip=True).replace(':', '').replace(' ', '_').lower()
                if this_key != '':
                    this_value = row_cells[1].get_text(strip=True)
                    dict[this_key] = this_value
        airtab_mcj_counties.insert(dict)
        time.sleep(0.5)


def main():
    get_county_urls()
    scrape_county_data()



