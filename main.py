from datetime import datetime

import requests
import os
from dotenv import load_dotenv
import datetime as dt
load_dotenv("C:/Python/Environmental variables/.env")

nutritionix_id = os.getenv("nutritionix_id")
nutritionix_key = os.getenv("nutritionix_api_key")

header = {
    "x-app-id":nutritionix_id,
    "x-app-key":nutritionix_key
}

parameters = {
    "query":input("Tell me which exercise you did ? "),
    "gender":"male",
    "weight_kg":75,
    "height_cm":182,
    "age":22
}
response = requests.post(url ="https://trackapi.nutritionix.com/v2/natural/exercise",data=parameters,headers=header)
data = response.json()
exercises = data["exercises"]
no_of_exercises = len(exercises)

today = dt.datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M")

for exercise in exercises:
    name = exercise["name"]
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]
    parameters = {
        "sheet1":{
            "date": date,
            "time": time,
            "exercise": name.title(),
            "duration": duration,
            "calories": calories
        }
    }

    response = requests.post(url = "https://api.sheety.co/f2cc6990c1585bc16e71a2d26e7a6fbf/workoutTracker/sheet1",
                             json=parameters)
    print(response.text)