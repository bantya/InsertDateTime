import sublime
import sublime_plugin
import time

class InsertDateTimeCommand(sublime_plugin.TextCommand):
    def run(self, edit, **kwargs):
        self.edit = edit
        command = kwargs.get('command', None)

        if command == 'insert_date':
            self.insert_date()
        elif command == 'insert_time':
            self.insert_time()
        elif command == 'insert_datetime':
            self.insert_datetime()
        elif command == 'insert_plain_date':
            self.insert_plain_date()
        elif command == 'insert_plain_time':
            self.insert_plain_time()
        elif command == 'insert_plain_datetime':
            self.insert_plain_datetime()

    def insert_date(self):
        self.put_in("%d-%m-%Y")

    def insert_time(self):
        self.put_in("%I:%M:%S")

    def insert_datetime(self):
        self.put_in("%d-%m-%Y %I:%M:%S")

    def insert_plain_date(self):
        self.put_in("%d%m%Y")

    def insert_plain_time(self):
        self.put_in("%I%M%S")

    def insert_plain_datetime(self):
        self.put_in("%d%m%Y %I%M%S")


    def put_in(self, format):
        sel = self.view.sel();
        for s in sel:
            self.view.replace(self.edit, s, time.strftime(format))
