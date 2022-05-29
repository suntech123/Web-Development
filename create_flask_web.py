## Read the documentation - https://cookiecutter-django.readthedocs.io/en/latest/
from cookiecutter.main import cookiecutter
from datetime import datetime

#extra_context={'project_name': 'TheGreatest'}
sun_web_config = { 'full_name': 'Sunil Kumar Behl',\
 'email' : 'skumarbehl@gmail.com',\
 'github_username' : 'suntech123',\
 'project_name':'sunproject',\
 'app_name' : 'webapp',\
 'project_short_description' : 'my flask project',\
 'use_pipenv' : 'n',\ 
 'python_version' : ,\
 'node_version' : ,\
 'use_heroku' : 'y',\
 }

def run_cookiecutter():
    template = 'gh:cookiecutter/cookiecutter-django'
    project_dir = cookiecutter(template, no_input=True, extra_context = sun_web_config)
    print(f'Project generated in { project_dir }' )

if __name__ == '__main__':
    run_cookiecutter()
