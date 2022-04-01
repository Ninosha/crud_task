from Flapp import app
from flask import request
from Flapp.helper_functions.api_data import get_api_data


@app.route("/create", methods=['POST'])
def create():
    """
    function gets crud object from function get_api_data, calls function
    that creates file
    """

    crud_obj = get_api_data(request)
    crud_obj.creat_file()
    return "file created"


@app.route("/read", methods=['GET'])
def read_file():
    """
    function gets crud object from function get_api_data, calls function
    that reads file
     """

    crud_obj = get_api_data(request)
    crud_obj.read_file()
    return "file read"


@app.route("/update", methods=['PUT'])
def update_file():
    """
    function gets crud object from function get_api_data, calls function
    that creates file
    """

    crud_obj = get_api_data(request)
    crud_obj.update_file()
    return "file updated"


@app.route("/delete", methods=['DELETE'])
def delete_file():
    """
    function gets crud object from function get_api_data, calls function
    that creates file
    """

    crud_obj = get_api_data(request)
    crud_obj.delete_file()
    return "file deleted"

