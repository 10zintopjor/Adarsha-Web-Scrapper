import requests
import json
from bs4 import BeautifulSoup
li=[]


def call_api():        
    url = "https://adarsha.dharma-treasure.org/kdbs/degekangyur"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    results = soup.find("script", {"data-reactid": "23"}).text.strip()[14:-1]
    results = json.loads(results)["sidebar"]["data"]

    with open("s.json","w") as f:
        f.write(json.dumps(results))


def get_leaf_value(results,pbid):
    val = None
    global li
    for n,result in enumerate(results):
        if "nodes" in result:
            val = get_leaf_value(result["nodes"],pbid)
            if val != None:
                li.append(result["text"])
                return val
        elif n<len(results)-1:
            if pbid >= result["PbId"] and pbid < results[n+1]["PbId"]:
                li.append(result["text"])
                return result["text"]
        elif n == len(results)-1:
            if pbid == result["PbId"]:
                li.append(result["text"])
                return result["text"]
        
    return val


def load_json():
    with open("s.json") as f:
        data = json.load(f)
    return data


def go_to_leaf(obj,next_obj,root_obj):

    if "nodes" in obj:
        parent_dict = {}
        parent_list = []
        cur_dict={}
        for index,node in enumerate(obj["nodes"],start=1):
            next_node = obj["nodes"][index] if index < len(obj["nodes"]) else None
            parent_list.append({"span":{"start":obj["PbId"],"end":"undefined"}})
            cur_dict = go_to_leaf(node,next_node,)   
            parent_list.append(cur_dict)
        parent_dict["nodes"] = {obj["text"]:parent_list}
        return parent_dict 
    else:
        dict = {}
        dict_in = {}
        if next_obj != None:
            dict_in["pbId_end"] = next_obj["PbId"]-1
        else:
            dict_in["pbId_end"] = "undefined"

        dict_in["pbId_start"] = obj["PbId"]
        dict[obj["text"]] = dict_in
        return dict       
    

def start_work():
    li.clear
    #results = call_api()
    results = load_json()
    for result in results:
        dict = go_to_leaf(result,None,None)
        with open("notes.txt","w") as f:
            f.write(str(dict))
        break
    #val = get_leaf_value(data,pbid)


if __name__ == "__main__":
    start_work()
   