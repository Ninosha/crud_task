
class Listener:
    def __init__(self, client_obj, bucket_ob):
        self.client_obj = client_obj
        self.bucket_ob = bucket_ob
        self.logs_path = "/home/ninosha/Desktop/crud_task/" \
                         "listener_data/logs.csv"

    def get_logs(self):
        while True:
            pass


