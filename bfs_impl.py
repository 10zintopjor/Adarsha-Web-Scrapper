import requests
import json
from bs4 import BeautifulSoup
li=[]
import collections



def call_api():        
    pass
    """ url = "https://adarsha.dharma-treasure.org/kdbs/degekangyur"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    results = soup.find("script", {"data-reactid": "23"}).text.strip()[14:-1]
    results = json.loads(results)["sidebar"]["data"]

    with open("s.json","w") as f:
        f.write(json.dumps(results)) """


def load_json():
    with open("s.json") as f:
        data = json.load(f)
    return data

def bfs(cur_obj,next_obj,par_obj):
    new_obj = []
    for index,obj in enumerate(cur_obj,start=1):

        if "nodes" in obj:
            if index < len(cur_obj):
                obj["PbEnd"] = cur_obj[index]["PbId"]
            elif par_obj != None:                
                obj["PbEnd"] = par_obj["PbEnd"]
            else:
                obj["PbEnd"] = "Undefined"

            parent_list = []
            parent_dict = {}

            next_obj = obj["nodes"][index] if index < len(obj["nodes"]) else None
        
            cur_dict=bfs(obj["nodes"],next_obj,obj)
            

            parent_list.append({"span":{"start":obj["PbId"],"end":obj["PbEnd"]}})
            parent_list.append(cur_dict)

            print(obj["depth"])
            if par_obj == None:
                new_obj.append({obj["text"]:parent_list})
            else:
                parent_dict["nodes"] = {obj["text"]:parent_list}
                return parent_dict
            

            """ parent_dict = {}
            parent_list = []
            cur_dict={}
            next_obj = obj["nodes"][index] if index < len(obj["nodes"]) else None
            parent_list.append({"span":{"start":obj["PbId"],"end":obj["PbEnd"]}})
            cur_dict = bfs(obj["nodes"],next_obj,obj)  
            parent_list.append(cur_dict)
            parent_dict["nodes"] = {obj["text"]:parent_list} """

        else:
            dict = {}
            dict_in = {}
            if next_obj != None:
                dict_in["pbId_end"] = next_obj["PbId"]-1
            else:
                dict_in["pbId_end"] = par_obj["PbEnd"]

            dict_in["pbId_start"] = obj["PbId"]
            dict[obj["text"]] = dict_in
            return dict    

    return new_obj    
     


def start_work():
    li.clear
    #results = call_api()
    results = load_json()
    obj=bfs(results,None,None)
    #val = get_leaf_value(data,pbid)
    with open("notes.txt","w") as f:
            f.write(str(obj))

    
if __name__ == "__main__":
    start_work()
   