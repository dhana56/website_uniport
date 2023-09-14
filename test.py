import requests
import re
import multiprocessing
from bs4 import BeautifulSoup

def chain_crawl(html,x):
    """Function used for looping the chain tables in the PDB website.
    And retrieve the chain and uniport id of the chain
    :html: the html tags from beautifulsoup
    :x: int indicates chain column class in the pdb page
    :y: dictionary for getting value"""

    chain_dic = {}
    need = html.find_all('tr',{'id':f"macromolecule-entityId-{x}-rowDescription"})
    if len(need)!=0:
        chain = need[0].find('td',{'style':'width:200px;'}).text 
        uniport_1 = html.find_all("table", attrs={"id":f"table_macromolecule-protein-entityId-{x}"})
        uniport_2 = uniport_1[0].find_all(href=re.compile("https://www.uniprot.org/uniprot"))
        if len(uniport_2)!=0:
            uniport_id = uniport_2[0].text
        else:
            uniport_id = None
        print(chain,uniport_id)
        chain_dic[chain] = uniport_id
        return chain_dic
    else:
        return None
    
def sq(x,y):
    return x**y

if __name__ ==  "__main__":

        pageurls = r"https://www.rcsb.org/structure/"+"1mky"
        try:
            url = requests.get(pageurls)
        except requests.exceptions.RequestException as e:
            print("Connection ERROR")

        if url.status_code==200:   
            soup = BeautifulSoup(url.content, 'html.parser')
            const_v= soup
            with multiprocessing.Pool(processes=2) as pool:
                result = pool.starmap(chain_crawl, [(const_v, args) for args in [1,2,3,4,5]])
                # result = pool.starmap(sq, [(3, args) for args in [1,2,3,4,5]])
            print(result)
        else:
            print(url.status_code, "Error")
            pass



























