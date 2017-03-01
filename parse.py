# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests


def get_all_the_book_links(author='any', english='any', genre='any',
                           text='any', audio='false', level='any', length='any'):
    book_list_url = 'http://english-e-reader.net/findbook'

    all_book_links = []

    data = {
        'author': author,
        'english': english,
        'genre': genre,
        'text': text,
        'audio': audio,
        'level': level,
        'length': length,
        'sortColumn': 'date',
        'sortType': 'DESC',
    }

    page = requests.post(book_list_url, data).content
    soup = BeautifulSoup(page, 'html.parser')

    for url in soup.find_all(attrs={'title': 'Open book'}):
        all_book_links.append(url.get('href'))

    return all_book_links


def get_books(book_links):
    books = []
    template = 'http://english-e-reader.net'

    for link in book_links:
        page = requests.get(template + link).content
        soup = BeautifulSoup(page, 'html.parser')

        download_link = []
        download_links = soup.find_all('p')[4]

        for p in download_links.find_all('a'):
            download_link.append(template + p.get('href'))

        book = {
            'title': soup.title.string,
            'level': soup.p.string.title(),
            'genre': soup.find_all('p')[1].string.title(),
            'author': soup.h4.get_text(),
            'description': soup.find_all('p')[3].string,
            'img': template + soup.find(attrs={'alt': 'Cover'}).get('src'),
            'epub': download_link[1],
            'mobi': download_link[2],
            'fb2': download_link[3],
            'rtf': download_link[4],
            'txt': download_link[5],
        }

        books.append(book)

    return books


def books_save(books):
    f = open('Books.txt', 'w')

    for book in books:
        f.write(
            '-' *
            40 +
            '\n' +
            'Title: {0}\nLevel: {1}\nGenre: {2}\nAuthor: {3}\nDescription: {4}\nImg: {5}\nEpub: {6}\nMobi: {7}\nFb2: {8}\nRtf: {9}\nTxt: {10}'.format(
                book['title'],
                book['level'],
                book['genre'],
                book['author'],
                book['description'],
                book['img'],
                book['epub'],
                book['mobi'],
                book['fb2'],
                book['rtf'],
                book['txt']) +
            '\n' +
            '-' *
            40 +
            '\n\n')


if __name__ == '__main__':
    liks = get_all_the_book_links(
        genre='detective',
        level='elementary',
        audio='true',
        length='short')
    books = get_books(liks)
    books_save(books)
    print('-' * 12 + '\n' + 'Books: ' + str(len(books)) + '\n' + '-' * 12)
