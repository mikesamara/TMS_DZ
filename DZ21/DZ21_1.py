'''
Задача 2. Массовое обновление статусов рейсов
Создать функцию для пакетного обновления 
статусов рейсов (например, "Задержан" или "Отменен").
Функция должна:
- Принимать список рейсов и их новых статусов
- Подтверждать количество обновленных записей
- Обрабатывать ошибки (например, несуществующие рейсы)
Пример входных данных:
updates = [
    {"flight_id": 123, "new_status": "Delayed"},
    {"flight_id": 456, "new_status": "Cancelled"}
]
update_flights_status(updates)
'''
import pandas as pd
import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    port='5432',
    database ='demo',
    password = 'postgres',
    user = 'postgres'
)

def test_connection(conn):
    query = '''
            select 
                f.flight_id,
                f.flight_no, 
                f.status ,
                case  
                    when extract(epoch from(f.actual_departure - f.scheduled_departure)) / 60 > 0  or extract(epoch from(f.actual_arrival - f.scheduled_arrival)) / 60 > 0 then 'задержался'
                    when f.actual_departure is null then 'отменен'
                    else 'все ок'
                end as new_status
            from bookings.flights f 
            where f.status != 'Scheduled'
            '''
    with conn.cursor() as cursos:

        cursos.execute(query=query)
        print(cursos.fetchall())



def list_dupdate_flights_status(updates):
    for i in updates:
        print(i['flight_id'])
        print(i['new_status'])
        print(f'flight_id = {i['flight_id']}')
        print(f'update booking.test.flights f  set status = {i['new_status']} where f.flight_id = {i['flight_id']}')

#посмотреть что такое курсос, как его испольовать и как обновлять данные 


'''update booking.test.flights f  
set status = 'jhsdf'
where f.flight_id = 3'''



updates = [
    {"flight_id": 123, "new_status": "Delayed"},
    {"flight_id": 456, "new_status": "Cancelled"}
]

#list_dict(updates)
test_connection(conn)