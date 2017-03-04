# Parser books from the site [English e-Reader](http://english-e-reader.net/)

You can parse books from the site [English e-Reader](http://english-e-reader.net/) using the methods:

### Import
```python3
import ebparse
```

### Get links on books
You can see filters on [this page](http://english-e-reader.net/findbook).
```python3
ebparse.get_all_the_book_links(author='any', english='any', genre='any',
                           text='any', audio='false', level='any', length='any') # (author='any'..) - this is filters
```

### Parsing books
Нou have to pass a list of links to a method:
```python3
ebparse.get_books(book_links)
```

### Saving books
You can save result of parsing in file
```python3
def books_save(books, file_name='Books'):
```

File:
```
----------------------------------------
Title: Board Games
Level: Elementary
Genre: Detective
Author:  Butler James
Description: Arthur Mowbray is a head of a huge company. He created his company after he had invented a board game “Mowbray’s Killer”. The game was made of cardboard and Plasticine figures. One day something terrible happened. His body was found in the dining room of his country house. Inspector Ainsworth started investigating this case. He has no evidence and no witnesses. But there are many suggestions. Ainsworth suspects that one of the directors can be guilty. He has to dive into the world of a fierce competition between the employees to learn the real truth and to find the killer. Will he be able to remain unharmed at the end? And the company is not so great it appears to be at first glance. Let’s see what a single inspector can do against the entire corporation. 
Img: http://english-e-reader.net/books/elementary/Board_Games-Butler_James/Board_Games-Butler_James.jpg
Epub: http://english-e-reader.net/download?link=board-games-butler-james&format=epub
Mobi: http://english-e-reader.net/download?link=board-games-butler-james&format=mobi
Fb2: http://english-e-reader.net/download?link=board-games-butler-james&format=fb2
Rtf: http://english-e-reader.net/download?link=board-games-butler-james&format=rtf
Txt: http://english-e-reader.net/download?link=board-games-butler-james&format=txt
----------------------------------------
[...]
```

### Example
```python3
>>> links = ebparse.get_all_the_book_links(
        genre='detective',
        level='elementary',
        audio='true',
        length='short')
        
>>> books = ebparse.get_books(liks)
>>> books[0]['title']
"Board Games"
>>> ebparse.save(books, file_name='Books')
------------
Books: 8
------------
```
