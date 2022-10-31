symbol_dict=dict()
def get_count_char(str_):
    str_ = ''.join(main_str.lower().split(' '))
    for symbol in str_: #Перебор всех символов в строке
        if symbol.isalpha() and symbol not in symbol_dict: #Условие, при котором символ является алфавитным и ещё не включен в словарь
            symbol_dict[symbol]=str_.count(symbol) #Добавление новых элементов в словарь
    return symbol_dict
def get_percent(symbol_dict):
    sum_ = sum(symbol_dict.values())
    for i in symbol_dict:
        symbol_dict[i] = round((symbol_dict[i] / sum_) * 100, 3)
    return symbol_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
