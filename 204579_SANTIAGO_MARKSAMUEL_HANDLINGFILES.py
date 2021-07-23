products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}
def get_product(code):
    for key in products.keys():
        if key == code:
            return(products[key])

def get_property(code,property):
    for key in products.keys():
        if key == code:
            return(products[key][property])

def main(): 
    total=0
    dict1={}
    while(True):
        inp=input("Input:")
        if inp == "/":
            break
        else:
            order=inp.split(",")
            code=order[0]
            num=int(order[1])
            if code in dict1.keys():
                dict1[code]+=num
            else:
                dict1[code]=num
    with open("receipt.txt","w") as f:             
        f.write(F'''
==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL''')
        for i in products.keys():
            if i in dict1.keys():
                name=get_property(i,"name")
                price=get_property(i,"price")*dict1[i]
                total+=price
                f.write(F'''\n{i}\t\t\t{name}\t\t\t{dict1[i]}\t\t\t\t{price}''')
        f.write(F'''\nTotal:\t\t\t\t\t\t\t\t\t\t{total}
==
''')
main()