from abc import ABC, abstractmethod
from typing import List

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        pass

# Subject interface
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass
    
    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass
    
    @abstractmethod
    def notify(self) -> None:
        pass

# Concrete Subject
class WeatherStation(Subject):
    def __init__(self):
        self._observers: List[Observer] = []
        self._temperature = 0.0
        self._humidity = 0.0
        self._pressure = 0.0
    
    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
    
    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)
    
    def set_measurements(self, temperature: float, humidity: float, pressure: float) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify()

# Concrete Observers
class CurrentConditionsDisplay(Observer):
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        print(f"\nCurrent conditions:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")

class StatisticsDisplay(Observer):
    def __init__(self):
        self._temperatures: List[float] = []
    
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        self._temperatures.append(temperature)
        avg_temp = sum(self._temperatures) / len(self._temperatures)
        max_temp = max(self._temperatures)
        min_temp = min(self._temperatures)
        
        print(f"\nTemperature Statistics:")
        print(f"Average: {avg_temp:.1f}°C")
        print(f"Maximum: {max_temp}°C")
        print(f"Minimum: {min_temp}°C")

class ForecastDisplay(Observer):
    def __init__(self):
        self._last_pressure = 0.0
        self._current_pressure = 0.0
    
    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        self._last_pressure = self._current_pressure
        self._current_pressure = pressure
        
        print("\nForecast:")
        if self._current_pressure > self._last_pressure:
            print("Improving weather on the way!")
        elif self._current_pressure == self._last_pressure:
            print("More of the same")
        else:
            print("Watch out for cooler, rainy weather")

# Client code
def main():
    # Create the WeatherStation
    weather_station = WeatherStation()
    
    # Create displays
    current_display = CurrentConditionsDisplay()
    statistics_display = StatisticsDisplay()
    forecast_display = ForecastDisplay()
    
    # Register displays with WeatherStation
    weather_station.attach(current_display)
    weather_station.attach(statistics_display)
    weather_station.attach(forecast_display)
    
    # Simulate weather changes
    print("First weather update:")
    weather_station.set_measurements(25.2, 65.0, 1013.1)
    
    print("\nSecond weather update:")
    weather_station.set_measurements(26.8, 70.0, 1014.3)
    
    print("\nThird weather update:")
    weather_station.set_measurements(23.9, 90.0, 1009.5)
    
    # Remove one display
    print("\nRemoving forecast display...")
    weather_station.detach(forecast_display)
    
    print("\nFourth weather update:")
    weather_station.set_measurements(24.5, 80.0, 1011.2)

if __name__ == "__main__":
    main() 