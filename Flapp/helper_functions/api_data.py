from Flapp.helper_functions.crud_class import CRUD


def get_api_data(request):
    """
    function gets requested form data from api and passes needed
    parameters to CRUD class object
    :param request: flask module request
    :return: CRUD class object
    """
    try:
        bucket_name = request.form["bucket_name"]
        credentials_file = request.files["credentials_file"]
        file_name = request.form["file_name"]
        file_to_upload = request.files["file_to_upload"]
        project_name = request.form["project_name"]

        credentials_url = f"Credentials/{credentials_file.filename}"
        file_url = f"Data/{file_to_upload.filename}"

        try:
            credentials_file.save(credentials_url)
            file_to_upload.save(file_url)

        except KeyError:
            raise KeyError

        except FileNotFoundError:
            raise FileNotFoundError

    except ConnectionError:
        raise ConnectionError

    crud_obj = CRUD(credentials_url=credentials_url,
                    project_name=project_name,
                    bucket_name=bucket_name,
                    file_name=file_name,
                    filepath=file_url)

    return crud_obj
