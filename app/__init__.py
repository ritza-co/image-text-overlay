from flask import Flask
import os
import redis

redis_url = os.getenv('REDIS_URL')
conn = redis.from_url(redis_url)

app = Flask(__name__)

from app import views
