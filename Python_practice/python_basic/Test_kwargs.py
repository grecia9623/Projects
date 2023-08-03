def get_product(**datos): #**kwargs
    print(datos["id"], datos["name"]) #acceder a los parametros

get_product(id="0001", 
            name="iphone",
            desc="Iphone 13 PRO MAX") # se nombran los parametros obligatoriamente
#{'id': 'id'} Diccionario