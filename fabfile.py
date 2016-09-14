#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import random
from fabric.api import *
from fabric.colors import white, red
from fabric.contrib.files import upload_template
from fabric.contrib.files import exists

from settings import USER, PASS
from settings import HOSTS, DOMAIN, SUBDOMAIN

REPO = 'https://github.com/mitrofun/kids2'
PROJECT_NAME = 'kids2'
PROJECTS_DIR = 'projects'
PROJECT_DIR = 'projects/{project}'.format(project=PROJECT_NAME)
env.hosts = HOSTS
ENV_PATH = '~/.env'


def get_rand_str(length=16):
    return ''.join(
        [random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789')
         for i in range(length)])


@task
def pull():
    with cd(PROJECT_DIR):
        run('git pull origin master')


@task
def mk_dirs():
    run('mkdir -p projects')
    run('mkdir -p logs')
    run('mkdir -p logs/{project}'.format(project=PROJECT_NAME))
    run('mkdir -p .env')


@task
def create_env():
    try:
        run('virtualenv --no-site-packages -p python3.4 {env}/{project}'.
            format(env=ENV_PATH, project=PROJECT_NAME))
    except:
        print(red('environment already have!'))


@task
def clone_project():
    with cd(PROJECTS_DIR):
        try:
            run('git clone {repo}'.format(repo=REPO))
        except:
            print(red('dir {} already have, del dir and clone again'.
                      format(PROJECT_NAME)))
            run('rm -rf {project}'.format(project=PROJECT_NAME))
            run('git clone {repo}'.format(repo=REPO))


@task
def pip():
    with cd(PROJECT_DIR):
        run('{env}/{project}/bin/pip install -r requirements.txt'.
            format(env=ENV_PATH, project=PROJECT_NAME))


@task
def collectstatic():
    with cd(PROJECT_DIR):
        run('{env}/{project}/bin/python manage.py collectstatic --noinput'.
            format(env=ENV_PATH, project=PROJECT_NAME))
    print(white('Static was collected'))


@task
def createsuperuser():
    with cd(PROJECT_DIR):
        run('{env}/{project}/bin/python manage.py createsuperuser'.
            format(env=ENV_PATH, project=PROJECT_NAME))


def _run_as_pg(command):
    return sudo('sudo -u postgres {command}'.format(command=command))


@task
def pg_drop_database(db):
    try:
        _run_as_pg('psql -d postgres -c "DROP DATABASE {db};"'.format(db=db))
    except:
        print(white('nothing drop'))


@task
def pg_drop_user(username):
    try:
        _run_as_pg('psql -d postgres -c "DROP USER {user};"'.
                   format(user=username))
    except:
        print(white('nothing drop'))


def pg_create_user(username, password):
    _run_as_pg('psql -d postgres -c '
               '"CREATE USER {user} WITH PASSWORD \'{pas}\'"'.
               format(user=username, pas=password))
    print(white('psql -d postgres -c '
                '"CREATE USER {user} WITH PASSWORD \'{pas}\'"'.
                format(user=username, pas=password)))


def pg_create_database(database, owner):
    _run_as_pg('psql -d postgres -c '
               '"CREATE DATABASE {db} WITH OWNER={owner} ENCODING=\'utf-8\';"'.
               format(db=database, owner=owner))


def pg_user_exists(username=PROJECT_NAME):
    with settings(hide('running', 'stdout', 'stderr', 'warnings'),
                  warn_only=True):
        res = _run_as_pg('''psql -t -A -c "SELECT COUNT(*)
        FROM pg_user WHERE usename = '%(username)s';"''' % locals())
    return res == "1"


def pg_database_exists(database):
    with settings(hide('running', 'stdout', 'stderr', 'warnings'),
                  warn_only=True):
        res = _run_as_pg(
            '''psql -t -A -c "SELECT COUNT(*)
            FROM pg_database WHERE datname = '%(database)s';"''' % locals())
    return res == "1"


@task
def configure_postgres():
    if not pg_user_exists(env.pg_user):
        pg_create_user(env.pg_user, env.pg_password)
    if not pg_database_exists(env.pg_database):
        pg_create_database(env.pg_database, env.pg_user)


@task
def local_settings():
    context = {
        'pg_user': env.pg_user,
        'pg_password': env.pg_password,
        'pg_database': env.pg_database,
        'secret_key': get_rand_str(32),
        'token': env.token,
        'user': env.user,
        'project': PROJECT_NAME,
    }

    # Creating settings local.py
    upload_template('conf/templates/settings.template',
                    '{project_dir}/src/settings/local.py'.
                    format(project_dir=PROJECT_DIR),
                    context, use_jinja=True)


@task
def migrate_db(actions='migrate'):
    with cd(PROJECT_DIR):
        run('{env}/{project}/bin/python manage.py migrate'.
            format(env=ENV_PATH, project=PROJECT_NAME))
    print(white('db was migrated'))


@task
def fill_dictionaries():
    with cd(PROJECT_DIR):
        run('{env}/{project}/bin/python manage.py filldicts --fill'.
            format(env=ENV_PATH, project=PROJECT_NAME))
    print(white('fill dictionaries'))


@task
def fill_breadcrumbs():
    with cd(PROJECT_DIR):
        run('{env}/{project}/bin/python manage.py sitetree_resync_apps'.
            format(env=ENV_PATH, project=PROJECT_NAME))
    print(white('fill breadcrumbs'))


