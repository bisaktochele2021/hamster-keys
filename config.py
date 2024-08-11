import os

my_bot_token = "6332838288:AAFUCr24eqPXfdAcH0BtAYRzO5LDKvTDDBo"
API_BASE_URL = "https://api.gamepromo.io/promo/"
EVENTS_DELAY = 20000
HEADERS_JSON = {
    'Content-Type': 'application/json; charset=utf-8',
    'Host': 'api.gamepromo.io'
}


games = {
    'BIKE': {
        'names': ['Riding Extreme 3D'],
        'appToken': 'd28721be-fd2d-4b45-869e-9f253b554e50',
        'promoId': '43e35910-c168-4634-ad4f-52fd764a843f',
        'delay': 10,
        'retry': 25,
        'keys': 4,
    },
    'CLONE': {
        'names': ['My Clone Army'],
        'appToken': '74ee0b5b-775e-4bee-974f-63e7f4d5bacb',
        'promoId': 'fe693b26-b342-4159-8808-15e3ff7f8767',
        'delay': 12,
        'retry': 25,
        'keys': 4,
    },
    'CUBE': {
        'names': ['Chain Cube 2048'],
        'appToken': 'd1690a07-3780-4068-810f-9b5bbf2931b2',
        'promoId': 'b4170868-cef0-424f-8eb9-be0622e8e8e3',
        'delay': 10,
        'retry': 25,
        'keys': 4,
    },
    'TRAIN': {
        'names': ['Train Miner'],
        'appToken': '82647f43-3f87-402d-88dd-09a90025313f',
        'promoId': 'c4480ac7-e178-4973-8061-9ed5b2e17954',
        'delay': 12,
        'retry': 25,
        'keys': 4,
    },
}
