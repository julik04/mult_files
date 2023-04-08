from func import func1

if __name__=='__main__':
    s = None
    while (s == None):
        file = input('Введите имя файла: ')
        s = func1(file)
