from flask import Flask
import os
import redis
from rq import Queue

redis_url = os.getenv('REDIS_URL')
conn = redis.from_url(redis_url)

app = Flask(__name__)

from app import views
