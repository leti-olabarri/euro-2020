import requests
import pandas as pd
from config import API_URI

def all_matches():
    res = requests.get(f"{API_URI}/matches").json()
    res = res["matches"]
    df = pd.DataFrame(res)
    return df