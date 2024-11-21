

# create a dictionary object to store weather details for 5 cities
weather_data = { "London": {"temperature": "15°C", "conditions": "Cloudy", "wind_speed": "5 km/h", "humidity": "80%"}, 
                "New York": {"temperature": "20°C", "conditions": "Sunny", "wind_speed": "10 km/h", "humidity": "50%"}, 
                "Tokyo": {"temperature": "18°C", "conditions": "Rainy", "wind_speed": "7 km/h", "humidity": "90%"}, 
                "Sydney": {"temperature": "22°C", "conditions": "Windy", "wind_speed": "15 km/h", "humidity": "60%"}, 
                "Paris": {"temperature": "17°C", "conditions": "Foggy", "wind_speed": "3 km/h", "humidity": "85%"} } 

# welcome prompt to obtain users name
name = input("Wecome to the bootcamp weather forecast. Please enter your name to log in: ")
print((f"Remember, {name} data cannot be guaranteed to be 100% accurate"))

# I am setting up a while loop so that user can retry to enter a city if the input is incorrect or if the city is not in the dictionary
while True:
        city = input("Please select the City you require. We have data for 'LONDON', 'NEW YORK','TOKYO', 'SYDNEY' 'PARIS'") # prompt user to enter city - with guide
        city = city.capitalize() # format user entry to match case in the dictionary
        if city in weather_data: # check if user entry matches dictionary and print weather if so
            city_weather = weather_data[city]
            print(f"Weather in {city}:")
            print(f"Temperature: {city_weather['temperature']}")    
            print(f"Conditions: {city_weather['conditions']}")
            print(f"Wind Speed: {city_weather['wind_speed']}")
            print(f"Humidity: {city_weather['humidity']}")
            print(f"Thankyou, {name} for using our weather forecaster")
            break   # exit after thanking user
        else:
            print(f"Sorry, we don't have weather data for {city}. Please enter a city") # user has entered invalid text so is prompted to try again
    
