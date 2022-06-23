from app import app, conn
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

if __name__ == "__main__":
    app.run()
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()