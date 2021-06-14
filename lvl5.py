import requests

params = { "nothing":"12345" }
while True:
    flag = 0
    r = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php", params= params )
    n = len(r.text.split()) -  1
    print(r.text)
    # print(r.text.split()[n])
    
    if flag == 1:
        params["nothing"] = int(params["nothing"])/2
        flag = 0
    else:
        params["nothing"] = r.text.split()[n]
        flag = 0
            
    if not params["nothing"].isdigit():  # when we get this sentence: Yes. Divide by two and keep going.
        flag = 1
        
    if r.text == "peak.html": #final answer
        break

# now visit http://www.pythonchallenge.com/pc/def/peak.html :)

