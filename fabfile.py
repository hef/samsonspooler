from fabric.api import run, cd, prefix, sudo, env

env.hosts = ['arbitrarion.com']

def bootstrap():
    """creates app log media static venv directories"""
    with cd('/srv/www/spooler.arbitrarion.com'):
        run('mkdir -p static media log')
        run('virtualenv --distribute venv')
        run('git clone https://github.com/hef/samsonspooler.git app')

def deploy():
    with cd('/srv/www/spooler.arbitrarion.com'):
            with cd('app'):
                run('git remote update')
                run('git merge origin/master')
                with prefix('source ../venv/bin/activate'):
                    run('pip install -r config/production/requirements.txt')
                    run('./manage.py syncdb --settings=config.production.settings')
                    run('./manage.py collectstatic --noinput --settings=config.production.settings')
                    sudo('supervisorctl restart samsonspooler')
