travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

def add_new_country(country, times_visited, cities):
    travel_log.append({"country": country, "visits": times_visited, "cities": cities})

add_new_country("Russia", 2, ["Moscow", "Sain Petersburg"])

print(travel_log[2]["country"])