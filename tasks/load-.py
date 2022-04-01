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

from pathlib import Path
import pickle
from exported import search_results, collate_results, main

# %% tags=["parameters"]
upstream = None
product = None

# %% tags=["parameters"]
upstream = None

# %% [markdown] tags=[]
# # Keyword Search with SMAT API 

# %% [markdown] tags=[]
# ## Load 

# %%
url = "https://api.smat-app.com/content?"
key_terms = "(Russia, Russie, Russe, Ambassade de Russie, Moscou, Wagner) AND (République centrafricaine, centrafricaine, RCA, Centrafrique, Central African Republic, Bangui)"

# %%
site = "telegram"
start_date = "2022-03-01"
last_date = "2022-03-31"

# %%
params = {
    "term": key_terms, 
    "site": site, 
    "since": start_date, 
    "until": last_date ,
    "esquery":"true",
    "sortdesc":"false"
}

# %% tags=["soorgeon-pickle"]
Path(product['params']).parent.mkdir(exist_ok=True, parents=True)
Path(product['params']).write_bytes(pickle.dumps(params))

Path(product['url']).parent.mkdir(exist_ok=True, parents=True)
Path(product['url']).write_bytes(pickle.dumps(url))
