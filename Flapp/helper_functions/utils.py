import json


def jsonfile_to_dict(url):
    """
    :param url: str/url of a json file
    :return: dictionary
    """
    try:
        with open(url) as file:
            file = file.read()
            to_dict = json.loads(file)
        return to_dict
    except FileNotFoundError:
        raise FileNotFoundError
