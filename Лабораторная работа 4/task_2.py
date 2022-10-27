def get_count_char(str_):
    symbol_dict=dict()
    for symbol in str_: #Перебор всех символов в строке
        if symbol.isalpha() and symbol not in symbol_dict: #Условие, при котором символ является алфавитным и ещё не включен в словарь
            if str_.count(symbol)>=1:
                symbol_dict[symbol]=str_.count(symbol) #Добавление новых элементов в словарь
    return symbol_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
str_=''.join(main_str.lower().split(' '))
print(get_count_char(str_))








