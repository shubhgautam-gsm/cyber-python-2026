# Custom Exception
class TemperatureTooHighError(Exception):
    def __init__(self, temperature):
        self.temperature = temperature
    def __str__(self):
        return f"Temperature exceeded safe limit: {self.temperature}°C"
    # Example usage in a real-life scenario
def check_greenhouse_temperature(temp):
    if temp > 35:  # 35°C is the safe upper limit
        raise TemperatureTooHighError(temp)
    else:
        print(f"Temperature {temp}°C is within safe range.")

try:
    # Example: sensor reports a dangerously high temperature
    check_greenhouse_temperature(42)
except TemperatureTooHighError as e:
    print("🚨 ALERT:", e)
