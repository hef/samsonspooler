from fabric.api import run, cd, prefix

def virtualenv(command):
    with cd(env.directory):
        run(env.activate + '&&' + command)

def bootstrap():
    with cd('/srv/'):
        run('git clone https://github.com/hef/samsonspooler.git')
    with cd('/srv/samsonspooler'):
        run('virtualenv --distribute venv')

def deploy():
    with cd('/srv/samsonspooler/'):
        run('git remote update')
        run('git merge origin/master')
        with prefix('source /srv/samsonspooler/venv/bin/activate'):
            run('pip install -r config/production/requirements.txt')
            run('./manage.py syncdb')
            run('./manage.py collectstatic --noinput')
