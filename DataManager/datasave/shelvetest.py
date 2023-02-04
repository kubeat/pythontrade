import shelve


if __name__ == '__main__':
    with shelve.open('localdata') as sh:
        sh['key1'] = {
            'int': 10,
            'float': 9.5,
            'string': 'Sample data',
        }


