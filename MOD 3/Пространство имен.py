calls = 0
def count_calls():
    global calls
    calls = calls + 1
def string_info(string):
    print(len(string), string.upper(), string.lower())
    count_calls()
def is_contains(string, list_to_search):
    a = [x.lower() for x in list_to_search]
    flag = False
    for value in a:
        if value == string.lower():
            flag = True
            break
    if flag:
        print(True)
    else:
        print(False)

    count_calls()

string_info('Eeeeee')
string_info('Абракадабра')
string_info('Привет мир')
is_contains('qWe', ['qwea', 'QWea', '1212', 'true'])
is_contains('RUs', ['R', 'Russian', 'Ru', 'RuS'])
is_contains('ТаБуРеТкА', ['Асфальт', 'КоНус', 'Покемон', 'табурет'])
print(calls)
