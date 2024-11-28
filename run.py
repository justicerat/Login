import subprocess
import requests
from datetime import datetime
from dateutil import parser
from colorama import Fore, Style
import os  


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


def authenticate(username, password):
    url = 'https://raw.githubusercontent.com/justicerat/Login/refs/heads/main/RAT3x.txt'  
    users = read_users_from_web(url)


    current_date = get_current_time_from_api()
    if current_date is None:
        print("Failed to retrieve the current date. Aborting login.")
        return False

    for user in users:
        if user['username'] == username and user['password'] == password:
            try:
                expiry_date = datetime.strptime(user['expiry_date'], '%Y-%m-%d')


                if current_date <= expiry_date:
                    return True
                else:
                    print("The account has expired.")
                    return False
            except ValueError:
                print(f"Error parsing the expiry date for {user['username']}.")
                return False

    print("Incorrect username or password.")
    return False


def run_pm2():
    try:

        current_directory = os.path.dirname(os.path.abspath(__file__))  
        index_js_path = os.path.join(current_directory, 'index.js')  


        subprocess.run(['pm2', 'start', index_js_path], check=True)
        print("PM2 process started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start PM2 process. Error: {e}")
    except FileNotFoundError as e:
        print(f"PM2 not found. Make sure PM2 is installed and in your PATH. Error: {e}")

# Ask for the username and password
username = input(Fore.RED + "Enter your username: " + Style.RESET_ALL)
password = input(Fore.RED + "Enter your password: " + Style.RESET_ALL)

# Authenticate the user
if authenticate(username, password):
    print(Fore.RED + "Login successful!" + Style.RESET_ALL)
    command = input(Fore.RED + "Please Type (RUN or run): " + Style.RESET_ALL).strip().lower()
    if command == "run" or command == "Run" or command == "RUN" or command == "RUn":

        run_pm2()
else:
    print("Login failed.")
