import time
import random

async def generate_client_id():
    timestamp = str(int(time.time() * 1000))
    random_numbers = ''.join([str(random.randint(0, 9)) for _ in range(19)])
    return f"{timestamp}-{random_numbers}"