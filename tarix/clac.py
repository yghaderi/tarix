import datetime
from dateutil.relativedelta import relativedelta
from tarix.date import Date


def count_days(end: str, start: str | None = None):
    """
    .. raw:: html

        <div dir="rtl">
         تعداد روزهایِ بین تاریخ جلالیِ ابتدا و انتها رو محاسبه می‌کنه.
        </div>

    .. note::
        .. raw:: html

            <div dir="rtl">
            اگه تاریخِ ابتدا داده نشه، پیش-فرض
            <span style="color:#831843">امروزه</span>
             .
            </div>

    Parameters
    ----------
    end: str , format "yyyymmdd", "yyyy-mm-dd", "yyyy/mm/dd"
        تاریخِ انتها
    start: str , format "yyyymmdd", "yyyy-mm-dd", "yyyy/mm/dd"
        تاریخِ ابتدا




    Returns
    -------
    int

    Examples
    --------
    >>> from tarix import count_days
    >>> count_days(end='1402-08-06', start='1402-05-25')
    73
    """
    if start:
        return (
                Date(end).jalali_to_gregorian() - Date(start).jalali_to_gregorian()
        ).days
    return (Date(end).jalali_to_gregorian() - datetime.date.today()).days


def evenly_periods(length: int, end: str, start: str | None = None):
    """
    .. raw:: html

        <div dir="rtl">
             تعداد‌ِ دوره‌هایِ length-ماهه و باقیمانده-بر حسبِ length * 30- رو بهت می‌ده.
        </div>

    .. note::
        .. raw:: html

            <div dir="rtl">
            اگه تاریخِ ابتدا داده نشه، پیش-فرض
            <span style="color:#831843">امروزه</span>
             .
            </div>

    Parameters
    ----------
    length: int , > 0
        تعدادِ ماه
    end: str , format "yyyymmdd", "yyyy-mm-dd", "yyyy/mm/dd"
        تاریخِ انتها
    start: str , format "yyyymmdd", "yyyy-mm-dd", "yyyy/mm/dd"
        تاریخِ ابتدا

    Returns
    -------
    (int, float)

    Examples
    --------
    >>> from tarix import evenly_periods
    >>> evenly_periods(length=8, end='1373-05-25', start='1402-05-25')
    (43, 0.5083333333333333)
    """
    date = sorted(
        (
            Date(end).jalali_to_gregorian(),
            Date(start).jalali_to_gregorian() if start else datetime.date.today(),
        )
    )
    if length > 0:
        start = date[0]
        end = date[1]
        floor_division = 0
        while start <= end + relativedelta(months=-length):
            end += relativedelta(months=-length)
            floor_division += 1
        modulo = (end - start).days / (length * 30)
        return int(floor_division), modulo
    raise ValueError("Length must be greater than 0.")
