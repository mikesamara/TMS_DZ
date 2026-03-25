'''Задача 1. Экспорт расписания рейсов по конкретному маршруту.
Нужно создать функцию на Python, которая выгружает 
в CSV-файл расписание рейсов между двумя городами 
(например, Москва и Санкт-Петербург). 
Функция должна включать:
- Номер рейса
- Время вылета и прилета
- Тип самолета
- Среднюю цену билета
❗️SELECT сделать без использования pandas!❗️
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

def get_flights(conn, dep_city, arr_city):
    query = ''' 
            select 
                f.flight_no,
                f.scheduled_departure,
                f.scheduled_arrival,
                f.aircraft_code,
                round(avg(tf.amount ), 0)
            from bookings.flights f 
            join bookings.ticket_flights tf on tf.flight_id = f.flight_id
            join bookings.airports a on a.airport_code = f.departure_airport 
            join bookings.airports a2 on a2.airport_code =f.arrival_airport 
            where a.city = %s and a2.city =  %s
            group by 1, 2, 3, 4
            '''
    
    df = pd.read_sql(query, conn, params=(dep_city,arr_city))
    df.to_csv(f'/Users/maiksamarchuk/PycharmProjects/teachsills/DZ/TMS_DZ/DZ21/flights_{dep_city} - {arr_city}.csv', index=False, encoding='UTF-8')
    return df

get_flights(conn, 'Москва', 'Мирный')
conn.close