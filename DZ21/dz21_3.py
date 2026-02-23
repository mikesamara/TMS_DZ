'''
Динамическое ценообразование
Реализовать функцию, которая автоматически корректирует
цены на билеты в зависимости от спроса:
- Повышает цены на 10%, если продано >80% мест
- Понижает на 5%, если продано <30% мест
- Не изменяет цены бизнес-класса
'''
  
# кол-во всего мест

select 
s.aircraft_code,
s.fare_conditions,
count(*)
from seats s 
group by 1, 2
order by 1


# кол-во проданных мест

select 
tf.flight_id,
tf.fare_conditions,
count(*)
from ticket_flights tf 
group by 1,2 
order by 1
