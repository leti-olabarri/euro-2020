import requests
import pandas as pd

def all_matches():
    res = requests.get("http://localhost:3500/matches").json()
    res = res["matches"]
    df = pd.DataFrame(res)
    return df