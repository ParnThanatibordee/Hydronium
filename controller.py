import sys
from flask import abort
import pymysql
from dbutils.pooled_db import PooledDB
from config import OPENAPI_STUB_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME

sys.path.append(OPENAPI_STUB_DIR)
from swagger_server import models
from datetime import timedelta

W = 18
PINNED_DEPTH = 6  # cm

pool = PooledDB(creator=pymysql,
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWD,
                database=DB_NAME,
                maxconnections=100,
                blocking=True)

def get_sensors():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT ts, source, value
            FROM SoftWet_sensor
        """)
        result = [models.Sensor(*row) for row in cs.fetchall()]
        return result

def get_sensor_details(source):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT ts, source, value
            FROM SoftWet_sensor
            WHERE source=%s
        """, [source])
        result = [models.Sensor(*row) for row in cs.fetchall()]
        return result

def get_water_consume():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT ts, source, value
            FROM SoftWet_sensor
            WHERE source='co2signal'
        """)
        result = [] 
        for row in cs.fetchall():
            ts, source, value = row
            co2 = (float(value)/100)*W
            result.append(models.WaterConsume(ts, co2)) 

        return result

def get_water_consume_details(ts):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT ts, source, value
            FROM SoftWet_sensor
            WHERE source='co2signal' AND ts=%s
        """, [ts])
        result = cs.fetchone()
    if result:
        ts, source, value = result
        co2 = (float(value)/100)*W
        
        return models.WaterConsume(ts, co2)
    else:
        abort(404)

def get_watering_next_time():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT ts, source, value
            FROM SoftWet_sensor
            WHERE source='tmd'
        """)
        fetch = cs.fetchall()

        if len(fetch) > 0:
            ts, source, value = fetch[len(fetch)-1]
        else:
            value = 0

        if value >= 10:
            return models.WaterAgain("The weather tends to rain, so you don't have to water yet.")
        else:
            cs.execute("""
                SELECT ts, source, value
                FROM SoftWet_sensor
                WHERE source='soil'
            """)
            fetch = cs.fetchall()

            if len(fetch) > 0:
                last_ts, source, value = fetch[len(fetch)-1]
                new_humidity = (float(value)/100) * PINNED_DEPTH
            else:
                last_ts = "No data."
                new_humidity = 0

            # next hour to watering
            cs.execute("""
            SELECT ts, source, value
            FROM SoftWet_sensor
            WHERE source='co2signal'
            """)
            result = [] 
            for row in cs.fetchall():
                ts, source, value = row
                float_value = float(value)
                if float_value > 0:
                    result.append(float_value)

            if len(result) > 0:
                water_consume = result[-1]
                co2 = (water_consume/100) * W

                next_hr = (new_humidity/co2) * W
            else:
                next_hr = 0

            # print('*', next_hr)

            # next_ts = ts + next_hr
            next_ts = last_ts + timedelta(hours=next_hr)

            # format datetime.datetime more readable
            new_ts = next_ts.strftime("%d/%m/%Y %H:%M:%S")

            return models.WaterAgain(new_ts) 

