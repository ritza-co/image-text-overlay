from flask import Flask
import os
import redis
from rq import Queue

app = Flask(__name__)

from app import views

redis_url = os.getenv('REDIS_URL')
conn = redis.from_url(redis_url)

que = Queue(connection=conn)
