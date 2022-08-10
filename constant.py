allKeys = open("keys", "r").read().splitlines()

# Twitter Keys/Tokens
API_KEY = allKeys[0].strip()
API_KEY_SECRET = allKeys[1].strip()
ACCESS_TOKEN = allKeys[2].strip()
ACCESS_TOKEN_SECRET = allKeys[3].strip()

# Reddit Keys/Tokens
CLIENT_SECRET = allKeys[4].strip()
PASSWORD = allKeys[5].strip()