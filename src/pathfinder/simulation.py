
import random, datetime

def seed_all(s=1234):
    random.seed(s)

def fake_now():
    return datetime.datetime.now().isoformat()
