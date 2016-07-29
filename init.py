#FUNCION DE INICIALZACION DE BASE DE DATOS COMPANIES_AMOUNT Y COMPANIES_PRICES

def init():
    #LIBRERIAS
    from yahoo_finance import Share
    import pandas as pd
    import numpy as np
    import sqlite3 as lite
    import requests
    from requests.auth import HTTPBasicAuth
    
    list_companies=["BBVA","TEF","SAN"]
    def data_frame_companies_prices(list_companies,a,b):

        # Es una funcion que toma una lista de empresas (codificadas por yahoo.finance) y valor minimo y maximo
        # de la distribucion uniforme que sigue la diferencia entre el bid y el ask para las empresas.



        list_index=["ask5","ask4","ask3","ask2","ask1","bid1","bid2","bid3","bid4","bid5"]
        companies_prices=pd.DataFrame(index=list_index)

        for i in list_companies:

            company = Share(i)
            open_price=company.get_price()
            open_price=float(open_price)
            a=float(a)
            b=float(b)
            random1=(np.random.rand(1)+(a/b-a))/(1.0/b-a)

            first_ask_price=open_price+(round(random1,2))/2.0
            ask_array=np.array([first_ask_price+0.04,first_ask_price+0.03,first_ask_price+0.02,first_ask_price+0.01,first_ask_price])

            first_bid_price=open_price-(round(random1,2))/2.0
            bid_array=np.array([first_bid_price+0.04,first_bid_price+0.03,first_bid_price+0.02,first_bid_price+0.01,first_bid_price])

            ask_bid_array=np.concatenate((ask_array,bid_array))

            companies_prices[i]=ask_bid_array

        return companies_prices


    def data_frame_companies_amount(list_companies,porcentaje_volumnen_diario,max_var_pvd):

        # Es una funcion que toma una lista de empresas (codificadas por yahoo.finance), el porcentaje (tanto por uno)
        # sobre el volumen diario a considerar y la maxima variacion en porcentaje (tanto por uno) sobre este porcentaje.



        list_index=["ask5","ask4","ask3","ask2","ask1","bid1","bid2","bid3","bid4","bid5"]
        companies_amount=pd.DataFrame(index=list_index)
        for i in list_companies:

            company = Share(i)
            volume=company.get_volume()
            cantidad_per_ba=float(company.get_avg_daily_volume())*porcentaje_volumnen_diario
            num=cantidad_per_ba*max_var_pvd # variacion maxima respecto al 1% del volumen diario
            vec_list_amount=[]

            for h in range(0,len(list_index)):

                vec_list_amount.append(round(cantidad_per_ba+np.random.randint(-num,num,1)))

            vec_amount=np.array(vec_list_amount)
            companies_amount[i]=vec_amount   

        return companies_amount



    companies_prices=data_frame_companies_prices(list_companies,0.1,0.8)
    companies_amount=data_frame_companies_amount(list_companies,0.001,0.1)
    
    # ENVIAR DATAFRAME COMPANIES_AMOUNT
    
    filename="a.csv"
    companies_amount.to_csv(filename, sep=',')

    url = 'http://rodrigocarvajal.pythonanywhere.com/uploadcsvfilea'

    files = {'file': (filename, open(filename, 'rb'))}
    rsub = requests.post(url, files=files)
    resp_str = str(rsub.text)
    print resp_str
    
    #ENVIAR DATAFRAME COMPANIES_PRICES

    filename="p.csv"
    companies_prices.to_csv(filename, sep=',')

    url = 'http://rodrigocarvajal.pythonanywhere.com/uploadcsvfilep'

    files = {'file': (filename, open(filename, 'rb'))}
    rsub = requests.post(url, files=files)
    resp_str = str(rsub.text)
    print resp_str
    

# FUNCION QUE A PARTIR DE LA BASE DE DATOS USERS INICIALIZA UNA BASE DATOS DE CANTIDAD DE ACCION POR USER Y EMPRESA

# OJO SE DEBE INICIALIZAR SIEMPRE QUE SE HAYA INICIALIDADO LA BB USERS , AMOUNTS O PRICES


def init_customers(): 

    import requests
    from requests.auth import HTTPBasicAuth

    url = 'http://rodrigocarvajal.pythonanywhere.com/init_customers'  # trabaja a partir de la otra base users
    rsub = requests.get(url)

    print rsub.text