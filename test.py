from utilities.CRUD import CRUD

credentials = "/home/ninosha/Desktop/crud_task/Credentials/" \
              "fair-solution-345912-e1b814ef61f8.json"
project_name = "My First Project"
bucket_name = "crudtask"
file_name = "axali.csv"

obj = CRUD(credentials_url=credentials,
           project_name=project_name,
           bucket_name=bucket_name,
           file_name=file_name)

file_path_create = "/home/ninosha/Desktop/crud_task/Data/" \
                   "email-password-recovery-code.csv"


print(obj.crud_obj.creat_file(file_path_create))

