import requests

API_BASE_URL = "https://www.wienerlinien.at/ogd_realtime/monitor"


def fetch_data(stop_id):
    api_url = f"{API_BASE_URL}?stopId={stop_id}"

    try:
        response = requests.get(api_url)

        # Raises an HTTPError for bad responses (4xx or 5xx).
        response.raise_for_status()

        data = response.json()

        monitors = data.get("data", {}).get("monitors", [])

        departures_list = []

        if monitors:
            lines = monitors[0].get("lines", [])

            for line in lines:
                departures = line.get("departures", {}).get("departure", [])

                if departures:
                    departure_info = {
                        "name": line.get("name", "?"),
                        "towards": line.get("towards", "?"),
                        "countdown": departures[0]
                        .get("departureTime", {})
                        .get("countdown"),
                    }

                    departures_list.append(departure_info)

        return departures_list, None

    except requests.exceptions.RequestException as e:
        return None, f"Network Error: {e}"

    except Exception as e:
        return None, f"Error: {e}"


if __name__ == "__main__":
    # For testing purposes:
    # 4118 = "Stephansplatz", line = "U1", direction = "Oberlaa/Alaudagasse"
    TEST_STOP_ID = 4118

    print(f"Fetching data for stop ID: {TEST_STOP_ID}")

    departures_list, err = fetch_data(TEST_STOP_ID)

    if err:
        print(f"An error occurred: {err}")
    elif not departures_list:
        print("No departures found.")
    else:
        print("Success! Data received:")
        print(departures_list)
