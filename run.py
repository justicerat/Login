import subprocess
import requests
from datetime import datetime
from dateutil import parser

# Function to get the current time from an online time API
def get_current_time_from_api():
    try:
        response = requests.get('http://timeapi.io/api/Time/current/zone?timeZone=UTC')
        if response.status_code == 200:
            data = response.json()
            current_time = data['dateTime']
            return parser.parse(current_time)
        else:
            print("Error retrieving time from API.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the time: {e}")
        return None

# Function to read users data from a URL (web)
def read_users_from_web(url):
    users = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            lines = response.text.splitlines()
            for line in lines:
                username, password, expiry_date = line.strip().split(',')
                users.append({'username': username, 'password': password, 'expiry_date': expiry_date})
        else:
            print(f"Failed to retrieve file from the URL: {url}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    return users

# Function to authenticate the user
def authenticate(username, password):
    url = 'https://raw.githubusercontent.com/justicerat/Login/refs/heads/main/RAT3x.txt'  
    users = read_users_from_web(url)
    
    # Get the current time from the API (instead of using local time)
    current_date = get_current_time_from_api()
    if current_date is None:
        print("Failed to retrieve the current date. Aborting login.")
        return False
    
    for user in users:
        if user['username'] == username and user['password'] == password:
            try:
                expiry_date = datetime.strptime(user['expiry_date'], '%Y-%m-%d')
                
                # Compare the actual current date with expiry date
                if current_date <= expiry_date:
                    return True
                else:
                    print("The account has expired.")
                    return False
            except ValueError:
                print("Error parsing the expiry date.")
                return False
    
    print("Incorrect username or password.")
    return False

# Function to execute the pm2 command
def run_pm2():
    try:
        subprocess.run(['pm2', 'start', 'index.js'], check=True)
        print("PM2 process started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start PM2 process. Error: {e}")

# Ask for the username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Authenticate the user
if authenticate(username, password):
    print("Login successful!")
    command = input("Enter a command: ").strip().lower()
    if command == "run":
        run_pm2()
else:
    print("Login failed.")
