from Sensor import Sensor
from WeatherForecastSystem import WeatherForecastSystem
from BintoXMLAdapter import BintoXMLAdapter
from DisplayApp import DisplayApp

sensor = Sensor()
weatherForecastSystem = WeatherForecastSystem() # new system 
adapter = BintoXMLAdapter(weatherForecastSystem)
displayApp = DisplayApp(adapter)

displayApp.displayForecast(sensor.getSensorData())