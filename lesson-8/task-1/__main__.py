class Date:
    date_str = None

    def __init__(self, date_str):
        day, month, year = Date.validate_day_month_year(date_str)
        self. day = day
        self.year = year
        self.month = month

    @classmethod
    def get_day_month_year(cls, date_str):
        date = cls(date_str)
        return date.day, date.month, date.year

    @staticmethod
    def validate_day_month_year(date_str):
        day, month, year = list(map(int,  date_str.split('-')))
        if (day > 31 or day < 1):
            raise ValueError('Day must be from 1 to 31')

        if (month > 12 or month < 1):
            raise ValueError('Month must be from 1 to 12')

        if (year > 9999 or year < -9999):
            raise ValueError('Year must be from -9999 to 9999')

        return day, month, year


date = Date('1-12-2012')
print(date.get_day_month_year('1-12-2012'))
