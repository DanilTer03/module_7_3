# %
team1 = 'Мастера кода'
team2 = 'Волшебники данных'

team1_num = 5
team2_num = 6

print('В команде %s участников: %s!' % (team1, team1_num))
print('Итого сегодня в командах участников: %s и %s' % (team1_num, team2_num))

# .format()
score_1 = 31
score_2 = 42

team1_time = 15465.0
team2_time = 18015.2

print('Команда {} решила задач: {}'.format(team2, score_2))
print('{} решили задачи за {} c.'.format(team2, team2_time))

# f-string

print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = f'Победа команды {team1}!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = f'Победа команды {team2}!'
else:
    result = 'Ничья!'

print(f'Результат битвы: {result}')

tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg,1)} на задачу!')