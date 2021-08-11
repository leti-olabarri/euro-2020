import requests
import pandas as pd
from config import API_URI

def all_matches():
    res = requests.get(API_URI + "/matches").json()
    res = res["matches"]
    df = pd.DataFrame(res)
    return df