import requests

user = input("enter website : ")
#INPUT FULL URL STARTING WITH HTTPS OR HTTP

try:
    response = requests.get(user)
    print("HTTP Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")
except ValueError:
    print("invalid input")
input("...")
