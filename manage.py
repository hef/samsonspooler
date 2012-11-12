#!/usr/bin/env python
import os
import sys
from socket import gethostname

if __name__ == "__main__":
    if "li362-124" == gethostname():
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.production.settings")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.development.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
