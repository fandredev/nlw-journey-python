import requests

payload = {
    "requestor": "YourNameOrAppName",
    "version": "1.0",
}

response = requests.post("http://api.nodemailer.com/user", json=payload)

if response.status_code == 200:
    print(response.json())

else:
    raise Exception(
        "Request failed with status code: "
        + str(response.status_code)
        + " and message: "
        + response.text
    )
