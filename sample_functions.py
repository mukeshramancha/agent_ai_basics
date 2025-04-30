
def get_weather(city: str):
    if city == "California":
        return "It is sunny and 70 degrees"
    elif city == "New York":
        return "It is cloudy and 60 degrees"
    elif city == "Paris":
        return "It is sunny and 50 degrees"
    elif city == "London":
        return "It is rainy and 55 degrees"
    elif city == "Toronto":
        return "It is snowy and 32 degrees"
    else:
        return "Sorry, I don't know the weather in that city"

