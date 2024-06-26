

import time
from typing import Any
from django.core.management import BaseCommand
from psycopg import OperationalError
from django.db.utils import OperationalError as DjError

class Command(BaseCommand):
    def handle(self, *args: Any, **options) :
        self.stdout.write("Check db")
        up =False

        while up is False:
            try:
                self.check(databases=['default'])
                up=True
            except(OperationalError,DjError):
                self.stdout.write("Db has error")
            time.sleep(2)
        self.stdout.write("Db loaded")