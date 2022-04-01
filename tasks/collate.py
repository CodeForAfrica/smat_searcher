# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.7
# ---

# %% tags=["soorgeon-imports"]
import pandas as pd
from datetime import datetime as dt
from pathlib import Path
import pickle
from exported import search_results, collate_results, main

# %% tags=["parameters"]
upstream = ['load-']
product = None

# %% tags=["soorgeon-unpickle"]
params = pickle.loads(Path(upstream['load-']['params']).read_bytes())
url = pickle.loads(Path(upstream['load-']['url']).read_bytes())


# %% [markdown]
# ## Collate

# %%
def collate_results(results):
    data = []
    for item in results:
        d={}
        try:
            #  Channel Title
            d["Channel"] = item['_source']['channeltitle']
            #  Channel description 
            d["desc"] = item['_source']['channelabout'] 
            # Channel UserName
            d["UserName"] = item['_source']['channelusername']
             #   Resulting Message
            d["msg"] = item['_source']['message']
            #   channel url
            d["c_URL"] = item['_source']['entities'][0]['url']
        except:
            pass
            #   collect data in a list
        data.append(d)
    # store data in a dataframe
    frame = pd.DataFrame(data)
    
    return frame 

def main(args,kwargs):
    results = search_results(args,kwargs)
    frame = collate_results(results)
    today = str(dt.today().date())
    frame.to_csv(today + '_search_results.csv')
    return frame


# %%
main(url,params)
