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
        self.file_name = blob_obj.file_name

    def creat_file(self, file_path):
        """
        uploads file from file path to bucket

        :param file_path: str/file path
        :return: message if operation was successful, else - error
        """
        print(f"{self.file_name} is creating")
        try:
            self.blob_obj.blob.upload_from_filename(file_path)
            return f"{self.file_name} was created"

        except FileNotFoundError as f:
            raise FileNotFoundError(f)

        except NotImplementedError as f:
            raise NotImplementedError(f)

    def read_file(self, path_to_download):
        """
        downloads requested file to passed path

        :param path_to_download: string url
        :return: message if operation was successful, else - error
        """
        print(f"{self.file_name} read in process")
        try:
            self.blob_obj.blob. \
                download_to_filename(f"{path_to_download}/"
                                     f"{self.file_name}")

            return f"{self.file_name} is downloaded on" \
                   f" {path_to_download} "

        except FileNotFoundError as f:
            raise FileNotFoundError(f)

        except NotImplementedError as f:
            raise NotImplementedError(f)

    def update_file(self, filepath):
        """
        updates file from file path to bucket
        :param filepath: str/file path
        :return: message if operation was successful, else - error
        """
        print(f"{self.file_name} is updating")
        try:
            bucket = self.blob_obj.bucket
            bucket.delete_blob(self.file_name)
            self.blob_obj.blob.upload_from_filename(filepath)

            return f"{self.file_name} is updated"

        except FileNotFoundError as f:
            raise FileNotFoundError(f)

        except NotImplementedError as f:
            raise NotImplementedError(f)

    def delete_file(self):
        """
        deletes file with obj filename
        :return: message if operation was successful, else - error
        """

        print(f"{self.file_name} file is deleting")

        bucket = self.blob_obj.bucket
        bucket.delete_blob(self.file_name)

        return f"{self.file_name} file is deleted"
