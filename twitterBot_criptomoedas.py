
# coding: utf-8

# In[ ]:


import hashlib
import hmac
import requests
import time



#funções

def getapi(siglamoeda):
    url = 'https://apiv2.bitcoinaverage.com/indices/global/ticker/' + siglamoeda
    headers = {'X-Signature': signature}
    result = requests.get(url=url, headers=headers)
    info = result.json()
    return info

def media_em_reais(siglamoeda):
    media_moeda = getapi(siglamoeda)['averages']
    media_moeda = "%.2f" % media_moeda['day']
    media_moeda = media_moeda.replace('.', ',')
    return media_moeda


import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

while True:
        
#coleta API bitcoinaverage

    secret_key = ''
    public_key = ''
    timestamp = int(time.time())
    payload = '{}.{}'.format(timestamp, public_key)
    hex_hash = hmac.new(secret_key.encode(), msg=payload.encode(), digestmod=hashlib.sha256).hexdigest()
    signature = '{}.{}'.format(payload, hex_hash)

    media_bitcoin_brl_dia = media_em_reais('BTCBRL')
    media_litecoin_brl_dia = media_em_reais('LTCBRL')
    media_bitcoincash_brl_dia = media_em_reais('BCHBRL')
    media_ethereum_brl_dia = media_em_reais('ETHBRL')
    frase_tweet = f'O valor médio das criptomoedas é:\n Bitcoin(BTC) R$ {media_bitcoin_brl_dia} \n Litecoin(LTC) R$ {media_litecoin_brl_dia} \n Bitcoin Cash(BCH) R$ {media_bitcoincash_brl_dia} \n Ethereum(ETH) R$ {media_ethereum_brl_dia} \n #bitcoin #litecoin #bitcashcoin #ethereum'
    api.update_status(frase_tweet)
    time.sleep(1800)
        
        

