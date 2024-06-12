import requests

api_key = 'ed286ec1436597cf3a0ec3067d5da23c'

# Prompt the user to enter the city name until 'exit' is entered
while True:
    try:
        city_name = input("Enter city name (TYPE exit TO QUIT): ")
        if city_name == 'exit':
            break

        # Construct the URL for the API call
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=imperial'

        # Get weather data from the API
        forecast = requests.get(url)

        # Check the status code of the response
        if forecast.status_code == 200:
            display = forecast.json()

            # Extract relevant weather information
            description = display['weather'][0]['description']
            temperature = display['main']['temp']
            feels_like = display['main']['feels_like']
            humidity = display['main']['humidity']

            # Converting temp Fahrenheit to Celsius
            celcius = (temperature - 32) * 5 / 9

            # Display weather information
            print('Weather:', description)
            print('Temperature:', temperature, '°F (', round(celcius, 2), '°C )')
            print('Feels like:', feels_like, '°F')
            print('Humidity:', humidity, '%')
        else:
            print("The City does not exists")

    except Exception as e:
        print(f"An error occurred: {e}")

    print() 
