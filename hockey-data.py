import requests

def get_nhl_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any HTTP errors
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

if __name__ == "__main__":
    nhl_url = "https://statsapi.web.nhl.com/api/v1/"
    nhl_data = get_nhl_data(nhl_url)

    if nhl_data:
        print("NHL data retrieved successfully.")
        # Now you can access and process the data as needed.
        # For example, to see the structure of the retrieved data:
        print(nhl_data)
    else:
        print("Failed to retrieve NHL data.")
