import connexion
import six

from swagger_server.models.sensor import Sensor  # noqa: E501
from swagger_server.models.water_again import WaterAgain  # noqa: E501
from swagger_server.models.water_consume import WaterConsume  # noqa: E501
from swagger_server import util


def controller_get_sensor_details(source):  # noqa: E501
    """Returns complete details of the specified sensors.

     # noqa: E501

    :param source: 
    :type source: str

    :rtype: List[Sensor]
    """
    return 'do some magic!'


def controller_get_sensors():  # noqa: E501
    """Returns a list of sensors.

     # noqa: E501


    :rtype: List[Sensor]
    """
    return 'do some magic!'


def controller_get_water_consume():  # noqa: E501
    """Returns a list of water consuming.

     # noqa: E501


    :rtype: List[WaterConsume]
    """
    return 'do some magic!'


def controller_get_water_consume_details(ts):  # noqa: E501
    """Returns complete details of the specified timestamp.

     # noqa: E501

    :param ts: 
    :type ts: str

    :rtype: List[WaterConsume]
    """
    return 'do some magic!'


def controller_get_watering_next_time():  # noqa: E501
    """Returns next datetime to watering.

     # noqa: E501


    :rtype: List[WaterAgain]
    """
    return 'do some magic!'
