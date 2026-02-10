
#وظیفه: محاسبه جدول مقایسه اثر اخبار # src/analysis.py
import pandas as pd
import numpy as np
from src.preprocessing import get_event_window_returns

def event_summary_tabel(gold,events,window=5):
    event_type=events["type"].unique()
    summary=[]

    for et in event_type:
        temp=[]
        for date in events[events["type"] == et]["date"]:
            window_df = get_event_window_returns(gold, events, window)
            temp.append(window_df["return"].values)
        arr = np.array(temp)
        mean_before = arr[:, :window].mean()
        mean_event = arr[:, window].mean()
        mean_after = arr[:, window + 1:].mean()
        summary.append({
            "Event_Type": et,
            "Mean_Return_Before": mean_before,
            "Mean_Return_On_Event": mean_event,
            "Mean_Return_After": mean_after
        })

    summary_df = pd.DataFrame(summary)
    return summary_df