import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
YOUR_API_KEY = os.getenv("YOUR_API_KEY")
keys = {
    'евро': 'EUR',
    'доллар': 'USD',
    'рубль': 'RUB',
}
