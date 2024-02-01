class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin_temp = celsius + 273.15
        farenheit_temp = celsius * 1.80 + 32.00
        return [kelvin_temp, farenheit_temp]
        