#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from os import path
from dotenv import dotenv_values


def load_django_dotenv():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gateway.config")
    os.environ.setdefault("DJANGO_CONFIGURATION", "Local")

    dotenv_path = ('.env.%(DJANGO_CONFIGURATION)s' % os.environ).lower()

    if not path.isfile(dotenv_path):
        dotenv_path = '.env'

    os.environ.update(dotenv_values(dotenv_path))

    return os.environ


def main():
    load_django_dotenv()

    try:
        from configurations.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django  # noqa
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
