salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
n=1 #порядковый номер месяца

while(n!=11):
    need_money+=spend-salary;
    n += 1;
    spend+=spend*increase;
print(round(need_money))
