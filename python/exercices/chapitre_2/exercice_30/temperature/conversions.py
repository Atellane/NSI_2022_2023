class convertir_temperature():
    def __init__(self, name: str) -> None:
        self.name = name + " :"
    
    def farhenheitEnCelsius(self, temperatureAConvertir: float) -> float :
        """Convertie une température donnée en degré farhenheit en degré celsius"""
        temperatureEnCelsius = (5 * (temperatureAConvertir - 32))/ 9
        return temperatureEnCelsius

    def celsiusEnFarhenheit(self, temperatureAConvertir: float) -> float :
        """Convertie une température donnée en degré celsius en degré farhenheit"""
        temperatureEnFarhenheit = temperatureAConvertir*9/5+32
        return temperatureEnFarhenheit