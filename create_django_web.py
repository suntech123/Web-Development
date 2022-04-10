## Read the documentation - https://cookiecutter-django.readthedocs.io/en/latest/
from cookiecutter.main import cookiecutter
from datetime import datetime

#extra_context={'project_name': 'TheGreatest'}
sun_web_config = {'project_name':'sunproject',\
 'description':'SunTech Web App Idea',\
 'author_name': 'Sunil Kumar Behl',\
 'email' : 'skumarbehl@gmail.com',\
 'open_source_license':'MIT',\
 'timestamp': datetime.utcnow().isoformat(),\
 'windows':'y',\
 'use_pycharm':'y',\
 'use_docker':'y',\
 'postgresql_version':14.1,\
 'cloud_provider':None,\
 'mail_service':'mailjet',\
 'use_async':'y',\
 'use_drf':'y',\
 'frontend_pipeline':None,\
 'use_celery':'n',\
 'use_mailhog':'y',\
 'use_sentry':'y',\
 'use_whitenoise':'n',\
 'use_heroku':'y',\
 'ci_tool':'Github',\
 'keep_local_envs_in_vcs':'y',\
 'debug':'n'
 }

def run_cookiecutter():
    template = 'gh:cookiecutter/cookiecutter-django'
    project_dir = cookiecutter(template, no_input=True, extra_context = sun_web_config)
    print(f'Project generated in { project_dir }' )

if __name__ == '__main__':
    run_cookiecutter()
