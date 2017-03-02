# Parser books from the site [English e-Reader](http://english-e-reader.net/)

You can parse books from the site [English e-Reader](http://english-e-reader.net/) using the methods:

### Get links on books
You can see filters on [this page](http://english-e-reader.net/findbook).
```python3
get_all_the_book_links(author='any', english='any', genre='any',
                           text='any', audio='false', level='any', length='any') # (author='any'..) - this is filters
```

### Parsing books
Нou have to pass a list of links to a method:
```python3
get_books(book_links)
```
