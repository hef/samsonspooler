SamsonSpooler
============

Samson Spooler is a 3d print queue for the makerbot replicator designed to run on a Raspberri Pi.


Bootstraping
------------

Use an appropriate python2 virtualenv for your platform.

    virtualenv venv
    . venv/bin/activate
    pip install -e git://github.com/makerbot/pyserial.git#egg=pyserial
    pip install -r requirements.txt

