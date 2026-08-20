from weather_cli import get_weather
from unittest.mock import patch
import requests


@patch("weather_cli.requests.get")
def test_get_weather(mock_get):

    fake_data = {
        "current_condition": [
            {
                "temp_C": "30",
                "humidity": "60",
                "weatherDesc": [
                    {
                        "value": "Sunny"
                    }
                ]
            }
        ]
    }

    mock_get.return_value.json.return_value = fake_data

    result = get_weather("Khammam")

    assert result["city"] == "Khammam"
    assert result["temperature"] == "30"
    assert result["humidity"] == "60"
    assert result["weather"] == "Sunny"

@patch("weather_cli.requests.get")
def test_get_weather_failure(mock_get):

    mock_get.side_effect = requests.RequestException("API failed")

    result = get_weather("Khammam")

    assert result is None