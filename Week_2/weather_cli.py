import requests, json, logging, os


logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_weather(city):

    url = "https://wttr.in/"

    params = {
        "format" : "j1"
    }

    try: 
        logging.info("Fetching weather for %s", city)

        response = requests.get(
        url + city,
        params = params,
        timeout = 5
        )

        response.raise_for_status()

        data = response.json()

        current = data["current_condition"][0]

        temperature = current["temp_C"]
        humidity = current["humidity"]
        weather = current["weatherDesc"][0]["value"]

        logging.info("Weather fetched successfully for %s", city)

        return {    
            "city": city,
            "temperature": temperature,
            "humidity": humidity,
            "weather": weather
        }
    
       
    except requests.RequestException as e:
        logging.error("API request failed: %s", e)
        print("Actual error: ", e)
        return None

def main():
    city = input("Enter city: ")

    result = get_weather(city)

    if result:
        print("City:", result["city"])
        print("Temperature:", result["temperature"], "C")
        print("Humidity:", result["humidity"], "%")
        print("Weather:", result["weather"])

    else:
        print("Error: Could not fetch weather data.")

if __name__=="__main__":
    main()
