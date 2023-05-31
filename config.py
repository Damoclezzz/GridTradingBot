import os

from dotenv import load_dotenv

load_dotenv()

KUCOIN_SECRET_KEY = os.getenv('KUCOIN_SECRET_KEY')
KUCOIN_API_KEY = os.getenv('KUCOIN_API_KEY')
