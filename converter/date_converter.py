from werkzeug.routing import BaseConverter
from datetime import datetime, date

class DateConverter(BaseConverter):
    def to_python(self, value):
        date_value = datetime.strptime(value, "%Y-%m-%d")
        return date_value