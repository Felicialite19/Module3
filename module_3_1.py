calls = 0

def count_calls(): # подсчитывает вызовы других функций
    global calls
    calls += 1

def string_info(string): # (количество символов, в вархнем регистре, в нижнем регистре)
    line = str(string)
    text = len(line), line.upper(), line.lower()
    count_calls()
    return text

def is_contains(string,list_to_search): # поиск в строке
    string = str(string).lower()
    list_to_search = list (list_to_search)
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            text = True
            break
        else:
            text = False
            continue
    count_calls()
    return text


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)