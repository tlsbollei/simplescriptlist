import requests

def check_paths(domain, paths):
    for path in paths:
        url = f"https://{domain}{path}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"Found: {url}")
            else:
                print(f"Not Found: {url}")
        except requests.RequestException:
            print(f"Error accessing: {url}")

def main():
    domain = input("Enter the domain (e.g., example.com): ").strip()
    common_vulnerable_paths = [
        "/admin",
        "/login",
        "/phpmyadmin",
        "/wp-admin"
    ]

    print(f"Checking common paths for {domain}...")
    check_paths(domain, common_vulnerable_paths)
    
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
