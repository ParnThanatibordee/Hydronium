# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.sensor import Sensor  # noqa: E501
from swagger_server.models.water_again import WaterAgain  # noqa: E501
from swagger_server.models.water_consume import WaterConsume  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_controller_get_sensor_details(self):
        """Test case for controller_get_sensor_details

        Returns complete details of the specified sensors.
        """
        response = self.client.open(
            '/hydro/v1/sensors/{source}'.format(source='source_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_sensors(self):
        """Test case for controller_get_sensors

        Returns a list of sensors.
        """
        response = self.client.open(
            '/hydro/v1/sensors',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_water_consume(self):
        """Test case for controller_get_water_consume

        Returns a list of water consuming.
        """
        response = self.client.open(
            '/hydro/v1/water/consume',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_water_consume_details(self):
        """Test case for controller_get_water_consume_details

        Returns complete details of the specified timestamp.
        """
        response = self.client.open(
            '/hydro/v1/water/consume/{ts}'.format(ts='ts_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_watering_next_time(self):
        """Test case for controller_get_watering_next_time

        Returns next datetime to watering.
        """
        response = self.client.open(
            '/hydro/v1/water/nextWatering',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
