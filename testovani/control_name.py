if __name__ == '__main__':
    #name1, name2 = 'Kateřina', ''
    #name1, name2 = '', ''
    name1, name2 = '', 'Tomas'
    
    if name := name1 or name2:
        print(name)
        print('Nalezen')
    else:
        print('Jméno nenalezeno...')