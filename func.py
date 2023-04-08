def func1(file):
    try:
        with open(file) as file:
            func2(file)
    except FileNotFoundError:
        print('Файл не найден!')
        return None
    except:
        print("Ошибка!")
        return None
    return True

def func2(file):
    l_count = {}
    for line in file:
        for letter in line:
            if letter.isalpha():
                if letter in l_count:
                    l_count[letter] += 1
                else:
                    l_count[letter] = 1
    
    for letter, c in l_count.items():
        print(f'{letter}: {c}')


