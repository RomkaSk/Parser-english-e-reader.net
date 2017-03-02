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
### Example
```python3
>>> ebparse.links = get_all_the_book_links(
        genre='detective',
        level='elementary',
        audio='true',
        length='short')
        
>>> ebparse.books = get_books(liks)
>>> ebparse.books[0]['title']
"Board Games"
```
