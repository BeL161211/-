import requests
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    apikey = os.getenv("apikey")

    url = "https://calendarific.com/api/v2/holidays?&api_key=baa9dc110aa712sd3a9fa2a3dwb6c01d4c875950dc32vs&country=US&year=2019"
    params = {
        "api_key":apikey,
        "country":"RU",
        "year":2026
    }
    response = requests.get(url,params=params)
    response.raise_for_status()

    months = ["Января", "Февраля", "Марта", "Апреля", "Мая", "Июня", "Июля", "Августа", "Сентября", "Октября", "Ноября", "Декабря"]
    for song in response.json()["response"]["holidays"]:
        song_date = f"""{song["date"]["datetime"]["day"]} {months[song["date"]["datetime"]["month"]-1]}"""
        song_name = song["name"]
        song_description = song["description"]

        print(f"""Дата: {song_date}\nНазвание праздника: {song_name}\nОписание: {song_description}\n""")


if __name__ == "__main__":
    main()