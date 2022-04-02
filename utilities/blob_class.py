class Blob:
    """
    creates blob object
    """
    def __init__(self, bucket_obj,  file_name):
        """
        :param bucket_obj: bucket object from Bucket class
        :param file_name: str/file name
        """
        self._bucket_obj = bucket_obj
        self.file_name = file_name
        self.blob = self._bucket_obj.blob(self.file_name)
