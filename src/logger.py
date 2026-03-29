import pandas as pd
from datetime import datetime


def log_attention(score):
    data = {
        "timestamp": [datetime.now()],
        "class_attention": [score]
    }

    df = pd.DataFrame(data)

    try:
        old = pd.read_csv("attention_log.csv")
        df = pd.concat([old, df], ignore_index=True)
    except FileNotFoundError:
        pass

    df.to_csv("attention_log.csv", index=False)