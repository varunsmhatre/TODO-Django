#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "todo_app.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    # if sys.argv[-1] == 'runserver':
    #     scheduler = BackgroundScheduler()
    #     scheduler.start()

    #     trigger = CronTrigger(
    #         year="*", month="*", day="*", hour="*", minute="*", second="5"
    #     )
    #     scheduler.add_job(
    #         foo,
    #         trigger=trigger,
    #         name="daily foo",
    #     )
    main()
