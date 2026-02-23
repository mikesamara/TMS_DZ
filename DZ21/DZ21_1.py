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
        result = cursos.fetchall()

        updates = []
        count = 0
        for row in result:
            flight_id = row[0]
            new_status = row[1]

            update_dict = {'flight_id': flight_id, 'new_status': new_status}
            updates.append(update_dict)
            count += 1

        
        return updates, count



def list_dupdate_flights_status(updates, count):
    df = pd.DataFrame(updates)
    df.to_excel('/Users/maiksamarchuk/PycharmProjects/teachsills/DZ/TMS_DZ/DZ21/new_file_status.xlsx', index=False)

    print(f'Кол-во обновленных записей {count}')


updates, count = test_connection(conn)
list_dupdate_flights_status(updates, count)