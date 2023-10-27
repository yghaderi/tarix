from collections import namedtuple
import datetime
import jdatetime


def _translate_dastr(dtstr: str):
    dtstr = dtstr.translate(str.maketrans("", "", "-/"))
    if not isinstance(int(dtstr), int):
        raise ValueError(
            f'Invalid format string: {dtstr!r}. Format must be like "yyyymmdd", "yyyy-mm-dd", '
            f'"yyyy/mm/dd"'
        )
    return dtstr


def _parse_format_date(dtstr: str):
    dtstr = _translate_dastr(dtstr)
    Date_ = namedtuple("Date", ["year", "month", "day"])
    return Date_(year=int(dtstr[0:4]), month=int(dtstr[4:6]), day=int(dtstr[6:8]))


class Date:
    """
    .. raw:: html

        <div dir="rtl">
        رشته‌یِ تاریخِ جلالی رو به فرمتِ تاریخ جلالی و میلادی درمیاره.
        </div>

    Parameter
    ---------
    date_str: str, format "yyyymmdd", "yyyy-mm-dd", "yyyy/mm/dd"
        تاریخِ جلالی
    """

    def __init__(self, date_str: str):
        self.date_str = date_str

    @property
    def date_str(self):
        return self._date_str

    @date_str.setter
    def date_str(self, date_str):
        if not isinstance(date_str, str):
            raise TypeError("date_str: argument must be str")

        if len(_translate_dastr(date_str)) != 8:
            raise ValueError(
                f'Invalid format string: {date_str!r}. Format must be like  "yyyymmdd", "yyyy-mm-dd",'
                f' "yyyy/mm/dd"'
            )
        self._date_str = date_str

    def from_str(self):
        """
        .. raw:: html

            <div dir="rtl">
              رشته‌یِ تاریخِ جلالی رو به فرمتِ تاریخ جلالی درمیاره.
            </div>

        Returns
        -------
        jdatetime.date

        Examples
        --------
        >>> from tarix import Date
        >>> Date("1402-08-05").from_str()
        jdatetime.date(1402, 8, 5)
        """
        try:
            return jdatetime.date(*_parse_format_date(self._date_str))

        except Exception:
            raise ValueError(f"Invalid format string: {self._date_str!r}")

    def jalali_to_gregorian(self):
        """
        .. raw:: html

            <div dir="rtl">
              تاریخِ جلالی رو به میلادی تبدیل می‌کنه.
            </div>

        Returns
        -------
        datetime.date

        Examples
        --------
        >>> from tarix import Date
        >>> Date("1402-08-05").jalali_to_gregorian()
        datetime.date(2023, 10, 27)
        """
        jdate = self.from_str()
        return datetime.date(
            *jdatetime.JalaliToGregorian(
                jyear=jdate.year, jmonth=jdate.month, jday=jdate.day
            ).getGregorianList()
        )
