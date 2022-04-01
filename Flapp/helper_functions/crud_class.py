from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials
from Flapp.helper_functions.utils import jsonfile_to_dict


class CRUD:
    """
    class gets client and bucket user wants to work on, user chooses the
    file and can create, read, update and download it.
    """

    def __init__(self, credentials_url, project_name, bucket_name,
                 file_name, filepath):
        self.credentials_url = credentials_url
        self.project_name = project_name
        self.bucket_name = bucket_name
        self.file_name = file_name
        self.filepath = filepath

    @property
    def credentials(self):
        """
        :return: client credentials
        """
        credentials_dict = jsonfile_to_dict(self.credentials_url)
        return ServiceAccountCredentials. \
            from_json_keyfile_dict(credentials_dict)

    @property
    def client(self):
        """
        :return: gcp client
        """
        try:
            return storage.Client(credentials=self.credentials,
                                  project=self.project_name)
        except ConnectionError:
            raise ConnectionError

    @property
    def bucket(self):
        """
        :return: client bucket
        """
        try:
            return self.client.get_bucket(self.bucket_name)
        except Exception:
            raise "bucket not found"

    @property
    def blob(self):
        """
        :return: wanted file as a blob
        """
        try:
            return self.bucket.blob(self.file_name)
        except FileNotFoundError:
            raise FileNotFoundError

    def creat_file(self):
        """
        uploads downloaded file in gcp bucket
        """
        try:
            self.blob.upload_from_filename(self.filepath)
        except IOError:
            raise IOError

    def read_file(self):
        """
        reads wanted file from bucket and downloads to
        Downloads Directory
        """
        try:
            self.blob.download_to_filename(
                f"../crud_task/Downloads/{self.file_name}."
                f"{self.filepath[-3:]}"
            )
        except IOError:
            raise IOError

    def update_file(self):
        """
        updates wanted file, filename should be same as it was, deletes
        file and uploads changed file with same filename
        """
        try:
            bucket = self.blob.bucket
            bucket.delete_blob(self.file_name)
            self.blob.upload_from_filename(self.filepath)
        except IOError:
            raise IOError

    def delete_file(self):
        """
        deletes wanted file from wanted bucket
        """

        print(f"{self.file_name} file is deleting")
        bucket = self.bucket
        bucket.delete_blob(self.file_name)
