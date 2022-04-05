import os
import shutil
import time

from auth.bucket_task import Bucket
from auth.client_class import CreateClient

url = "/home/ninosha/Desktop/crud_task/Credentials/fair-solution" \
      "-345912-e1b814ef61f8.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = url
client = CreateClient(url, "My First Project").client

bucket = Bucket("crudtask", client)


class CheckOperations:
    def __init__(self, client_obj, bucket_obj):
        self.client_obj = client_obj
        self.bucket_obj = bucket_obj
        self.old_files = "/home/ninosha/Desktop/crud_task/" \
                         "listener_data/old_blobs"
        self.new_files = "/home/ninosha/Desktop/crud_task/" \
                         "listener_data/new_blobs"
        self.old_blobs_dir = os.listdir(self.old_files)
        self.new_blobs_dir = os.listdir(self.new_files)
        self.old_length = len(self.old_blobs_dir)
        self.new_length = len(self.new_blobs_dir)

    @staticmethod
    def download_file(dir_path):
        for blob in bucket.bucket.list_blobs():
            formatted_blob = str(blob).split()[2].replace(">", "")
            blob.download_to_filename(f"{dir_path}/{formatted_blob}")

    def update_directories(self):
        self.download_file(self.old_files)

        time.sleep(5)

        self.download_file(self.new_files)

    def if_created_deleted(self):
        start = time.time()
        old = os.listdir(self.old_files)

        new = os.listdir(self.new_files)

        if len(old) < len(new):
            extra_files = list(set(new) - set(old))

            for file_index in range(len(extra_files)):
                extra_file = "".join(extra_files[file_index])

                print(f"{extra_file} was created")

                shutil.copyfile(
                    f'{self.new_files}/{extra_file}',
                    f'{self.old_files}/{extra_file}')
        end = time.time()
        print(start-end)
        if len(old) > len(new):
            extra_files = list(set(old) - set(new))
            for file_index in range(len(extra_files)):
                extra_file = "".join(extra_files[file_index])
                os.remove(
                    f'{self.old_files}/{extra_file}'
                )

                print(
                    f"{extra_file} was deleted"
                )

    def if_updated(self):
        for index in range(self.old_length):
            old_file = f'{self.old_files}/{self.old_blobs_dir[index]}'
            new_file = f'{self.new_files}/{self.new_blobs_dir[index]}'

            with open(old_file, 'r') as f:
                old = f.read()

            with open(new_file, 'r') as f:
                new = f.read()

            if old != new:
                print(f"{self.new_blobs_dir[index]} was updated")

    @staticmethod
    def if_read(download_path):
        old = os.listdir(download_path)
        time.sleep(10)
        new = os.listdir(download_path)

        extra_files = list(set(old) - set(new))

        for file_index in range(len(extra_files)):
            extra_file = " ".join(extra_files[file_index])

            if len(new) > len(old):
                print(f"File {extra_file} was read")


class Listener:
    def __init__(self, client_obj, bucket_obj):
        self.client_obj = client_obj
        self.bucket_obj = bucket_obj
        self.check_obj = CheckOperations(client_obj=client_obj,
                                         bucket_obj=bucket_obj)

    def listen(self):

        downloads_path = input(
            "Pass the full path of directory where you "
            "download files to read: ")

        while True:
            self.check_obj.update_directories()
            self.check_obj.if_created_deleted()
            self.check_obj.if_updated()
            self.check_obj.if_read(downloads_path)


listener = Listener(client, bucket)
listener.listen()
