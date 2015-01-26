import os

def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % (var_name,)

API_KEY = get_env_variable('API_KEY')
API_SECRET = get_env_variable('API_SECRET')

API_TOKEN = get_env_variable('API_TOKEN')
API_SECRET_TOKEN = get_env_variable('API_SECRET_TOKEN')
