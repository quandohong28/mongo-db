# controller.py
import threading
from src.model import MongoDBModel
from src.view import MongoDBView

class MongoDBController:
    def __init__(self, root):
        self.model = MongoDBModel()
        self.view = MongoDBView(root)
        self.setup_event_handlers()

    def setup_event_handlers(self):
        self.view.start_button.config(command=self.start_mongod)
        self.view.stop_button.config(command=self.stop_mongod)

    def start_mongod(self):
        self.view.update_status("Starting MongoDB...")
        threading.Thread(target=self.run_mongod).start()

    def stop_mongod(self):
        self.model.stop_mongod()
        self.view.update_status("MongoDB stopped")

    def run_mongod(self):
        process = self.model.start_mongod()
        if process:
            for line in iter(process.stdout.readline, ''):
                self.view.append_log(line)
            process.stdout.close()
            process.wait()
