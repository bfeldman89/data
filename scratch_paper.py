import csv
import requests
from bs4 import BeautifulSoup

muh_headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}


def raid_library():
    url = 'https://www.prisonpolicy.org/research/whats_new_all.html'
    r = requests.get(url, headers=muh_headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    long_list = soup.find(id="longlist")
    with open('prison_policy_resource_library.csv', 'w', newline='') as csvfile:
        fieldnames = ['link', 'text']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for link in long_list.find_all('a'):
            this_dict = {}
            this_dict['link'] = link.get('href')
            this_dict['text'] = link.string
            writer.writerow(this_dict)
