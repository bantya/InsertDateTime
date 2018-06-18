import sublime
import sublime_plugin
import time

class InsertDateTimeCommand(sublime_plugin.TextCommand):

    DEFAULT_DATE_FORMAT = "%d-%m-%Y"
    DEFAULT_TIME_FORMAT = "%I:%M:%S"
    DEFAULT_DATETIME_FORMAT = "%d-%m-%Y %I:%M:%S"
    DEFAULT_PLAIN_DATE_FORMAT = "%d%m%Y"
    DEFAULT_PLAIN_TIME_FORMAT = "%I%M%S"
    DEFAULT_PLAIN_DATETIME_FORMAT = "%d%m%Y %I%M%S"

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
        self.put_in(
            self.get_font_settings('date_format', self.DEFAULT_DATE_FORMAT)
        )

    def insert_time(self):
        self.put_in(
            self.get_font_settings('time_format', self.DEFAULT_TIME_FORMAT)
        )

    def insert_datetime(self):
        self.put_in(
            self.get_font_settings('datetime_format', self.DEFAULT_DATETIME_FORMAT)
        )

    def insert_plain_date(self):
        self.put_in(
            self.get_font_settings('plain_date_format', self.DEFAULT_PLAIN_DATE_FORMAT)
        )

    def insert_plain_time(self):
        self.put_in(
            self.get_font_settings('plain_time_format', self.DEFAULT_PLAIN_TIME_FORMAT)
        )

    def insert_plain_datetime(self):
        self.put_in(
            self.get_font_settings('plain_datetime_format', self.DEFAULT_PLAIN_DATETIME_FORMAT)
        )

    def put_in(self, format):
        sel = self.view.sel();
        for s in sel:
            self.view.replace(self.edit, s, time.strftime(format))

    def get_font_settings(self, setting, default):
        return sublime.load_settings('InsertDateTime.sublime-settings').get(setting, default)
