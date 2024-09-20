import requests
import os
from dotenv import load_dotenv
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
response = requests.post(url ="https://trackapi.nutritionix.com/v2/natural/exercise",params=parameters,headers=header)
print(response.json())