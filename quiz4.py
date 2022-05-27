import csv
import requests
import csv
from bs4 import BeautifulSoup
from time import sleep
from random import randint

f = open('movies.csv', 'w', newline='\n')
f_obj = csv.writer(f)
f_obj.writerow(['number', 'Title', 'Year', 'genre', 'runtime', 'Ranking', 'voteing'])
h = {'Accept-Language': 'en-US'}
ind = 1
while ind < 250:
    url = f'https://www.imdb.com/search/title/?title_type=feature&groups=bottom_250&start={str(ind)}&ref_=adv_nxt'
    r = requests.get(url, headers=h)
    soup_all = BeautifulSoup(r.text, 'html.parser')
    soup = soup_all.find('div', class_='lister-list')
    all_movies = soup.find_all('div', class_='lister-item')
    for each in all_movies:
        num = each.find('span', class_='lister-item-index').text
        d1 = each.find('div', class_='lister-item-content')
        title = d1.a.text
        year = each.find('span', class_='lister-item-year').text
        year = year.replace('(', '')
        year = year.replace(')', '')
        genre = each.find('span', class_='genre').text
        runtime = each.find('span', class_='runtime').text
        ranking = each.strong.text
        genre = genre.replace('\n', '')
        vote = each.find('p', class_="sort-num_votes-visible").text

        # es nawili ver gavmarte
        for i in range(0, len(vote)):
            sp = vote.find("|")
            o = vote.find(':')
            for j in range(o + 1, sp):
                vote += vote[j]
                vote = vote.replace("\n", '')
        # print(vote)
        f_obj.writerow([num, title, year, genre, runtime, ranking, vote])
    ind += 50
    sleep(randint(12, 15))



























