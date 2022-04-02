from utilities.client_class import CreateClient
from utilities.blob_class import Blob
from utilities.bucket_task import Bucket
from utilities.crud_class import CRUDFuncs
import os


class CRUD:
    """
    class connects client, bucket, blob, and crud classes
    """
    def __init__(self, credentials_url, project_name,
                 bucket_name, file_name=None):
        """
        :param credentials_url: credentials path/str
        :param project_name: str/project name
        :param bucket_name: str/bucket name
        :param file_name: str/filename
        """
        self.project_name = project_name
        self.bucket_name = bucket_name
        self.file_name = file_name
        self.credentials_url = credentials_url
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_url

    @property
    def crud_obj(self):
        """
        function passes wraps up parameters to initialize crud object
        :return: crud object from CRUDFuncs class
        """

        try:
            client_created = CreateClient(self.credentials_url,
                                          self.project_name)
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = \
                self.credentials_url
            client = client_created.client
        except NotImplementedError as f:
            raise NotImplementedError(f)

        bucket = Bucket(bucket_name=self.bucket_name, client_obj=client)
        bucket = bucket.bucket

        blob_file = Blob(bucket_obj=bucket, file_name=self.file_name)

        crud_obj = CRUDFuncs(blob_file)

        return crud_obj