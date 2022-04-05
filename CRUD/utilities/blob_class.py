class Blob:
    """
    creates blob object
    """

    def __init__(self, bucket_obj):
        """
        :param bucket_obj: bucket object from Bucket class
        """
        self.bucket_obj = bucket_obj

    def get_blob(self, file_name):
        return self.bucket_obj.blob(file_name)
