import requests
import names
import json
import os
from colorama import init, Fore
import random

# Initialize colorama
init()

# Banner
BANNER = """
╔══════════════════════════════════════════════╗
║       🌟 PickPocket Bot - API Automation     ║
║   Automate your PickPocket API requests!     ║
║  Developed by: https://t.me/sentineldiscus   ║
╚══════════════════════════════════════════════╝
"""

# API Endpoint
URL = "https://pickpocket.app/api/subscribe/"

# Headers
HEADERS = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/json",
    "origin": "https://pickpocket.app",
    "priority": "u=1, i",
    "referer": "https://pickpocket.app/",
    "sec-ch-ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}

# Function to save email to specified JSON file
def save_email(email, filename):
    data = []
    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    if email not in data:
        data.append(email)
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(Fore.GREEN + f"[SUCCESS] Email {email} saved to {filename}")

# Function to send POST request
def send_request(email, filename):
    payload = {"email": email}
    try:
        response = requests.post(URL, headers=HEADERS, json=payload)
        if response.status_code == 200:
            print(Fore.GREEN + f"[SUCCESS] Request sent for {email} - Status: {response.status_code}")
            save_email(email, filename)
        else:
            print(Fore.RED + f"[FAILED] Request failed for {email} - Status: {response.status_code}")
    except Exception as e:
        print(Fore.RED + f"[ERROR] Failed to send request for {email}: {str(e)}")

# Mode 1: Automatic email generation
def auto_mode():
    try:
        num_requests = int(input(Fore.YELLOW + "Masukkan jumlah request: "))
        print(Fore.YELLOW + f"Memulai {num_requests} request dengan email otomatis...")
        for _ in range(num_requests):
            # Generate random name and create email
            random_name = names.get_first_name().lower() + str(random.randint(1, 999))
            email = f"{random_name}@gmail.com"
            print(Fore.YELLOW + f"Mengirim request untuk {email}...")
            send_request(email, "names.json")
    except ValueError:
        print(Fore.RED + "[ERROR] Masukkan angka yang valid untuk jumlah request!")

# Mode 2: Manual email input
def manual_mode():
    while True:
        email = input(Fore.YELLOW + "Masukkan email (0 untuk keluar): ")
        if email == "0":
            print(Fore.YELLOW + "Keluar dari mode manual.")
            break
        if "@" not in email or not email.endswith("gmail.com"):
            print(Fore.RED + "[ERROR] Masukkan email Gmail yang valid!")
            continue
        print(Fore.YELLOW + f"Mengirim request untuk {email}...")
        send_request(email, "gmail.json")

# Main function
def main():
    print(BANNER)
    while True:
        print(Fore.YELLOW + "\nPilih mode:")
        print("1. Otomatis (generate email random)")
        print("2. Manual (input email sendiri)")
        print("0. Keluar")
        choice = input(Fore.YELLOW + "Masukkan pilihan (0-2): ")
        
        if choice == "1":
            auto_mode()
        elif choice == "2":
            manual_mode()
        elif choice == "0":
            print(Fore.YELLOW + "Terima kasih telah menggunakan PickPocket Bot!")
            break
        else:
            print(Fore.RED + "[ERROR] Pilihan tidak valid!")

if __name__ == "__main__":
    main()
