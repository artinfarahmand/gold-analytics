import pandas as pd

def load_gold_prices(path):
    df = pd.read_csv(path, )
    df.columns = df.columns.str.lower()
    df = df.drop(columns=["unnamed: 0"], errors="ignore")
    df["date"] = pd.to_datetime(df["date"])

    return df
def load_events(path):
    df = pd.read_csv(path,)
    df.columns = df.columns.str.lower()
    df["date"] = pd.to_datetime(df["date"])

    return df
