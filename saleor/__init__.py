#!/usr/bin/env python


def manage():
    import os
    import sys
    from django.core.management import execute_from_command_line

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stylish.settings")
    execute_from_command_line(sys.argv)
