import sys
from flask import abort
import pymysql
from dbutils.pooled_db import PooledDB
from config import OPENAPI_STUB_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME

sys.path.append(OPENAPI_STUB_DIR)
from swagger_server import models

W = 18

pool = PooledDB(creator=pymysql,
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWD,
                database=DB_NAME,
                maxconnections=1,
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
        result = cs.fetchone()
    if result:
        ts, source, value = result
        return models.Sensor(*result)
    else:
        abort(404)

def get_water_consume():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT ts, source, value
            FROM SoftWet_sensor
            WHERE source=co2signal
        """)
        result = [] 
        for row in cs.fetchall():
            ts, source, value = row
            co2 = (float(value)/100)/W
            result.append(models.WaterConsume(ts, co2)) 

        return result

def get_water_consume_details(ts):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT ts, source, value
            FROM SoftWet_sensor
            WHERE source=co2signal AND ts=%s
        """, [ts])
        result = cs.fetchone()
    if result:
        ts, source, value = result
        co2 = (float(value)/100)/W
        
        return models.WaterConsume(ts, co2)
    else:
        abort(404)

def get_watering_next_time():
    return 'get_watering_next_time'

