import csv
import json
import os


def jsonfile_to_dict(url):
    """
    :param url: str/url of a json file
    :return: dictionary
    """
    with open(url) as file:
        file = file.read()
        to_dict = json.loads(file)
    return to_dict


def logs_csv(data):
    path = "/home/ninosha/Desktop/crud_task/listener_data/logs.csv"

    with open(path, 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        columns = ["file", "time", "status"]
        if os.stat(path).st_size != 0:
            print(os.stat(path).st_size)
            writer.writerow(data)
        else:
            writer.writerow(columns)
            writer.writerow(data)



