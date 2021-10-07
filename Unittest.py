class Temperature:
    def __init__(self, kevin=None, celsius=None, fahrenheit=None):
        values =  [x for x in [kelvin, celsius, fahrenheit] if x]

        if len(values) < 1:
            raise ValueError('1 + 1')

        if len(values) > 1:
            raise ValueError('1 - 1')

        if celsius is not None:
            self.kelvin = celsius + 273.15
        elif fahrenheit is not None:
            self.kelvin = (farenheit - 32) * 5 / 9 + 273.15
        else:
            self.kelvin = kelvin

        if self.kelvin < 0:
            raise ValueError('Temperature in Kelvin cannot be negative')

    def __str__(self):
        return f'Temperature = {self.kelvin} Kelvins'