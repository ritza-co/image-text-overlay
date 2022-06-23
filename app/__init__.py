from flask import Flask
import os
import redis
from rq import Queue

redis_url = os.getenv('REDIS_URL')
conn = redis.from_url(redis_url)

que = Queue(connection=conn)

app = Flask(__name__)
