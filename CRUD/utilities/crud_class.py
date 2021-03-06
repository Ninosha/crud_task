from datetime import datetime
from CRUD.utilities.utils import logs_csv


class CRUDFuncs:
    """
    class has functions to operate on blob, create file in bucket,
    read/download, update and delete
    """

    def __init__(self, blob_obj):
        """
        :param blob_obj: blob object instance
        """
        self.blob_obj = blob_obj

    def creat_file(self, file_name, file_path):
        """
        uploads file from file path to bucket

        :param file_name:
        :param file_path: str/file path
        :return: message if operation was successful, else - error
        """
        try:
            self.blob_obj.get_blob(file_name).upload_from_filename(
                file_path)
            time_now = datetime.now()
            data = [file_name,
                    "created",
                    str(time_now)]
            logs_csv(data)

        except FileNotFoundError as f:
            raise FileNotFoundError(f)

        except NotImplementedError as f:
            raise NotImplementedError(f)

    def read_file(self, file_name, path_to_download):
        """
        downloads requested file to passed path

        :param file_name:
        :param path_to_download: string url
        :return: message if operation was successful, else - error
        """
        try:
            self.blob_obj.get_blob(file_name). \
                download_to_filename(f"{path_to_download}/"
                                     f"{file_name}")
            time_now = datetime.now()
            data = [file_name,
                    "read",
                    str(time_now)]
            logs_csv(data)

        except FileNotFoundError as f:
            raise FileNotFoundError(f)

        except NotImplementedError as f:
            raise NotImplementedError(f)

    def update_file(self, file_name, filepath):
        """
        updates file from file path to bucket
        :param file_name:
        :param filepath: str/file path
        :return: message if operation was successful, else - error
        """
        try:
            bucket = self.blob_obj.bucket_obj
            bucket.delete_blob(file_name)
            self.blob_obj.get_blob(file_name).upload_from_filename(
                filepath)

            time_now = datetime.now()
            data = [file_name,
                    "updated",
                    str(time_now)]
            logs_csv(data)

        except FileNotFoundError as f:
            raise FileNotFoundError(f)

        except NotImplementedError as f:
            raise NotImplementedError(f)

    def delete_file(self, file_name):
        """
        deletes file with obj filename
        :return: message if operation was successful, else - error
        """

        bucket = self.blob_obj.bucket_obj
        bucket.delete_blob(file_name)
        time_now = datetime.now()
        data = [file_name,
                "deleted",
                str(time_now)]
        logs_csv(data)
