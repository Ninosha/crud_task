from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials
from CRUD.utilities.utils import jsonfile_to_dict
import os


class CreateClient:
    """
    creates client object with credentials
    """

    def __init__(self, url, project_name):
        """
        :param url: credentials path/str
        :param project_name: str/project name
        """

        self.url = url
        self.project_name = project_name
        self._credentials = None
        self.client = storage.Client(credentials=self._credentials,
                                     project=self.project_name)

    def get_credentials(self):

        """
        gets credentials in json and returns as a dictionary
        :return: dictionary
        """
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.url
        try:
            credentials_dict = jsonfile_to_dict(self.url)
            self._credentials = ServiceAccountCredentials. \
                from_json_keyfile_dict(credentials_dict)
            return credentials_dict
        except Exception as f:
            raise ConnectionError(f)

        except NotImplementedError as f:
            raise NotImplementedError(f)

# client = CreateClient("/home/ninosha/Desktop/crud_task/Credentials/" \
#               "fair-solution-345912-e1b814ef61f8.json",
#                       "My First Project")
#
