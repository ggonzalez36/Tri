from distutils.ccompiler import show_compilers
from typing import Union

from fastapi import FastAPI
import requests
import json

app = FastAPI()

@app.get("/stocks/{stock_value}")
def read_item(stock_value: int):

    allprice=getallStocks()

    if(stock_value<allprice):

        return "no se puede invertir en este protafolio el monto es menor"

    else :


        return dict

def createPortfolio():

    dict={'appl':getStockPrice('AAPL'), 'googl':getStockPrice('GOOGL'),'amzn':getStockPrice('AMZN'),
    'tsla':getStockPrice('TSLA'),'fb':getStockPrice('FB'),'twtr':getStockPrice('TWTR')
    }

    return dict


@app.get("/allstocks/")
def read_item(stock_value: int):


    allprice=getallStocks()


    return {"price":allprice}



def getallStocks():

    aapl=getStockPrice('AAPL')
    googl=getStockPrice('GOOGL')
    amzn=getStockPrice('AMZN')
    tsla=getStockPrice('TSLA')
    fb=getStockPrice('FB')
    twtr=getStockPrice('TWTR')
    uber=getStockPrice('UBER')
    lyft=getStockPrice('LYFT')
    snap=getStockPrice('SNAP')
    shop=getStockPrice('SHOP')
    
    price =aapl+googl+amzn+tsla+fb+twtr+uber+lyft+snap+shop

    return price

def getStockPrice (company):

    response = requests.get("https://financialmodelingprep.com/api/v3/quote-short/"+ company +"?apikey=c13a5d2ecf7cc6b8c50c06d7e1dfce22")
    jresp=response.json()
    print(jresp[0])
    jsonLoad=jresp[0]
    #resp = json.loads(jsonLoad)
    print (jsonLoad['price'])


    return jsonLoad['price']