import requests
import re
import threading
from bs4 import BeautifulSoup


def chain_crawl(html,x,y,r):
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
        chain_dic[chain] = uniport_id
        y[r] =chain_dic
    else:
        return None

def uni_id(array):
    """Function for retrieving uniport ids.
    :array: takes array of PDB ids
    """
    patern = re.compile(r'\w+')
    array_1= re.findall( patern, array[0])
    dic_1 = {}

    for k,l in enumerate(array_1):
        pageurls = r"https://www.rcsb.org/structure/"+l[:4]
        try:
            url = requests.get(pageurls)
        except requests.exceptions.RequestException as e:
            print("Connection ERROR")
        if url.status_code==200:   
            soup = BeautifulSoup(url.content, 'html.parser')
            const_v= soup
            threds= []
            for i in range(5):
                thred= threading.Thread(target=chain_crawl, args=(const_v,i,dic_1,l[:4]))
                threds.append(thred)
                thred.start()
            for j in threds:
                thred.join()
        else:
            print(url.status_code, "Error")
            pass

    return dic_1
    


    
        
  









