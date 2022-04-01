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
import json
import requests
from exported import search_results, collate_results, main

# %% tags=["parameters"]
upstream = None
product = None


# %% [markdown]
# ## Search

# %%
def search_results(args,kwargs):
    response = requests.get(args,
                            kwargs)
    c = response.json()
    search_results = c['hits']['hits']
    return search_results
