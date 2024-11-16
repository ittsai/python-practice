from ui import QuizInterface

import requests

parameters = {
    "amount": 50,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

question_data = response.json()["results"]

question_interface = QuizInterface(question_data)

