from abc import ABC, abstractmethod
from typing import Type
from DisplayApp import DisplayApp


class BintoXMLAdapter(DisplayApp):
    def __init__(self, adaptee):
        self.__adaptee = adaptee # WeatherForecastSystem

    def getForecast(self, sensorData):
        XML_data = self.__BintoXML(sensorData)
        forecast = self.__adaptee.makeForecast(XML_data)
        return self.__XMLtoBin(forecast)

    def __BintoXML(self, sensorData):
        print('\n')
        print("BintoXMLAdapter received sensor data")
        print(f"Binary data converted to XML")
        return sensorData

    def __XMLtoBin(self, forecast):
        print('\n')
        print(f"BintoXMLAdapter received forecast: {forecast}")
        print(f"XML data converted to binary")
        return forecast