import uuid
import time
import requests
from config import API_BASE_URL, HEADERS_JSON
from utils import generate_client_id

async def login_client(key):
    client_id = await generate_client_id()
    json = {
        'appToken': key['appToken'],
        'clientId': client_id,
        'clientOrigin': 'deviceid'
    }
    response = requests.post(f'{API_BASE_URL}login-client',
                             json=json,
                             headers=HEADERS_JSON)
    res = response.json()
    time.sleep(key['delay'])
    return res["clientToken"]

def register_event(key, clientToken):
    while True:
        event_id = str(uuid.uuid4())
        data = {
            'promoId': key['promoId'],
            'eventId': event_id,
            'eventOrigin': 'undefined'
        }
        headers = {**HEADERS_JSON, 'Authorization': f'Bearer {clientToken}'}
        response = requests.post(f'{API_BASE_URL}register-event',
                                 json=data,
                                 headers=headers)

        result = response.json()
        print(result)
        if result.get('hasCode'):
            return

        time.sleep(key['retry'])

async def create_code(key, clientToken):
    headers = {**HEADERS_JSON, 'Authorization': f'Bearer {clientToken}'}
    json = {'promoId': key['promoId']}
    response = requests.post(f"{API_BASE_URL}create-code", json=json, headers=headers)
    pcode = response.json()
    return pcode