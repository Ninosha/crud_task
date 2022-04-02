"""
1. connect to gcp
2. see if bucket is empty and what files are on it
3. while true check if file numbers are raised message what file was created dowload all files from gcp
4. check all files data and compare dowloaded files in dataframes message updated
5. id files are less then it was message deleted
6. check
"""

from utilities.client_class import CreateClient
from utilities.bucket_task import Bucket
from utilities.blob_class import Blob
import os
import pandas as pd
import time

url = "/home/ninosha/Desktop/crud_task/Credentials/fair-solution" \
      "-345912-e1b814ef61f8.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = url
client = CreateClient(url, "My First Project").client

bucket = Bucket("crudtask", client)


class CheckUpdatedBlobs:
    def __init__(self, client_obj, bucket_obj):
        self.client_obj = client_obj
        self.bucket_obj = bucket_obj

    # @property
    # def blob_list(self):
    #     blob_list = []
    #     for blob in bucket.bucket.list_blobs():
    #         formatted_blob_name = str(blob).split()[2].replace(">", "")
    #         blob_list.append(formatted_blob_name)
    #     return blob_list

    @staticmethod
    def download_file(dir_path):
        dfs = []
        print(dfs)
        for blob in bucket.bucket.list_blobs():
            formatted_blob = str(blob).split()[2].replace(">", "")
            blob.download_to_filename(f"{dir_path}/{formatted_blob}")
            # if "csv" in formatted_blob:
            #
            #     dfs.append(pd.read_csv(f"{dir_path}/{formatted_blob}"))
            #
            # if "json" in formatted_blob:
            #     dfs.append(pd.read_json(f"{dir_path}/{formatted_blob}"))
            #
            # if "txt" in formatted_blob:
            #     pass

        return dfs


updated_list = CheckUpdatedBlobs(client, bucket)
print(updated_list.download_file(
    "/home/ninosha/Desktop/crud_task/listener_data"))


class CheckOperations:
    def __init__(self, updated_blobs_obj):
        self.updated_blobs_obj = updated_blobs_obj

    def if_created(self):
        old_list = self.updated_blobs_obj.blob_list()
        time.sleep(10)
        new_list = self.updated_blobs_obj.blob_list()
        for index in range(len(old_list)):
            if old_list[index] == new_list[index]:
                pass
            else:
                print(f"{new_list[index]} was created")
                return new_list[index]

            if new_list[index] == old_list[index]:
                pass
            else:
                print(f"{old_list[index]} was deleted")
                return old_list[index]

    def if_updated(self):
        dfs_old = self.updated_blobs_obj.download_file \
            ("/home/ninosha/Desktop/crud_task/old_blobs")
        time.sleep(10)
        dfs_new = self.updated_blobs_obj.download_file \
            ("/home/ninosha/Desktop/crud_task/new_blobs")

        old_blobs_dir = os.listdir("/home/ninosha/Desktop/crud_task/old_blobs")
        new_blobs_dir = os.listdir("/home/ninosha/Desktop/crud_task/new_blobs")
        old_length = len(old_blobs_dir)
        new_length = len(new_blobs_dir)

        for file in :
            print(len(os.listdir("/home/ninosha/Desktop/crud_task/old_blobs")))



check = CheckOperations(updated_list)
print(check.if_updated())
        # for filename in dfs_old:
# def check_if_updated(self):
#     for filename in self.old_blobs_list:
#         blob_file = Blob(bucket.bucket, filename)
