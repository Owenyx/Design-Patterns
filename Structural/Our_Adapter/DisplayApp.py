


class DisplayApp():

    def __init__(self, adapter):
        self.__adapter = adapter

    def getForecast(self, data):
        return self.__adapter.getForecast(data)

    def displayForecast(self, data):
        print("Displaying forecast...")
        print("\n")
        forecast = self.getForecast(data)
        print(forecast)
