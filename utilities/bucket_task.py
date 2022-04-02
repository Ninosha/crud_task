class Bucket:
    """
    creates bucket object
    """
    def __init__(self, bucket_name, client_obj):
        """
        :param bucket_name: str/bucket name
        :param client_obj: Client class object
        """
        self._client_obj = client_obj
        self._bucket_name = bucket_name
        self.bucket = self._client_obj.get_bucket(self._bucket_name)