@task
def supervisor_conf():
    context = {
        'user': env.user,
        'project': PROJECT_NAME,

    }

    upload_template('conf/templates/supervisor.template',
                    '{project_dir}/conf/supervisor/{project}.conf'.
                    format(project=PROJECT_NAME, project_dir=PROJECT_DIR),
                    context, use_jinja=True)


@task
def gunicorn_conf():
    context = {
        'user': env.user,
        'project': PROJECT_NAME,

    }

    upload_template('conf/templates/run.template',
                    '{project_dir}/run/run.sh'.
                    format(project_dir=PROJECT_DIR),
                    context, use_jinja=True)


@task
def nginx_conf():
    context = {
        'user': env.user,
        'project': PROJECT_NAME,

    }

    upload_template('conf/templates/nginx.template',
                    '{project_dir}/conf/nginx/{project}.conf'.
                    format(project=PROJECT_NAME, project_dir=PROJECT_DIR),
                    context, use_jinja=True)


@task
def create_conf():
    context = {
        'user': env.user,
        'project': PROJECT_NAME,
    }

    supervisor_dir = '{project_dir}/conf/supervisor'. \
        format(project_dir=PROJECT_DIR)
    run_dir = '{project_dir}/run'.format(project_dir=PROJECT_DIR)
    nginx_dir = '{project_dir}/conf/nginx'.format(project_dir=PROJECT_DIR)

    dirs = [supervisor_dir, run_dir, nginx_dir]

    for cdir in dirs:
        if not exists(cdir):
            run('mkdir {dir}'.format(dir=cdir))

    upload_template('conf/templates/supervisor.template',
                    '{project_dir}/conf/supervisor/{project}.conf'.
                    format(project=PROJECT_NAME, project_dir=PROJECT_DIR),
                    context, use_jinja=True)

    upload_template('conf/templates/run.template',
                    '{project_dir}/run/run.sh'.
                    format(project_dir=PROJECT_DIR),
                    context, use_jinja=True)

    upload_template('conf/templates/nginx.template',
                    '{project_dir}/conf/nginx/{project}.conf'.
                    format(project=PROJECT_NAME, project_dir=PROJECT_DIR),
                    context, use_jinja=True)


@task
def link_conf():
    supervisor_link = '/etc/supervisor/conf.d/{project}.conf'. \
        format(project=PROJECT_NAME)

    nginx_link = '/etc/nginx/sites-enabled/{project}.conf'. \
        format(project=PROJECT_NAME)

    if exists(supervisor_link, use_sudo=True):
        sudo('rm {file}'.format(file=supervisor_link))

    sudo('ln -s /home/{user}/{project_dir}/conf/supervisor/{project}.conf '
         '/etc/supervisor/conf.d/{project}.conf'.
         format(project=PROJECT_NAME, project_dir=PROJECT_DIR, user=env.user))

    if exists(nginx_link, use_sudo=True):
        sudo('rm {file}'.format(file=nginx_link))

    sudo('ln -s /home/{user}/{project_dir}/conf/nginx/{project}.conf '
         '/etc/nginx/sites-enabled/{project}.conf'.
         format(project=PROJECT_NAME, project_dir=PROJECT_DIR, user=env.user))

    sudo('supervisorctl update')
    sudo('nginx -s reload')


@task
def restart():
    sudo('supervisorctl update')
    sudo('killall gunicorn')
    sudo('nginx -s reload')


@task
def link_log():
    with cd('/home/{user}/logs/{project}'.format(user=env.user,
                                                 project=PROJECT_NAME)):
        run('ln -s /var/log/nginx/{name}-error.log nginx-error.log'.
            format(name=PROJECT_NAME))
        run('ln -s /var/log/nginx/{name}-access.log nginx-access.log'.
            format(name=PROJECT_NAME))
        run('ln -s /var/log/postgresql/postgresql-9.3-main.log postgresql.log')


@task
def install_bower():
    sudo('apt-get install nodejs -y')
    sudo('apt-get install npm -y')
    sudo('npm install -g bower')
    sudo('ln -s /usr/bin/nodejs /usr/bin/node')


def bower_install():
    with cd(env.root):
        try:
            run('bower i')
        except:
            install_bower()
            run('bower i')


@task
def deploy(user=USER, pas=PASS):
    """
    Развертываение на сервер с уже установленными системными библиотеками, СУБД
    без первоначальной настройки и установки
    :param user: Пользователь
    :param pas: Пароль пользователя
    :return: Развернутое приложения на сервере
    """
    env.user = user
    env.project = PROJECT_NAME
    env.password = pas
    env.pg_user = 'user_{project}'.format(project=PROJECT_NAME)
    env.pg_password = pas
    env.pg_database = 'db_{project}'.format(project=PROJECT_NAME)
    env.token = get_rand_str(32)
    mk_dirs()
    create_env()
    clone_project()
    pip()
    configure_postgres()
    local_settings()
    migrate_db()
    create_conf()
    collectstatic()
    link_conf()
    link_log()
    createsuperuser()
    fill_dictionaries()
    fill_breadcrumbs()
    bower_install()
    with cd(env.root):
        run('npm i')
        run('bundle install')
        run('node_modules/gulp/bin/gulp.js build')
