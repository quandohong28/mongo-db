# model.py
import os
import subprocess

class MongoDBModel:
    def __init__(self):
        self.process = None

    def start_mongod(self):
        if self.process is not None:
            return
        self.process = subprocess.Popen(
            ['mongod', '--dbpath', '/usr/local/mongodb/data/db'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return self.process

    def stop_mongod(self):
        if self.process is None:
            return
        subprocess.Popen(['pkill', 'mongod'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.process.terminate()
        self.process = None
