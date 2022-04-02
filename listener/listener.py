"""
1. funqcia chamovwerot chveni failebi old da new 10 wamis gansxvavbeit
2. listad vnaxot da igive logika, vabrunebt jsons tu delte aris mashin vshlit chveni direqtoriidan am fails bolos
3. shemdeg am failebs
"""

from utilities.client_class import CreateClient
from utilities.bucket_task import Bucket
from utilities.blob_class import Blob
import os
import pandas as pd
import time
import shutil

url = "/home/ninosha/Desktop/crud_task/Credentials/fair-solution" \
      "-345912-e1b814ef61f8.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = url
client = CreateClient(url, "My First Project").client

bucket = Bucket("crudtask", client)


class CheckUpdatedBlobs:
    def __init__(self, client_obj, bucket_obj):
        self.client_obj = client_obj
        self.bucket_obj = bucket_obj

    @staticmethod
    def download_file(dir_path):
        for blob in bucket.bucket.list_blobs():
            formatted_blob = str(blob).split()[2].replace(">", "")
            blob.download_to_filename(f"{dir_path}/{formatted_blob}")


updated_list = CheckUpdatedBlobs(client, bucket)
updated_list.download_file(
    "/home/ninosha/Desktop/crud_task/listener_data")


class CheckOperations:
    def __init__(self, updated_blobs_obj):
        self.updated_blobs_obj = updated_blobs_obj
        self.old_files = "/home/ninosha/Desktop/crud_task/old_blobs"
        self.new_files = "/home/ninosha/Desktop/crud_task/new_blobs"
        self.old_blobs_dir = os.listdir(self.old_files)
        self.new_blobs_dir = os.listdir(self.new_files)
        self.old_length = len(self.old_blobs_dir)
        self.new_length = len(self.new_blobs_dir)

    def if_updated(self):
        dfs_old = self.updated_blobs_obj.download_file(self.old_files)
        time.sleep(10)
        dfs_new = self.updated_blobs_obj.download_file(self.new_files)

        old_list = list(self.old_blobs_dir)
        new_list = list(self.new_blobs_dir)

        for index in range(len(old_list)):
            if self.new_length != self.old_length:
                if old_list[index] != new_list[index]:
                    print(f"{new_list[index]} was created")
                    shutil.copyfile(f'{self.new_files}/{new_list[index]}',
                                    f'{self.old_files}/{new_list[index]}')
                    return new_list[index]

                # if new list is created move the same file to old list too

                if new_list[index] != old_list[index]:
                    print(f"{old_list[index]} was deleted")
                    os.remove(f'{self.old_files}/{new_list[index]}')
                    # if it was delted delete in old list too

            # if it was not deleted and not created
            # check file ext make to df and compare dfs if dfs are different say that file was changed
                return old_list[index]


check = CheckOperations(updated_list)
check.if_updated()
