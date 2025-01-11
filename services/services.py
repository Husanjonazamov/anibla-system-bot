import requests
from utils.env import BASE_URL



def getUser(user_id):
    url = f"{BASE_URL}/user/{user_id}/"
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(response.status_code)
        
        
def getRejissyor():
    url = f"{BASE_URL}/user/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        directors = [user for user in data.get('data', {}).get('results', []) if user.get('role') == "rejissyor"]
        for director in directors:
            print(f"User ID: {director['user_id']}")
            return director
    else:
        print(f"Error fetching data: {response.status_code}")

        