# src/preprocessing.py
# وظیفه: محاسبه بازده روزانه طلا در بازه اطراف هر رویداد اقتصادی

import pandas as pd

def get_event_window_returns(gold, events, window=5):
    """
    محاسبه بازده طلا قبل و بعد از هر رویداد اقتصادی
    ورودی:
        gold: DataFrame قیمت طلا با ستون‌های ['date','open','high','low','close','return']
        events: DataFrame رویدادها با ستون‌های ['date','event','type']
        window: تعداد روز قبل و بعد رویداد برای محاسبه بازده
    خروجی:
        DataFrame شامل بازده‌ها به همراه نوع رویداد و روز نسبت به رویداد
    """
    results = []

    # اطمینان از lowercase بودن ستون‌ها
    gold = gold.copy()
    gold["date"] = pd.to_datetime(gold["date"])
    gold = gold.set_index("date")

    events = events.copy()
    events["date"] = pd.to_datetime(events["date"])

    for _, row in events.iterrows():
        event_date = row["date"]
        event_type = row["type"]

        for i in range(-window, window + 1):
            day = event_date + pd.Timedelta(days=i)
            if day in gold.index:
                results.append({
                    "date": day,
                    "event_date": event_date,
                    "type": event_type,
                    "day_relative": i,
                    "return": gold.loc[day]["return"]  # lowercase
                })

    return pd.DataFrame(results)

