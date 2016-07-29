#FUNCIONES DE INFORMACION 


#FUNCION QUE DEVUELVE LAS CANTIDADES DE ASK Y BID PARA UNA EMPRESA

def get_companies_amount(empresa):
    
    import requests
    from requests.auth import HTTPBasicAuth

    url = 'http://rodrigocarvajal.pythonanywhere.com/get_companies_amount2/'+str(empresa)
    rsub = requests.get(url)

    print rsub.text

#FUNCIONES DE INFORMACION 


#FUNCION QUE DEVUELVE LAS CANTIDADES DE ASK Y BID PARA UNA EMPRESA

def get_companies_prices(empresa):
    
    import requests
    from requests.auth import HTTPBasicAuth

    url = 'http://rodrigocarvajal.pythonanywhere.com/get_companies_prices2/'+str(empresa)
    rsub = requests.get(url)

    print rsub.text

#FUNCIONES DE INFORMACION 


#FUNCION QUE DEVUELVE LAS CANTIDADES DE ASK Y BID PARA UNA EMPRESA

def get_customers(username):
    
    import requests
    from requests.auth import HTTPBasicAuth

    url = 'http://rodrigocarvajal.pythonanywhere.com/get_customers2/'+str(username)
    rsub = requests.get(url)

    print rsub.text

#FUNCIONES DE INFORMACION 


#FUNCION QUE DEVUELVE LOS USUARIOS DE LA APP

def get_users_username():
    
    import requests
    from requests.auth import HTTPBasicAuth

    url = 'http://rodrigocarvajal.pythonanywhere.com/get_users_username'
    rsub = requests.get(url)

    print rsub.text

#FUNCIONES DE INFORMACION 


#FUNCION QUE DEVUELVE LAS CONTRASENAS DE LA APP

def get_users_password():
    
    import requests
    from requests.auth import HTTPBasicAuth

    url = 'http://rodrigocarvajal.pythonanywhere.com/get_users_password'
    rsub = requests.get(url)

    return rsub.text