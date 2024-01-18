import os
from dotenv import load_dotenv

load_dotenv()

INVENTORY_BASE_URL=os.getenv('INVENTORY_BASE_URL')
API_AUTH_APPLICATION_KEY=os.getenv('API_AUTH_APPLICATION_KEY')
API_AUTH_ACCOUNT_ID=os.getenv('API_AUTH_ACCOUNT_ID')

