from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.cryptocurrencies import CryptoCurrencies


#GET DATA from ALPHA_VANTAGE

# Get json object with the intraday data and another with  the call's metadata
# alpha_vantage API key WE62WGNY1RRXS3ZO
def getStockAlpha(COMCODE):
    COMCODE = 'idx'
    ts = TimeSeries(key='WE62WGNY1RRXS3ZO', output_format='pandas', indexing_type='integer')
    data, meta_data = ts.get_intraday(symbol=COMCODE,interval='1min', outputsize='full')
    data.to_csv('output.csv')
    return data

def plotStockData(data):
    CompanyData = data.plot(y=['1. open','2. high','3. low','4. close'])
    fig = CompanyData.get_figure()
    return fig

def getcryptoAlpha(COMCODE):
    cc = CryptoCurrencies(key='WE62WGNY1RRXS3ZO', output_format='pandas')
    data, meta_data = cc.get_digital_currency_daily(symbol=COMCODE, market='CNY')
    print(data.to_string(), file=open("outputcrypto.txt", "w"))
    return data

def plotCryptokData(data):
    CompanyData = data.plot(y=['1b. open (USD)','2b. high (USD)','3b. low (USD)','4b. close (USD)'])
    fig = CompanyData.get_figure()
    return fig