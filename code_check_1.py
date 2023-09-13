import requests
import re
from bs4 import BeautifulSoup

def scrappy_fun(array):
    """Function used to retrieve the chain name : uniport for a given PDB id
    : array, will take the list of array of pdb_list
    """
    dic_1 ={}
    patern = re.compile(r'\w+')
    array_1= re.findall( patern, array[0])

    for i,r in enumerate(array_1):
        pageurls = r"https://www.rcsb.org/structure/"+r[:4]
        try:
            url = requests.get(pageurls)

        except requests.exceptions.RequestException as e:
            print("Connection ERROR")
            break
        
        if url.status_code==200:   
            soup = BeautifulSoup(url.content, 'html.parser')
            chain_dic = {}
            for i in range(1,5):
                need= soup.find_all('tr',{'id':f"macromolecule-entityId-{i}-rowDescription"})
                if len(need)!=0:
                    chain = need[0].find('td',{'style':'width:200px;'}).text 
                    uniport_1 = soup.find_all("table", attrs={"id":f"table_macromolecule-protein-entityId-{i}"})
                    uniport_2= uniport_1[0].find_all(href= re.compile("https://www.uniprot.org/uniprot"))
                    if len(uniport_2)!=0:
                        uniport_id= uniport_2[0].text
                    else:
                        uniport_id=None
                    print(chain,uniport_id)
                    chain_dic[chain] =uniport_id
                    dic_1[r.lower()] =chain_dic
                else:
                    pass
        else:
            print(url.status_code, "Error")
            pass
        
    return dic_1























