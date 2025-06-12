from datetime import datetime, timedelta
import pytz

# 1. 현재 시간 + 1시간 timedelta
def load_timedelta():
    kst = pytz.timezone('Asia/Seoul')
    now_kst = datetime.now(kst)
    one_hour_later = now_kst + timedelta(hours=1)
    return one_hour_later


# 2. 주중/주말 여부 계산
def calculate_weekday(date: datetime) -> int:
    if date.weekday() < 5:
        weekday = 1
    else:
        weekday = 0
    return weekday