import pandas as pd
import requests


def search_results(args,kwargs):
    response = requests.get(args,
                            kwargs)
    c = response.json()
    search_results = c['hits']['hits']
    return search_results

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
    frame.to_csv('data/search_results.csv')
    return frame