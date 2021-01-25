import copy
import json

import pandas as pd
import requests

BASE_URL = "http://3b2f6af5-8ca4-449e-a113-b0726fe8e6be.eastus.azurecontainer.io/score"
BODY = {
    "data": [
        {
            "Column1": None
        }
    ]
}

def update_request(x):
    new_body = copy.deepcopy(BODY)
    new_body["data"][0]["Column1"] = x["Date"]
    result = json.loads(json.loads(requests.post(url=BASE_URL, json=new_body).text))["forecast"][0]
    return result


data = pd.read_csv(filepath_or_buffer='../datasets/energy-test.csv',
                   names=['Date', 'TZ', 'City', 'Code', 'Load'])
predicted = data.apply(lambda x: update_request(x), axis=1)
data2 = pd.concat([data, predicted], axis=1)
data2.to_csv(path_or_buf='../datasets/energy-pred.csv', index=False)
