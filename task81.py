import datetime as dt

months = ["january", "february", "march", "april", "may", "june", "july",
          "august", "september", "october", "november", "december"]


class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def set_integer_date(cls, date_list):
        Date.validate(date_list)
        date_time_obj = dt.datetime.strptime(date_list, '%d %B %Y')
        date = (date_time_obj.day, date_time_obj.month, date_time_obj.year)
        return cls(date)

    @staticmethod
    def validate(date_list):
        if type(date_list) == str and len(date_list.split()) == 3:
            x = date_list.split()
            if int((x)[0]) in range(1, 32) and x[1] in months and int((x)[2]) > 0:
                return date_list
            else:
                raise ValueError("Дата должна быть в формате вида '01 january 1900'")
        else:
            raise ValueError("Дата должна быть в формате вида '01 january 1900'")


date_list = ("22 october 2021")
tomorrow = Date.set_integer_date(date_list)
print(tomorrow.date)

date_list_incorrect = ("222 october 2021")
tomorrow = Date.set_integer_date(date_list_incorrect)
