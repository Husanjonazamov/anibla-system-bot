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
        
        
def getRejissyorList():
    url = f"{BASE_URL}/user/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        directors = [
            user for user in data.get('data', {}).get('results', [])
            if user.get('role') == "rejissyor"
        ]
        return directors
    else:
        print(f"Error fetching data: {response.status_code}")
        return []
    

def createAnime(anime):
    url = f"{BASE_URL}/anime/"
    try:
        response = requests.post(url, json=anime)
        if response.status_code in [200, 201]:
            data = response.json()
            return data
        else:
            print(response.status_code)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        
        
        
        
def getTranslatorList():
    url = f"{BASE_URL}/user/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        directors = [
            user for user in data.get('data', {}).get('results', [])
            if user.get('role') == "tarjimon"
        ]
        return directors
    else:
        print(f"Error fetching data: {response.status_code}")
        return []
    


def getVoiceAktyorList():
    url = f"{BASE_URL}/user/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        directors = [
            user for user in data.get('data', {}).get('results', [])
            if user.get('role') == "ovoz aktyori"
        ]
        return directors
    else:
        print(f"Error fetching data: {response.status_code}")
        return []
    
    
def getTimerList():
    url = f"{BASE_URL}/user/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        directors = [
            user for user in data.get('data', {}).get('results', [])
            if user.get('role') == "timer"
        ]
        return directors
    else:
        print(f"Error fetching data: {response.status_code}")
        return []
    