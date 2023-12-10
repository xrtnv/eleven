def toUpper(a):
    '''Returnes uppercased word.'''
    return a.upper()


def secondToUpper(a):
    '''Returnes capitalized words.'''
    a = ' '.join(word.capitalize() for word in a.split())
    print(a)