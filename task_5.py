"""
5. Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна передаваться фиксированная
ежемесячная сумма пополнения вклада. Необходимо в главной функции реализовать вложенную функцию подсчета процентов
для пополняемой суммы. Примем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего.
Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев.
Вложенная функция возвращает сумму дополнительно внесенных средств (с процентами), а главная функция —
общую сумму по вкладу на конец периода.
"""


def deposit(start_sum, period, add_sum):
    my_list = [{'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5},
               {'begin_sum': 10000, 'end_sum': 100000, 6: 6, 12: 7, 24: 6.5},
               {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5}]
    for my_dict in my_list:
        if my_dict['begin_sum'] <= start_sum < my_dict['end_sum']:
            if period in my_dict:
                percent = my_dict[period]/100
                monthly_sum = start_sum * percent / 12
                def plus_sum(add_sum=add_sum):
                    added_period = period - 2 #период расчета процентов
                    added_monthly_sum = added_period * add_sum #общая пополняемая сумма за весь период
                    added_monthly_percent = (add_sum * percent / 12) * added_period # получаемые проценты за весь период
                    total_added_sum = added_monthly_sum + added_monthly_percent
                    return total_added_sum
                return f'Cумма вклада на конец срока составит: {round((start_sum + monthly_sum * period)+plus_sum(add_sum), 2)}'

print(deposit(100000, 12, 1000))


