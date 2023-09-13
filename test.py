import requests
import re
from bs4 import BeautifulSoup
 
with open (r"C:\Users\dhana\OneDrive\Desktop\thesis_work_final\prj501\Single_mutation\run_script\uniport_sadh\data\maindata.txt",'r')  as file:
    test_list= file.readlines()
# print(test_list)

for k,j in enumerate(test_list[:1]):
    pageurls = r"https://www.rcsb.org/structure/"+j[:4]
    print(pageurls)
    try:
        url = requests.get(pageurls)
        print(url.status_code)
        print(url.raise_for_status())

    except requests.exceptions.RequestException as e:
        print("Connection ERROR")


    # if url.status_code==200:   
    #     soup = BeautifulSoup(url.content, 'html.parser')

    #     for i in range(1,5):
    #         need= soup.find_all('tr',{'id':f"macromolecule-entityId-{i}-rowDescription"})
    #         if len(need)!=0:
    #             chain = need[0].find('td',{'style':'width:200px;'}).text 
    #             uniport_1 = soup.find_all("table", attrs={"id":f"table_macromolecule-protein-entityId-{i}"})
    #             uniport_2= uniport_1[0].find_all(href= re.compile("https://www.uniprot.org/uniprot"))
    #             if len(uniport_2)!=0:
    #                 uniport_id= uniport_2[0].text
    #             else:
    #                 uniport_id=None
    #             print(chain,uniport_id)
    #         else:
    #             pass


        












#             for z in [1,2,3,5,6,7]:   #multiple looping for the multple chains.
#                 d =soup.find('table',{'class':"table table-bordered table-condensed tableEntity" ,
#                                 'id':f'table_macromolecule-protein-entityId-{z}'}) 
#                 s = d.find('tr',{'id':f"macromolecule-entityId-{z}-rowDescription"})
#                 uniport = d.find('span',{'class':"label label-rcsb"}).text
#                 chain = s.find('td',{'style':'width:200px;'})        #.text.replace(',','').replace('Less','')
#                 sam_1 =[i.get_text() for i in chain.find_all('a')]   #Stores the chain value as list

#                 if uniport== '30% Identity':    #When chain have no uniport id is not provided,it will add value = 'None' 
#                     uniport ='None'
#                     with open(r"30%_identity.txt",'a') as file_30:
#                         file_30.write(r+' '+'\n')
#                         file_30.close()
#                 chain_dic[tuple(sam_1)] =uniport
#                 dic_1[r.lower()] =chain_dic
#                 print(dic_1)
# scrappy_fun(['1mky'