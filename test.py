import requests
import json
from bs4 import BeautifulSoup

apiBase = "https://adarsha.dharma-treasure.org/api/kdbs/{name}/pbs?size=10&lastId={pbs}"
workBase = "https://adarsha.dharma-treasure.org/kdbs/{name}"


def testUrl(work, pbs):
    # check if url has text
    url = apiBase.format(name=work[0], pbs=pbs)
    response = requests.get(url)
    if response.text == '{"total":0,"data":[]}':
        # print(response.text)
        status = False
    else:
        status = True
    return status

def get_page_source(opf_path,work): 
    url = workBase.format(name=work[0])       
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find("script", {"data-reactid": "23"}).text.strip()[14:-1]
    results = json.loads(results)["sidebar"]["data"]
    
    with open(f"{opf_path}/raw.json","w") as f:
        f.write(json.dumps(results))


def load_json(opf_path):
    with open(f"{opf_path}/raw.json") as f:
        data = json.load(f)
    return data

def get_sidebar_data(cur_obj,work,parent_obj=None):
    obj_li=[]
    for index,obj in enumerate(cur_obj):
        if index < len(cur_obj) -1:
            obj["pbEnd"] = cur_obj[index+1]["PbId"]
        elif len(cur_obj) == 1 and parent_obj != None:
            obj["pbEnd"]=parent_obj["pbEnd"]
        elif index == len(cur_obj) -1 and parent_obj != None:
            obj["pbEnd"]=parent_obj["pbEnd"]
        elif parent_obj == None:
            obj["pbEnd"] = get_last_pbid(work,obj["PbId"])

        if "nodes" in obj:
            cur_li=get_sidebar_data(obj["nodes"],work,obj)
            
            cur_dic = {
            "id":obj["id"],
            "text":str(obj["text"]).replace('"','').replace("'",""),
            "bo":str(obj["bo"]).replace('"','').replace("'",""),
            "en":str(obj["en"]).replace('"','').replace("'",""),
            "zh-TW":obj["zh-TW"] if obj["zh-TW"] else "None",
            "zh-CN":obj["zh-CN"] if obj["zh-CN"] else "None",
            "KdbId":obj["KdbId"] if obj["KdbId"] else "None",
            "SutraId":obj["SutraId"] if obj["SutraId"] else "None",
            "pbStart":obj["PbId"],
            "pbEnd":obj["pbEnd"],
            "nodes":cur_li
            }
            obj_li.append(cur_dic)
        else:
            
            cur_di = {
            "id":obj["id"],
            "text":str(obj["text"]).replace('"','').replace("'",""),
            "bo":str(obj["bo"]).replace('"','').replace("'",""),
            "en":str(obj["en"]).replace('"','').replace("'",""),
            "zh-TW":obj["zh-TW"] if obj["zh-TW"] else "None",
            "zh-CN":obj["zh-CN"] if obj["zh-CN"] else "None",
            "KdbId":obj["KdbId"] if obj["KdbId"] else "None",
            "SutraId":obj["SutraId"] if obj["SutraId"] else "None",
            "pbStart":obj["PbId"],
            "pbEnd":obj["pbEnd"],
            }
            obj_li.append(cur_di)

    return obj_li

def get_last_pbid(work,pbid):
    i=pbid
    while testUrl(work,pbs=i):
        is_last = False if testUrl(work, i+10) else True
        if is_last:
            url = apiBase.format(name=work[0], pbs=i)
            response = requests.get(url).text
            response = json.loads(response)
            objs = response["data"]
            last_pbid = ""
            for obj in objs:
                last_pbid = obj["id"]

            return last_pbid                   

        i += 10


def start_work(opf_path,work):
    get_page_source(opf_path,work)
    results = load_json(opf_path)
    obj=get_sidebar_data(results,work)

    return obj  


if __name__ == "__main__":
    start_work()        