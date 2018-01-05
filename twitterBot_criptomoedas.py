
# coding: utf-8

# In[ ]:


import hashlib
import hmac
import requests
import time

#coleta API bitcoinaverage

secret_key = 'ODA4ZGY1ZGJkYWRiNDM2YzgxZjA2ZDExOTA4N2NmODM2ZmZlZjNhMmIxNGU0MWFjOThkOGY1OWJmOGE0ZmQxOQ'
public_key = 'OTM2MzZkZTUyMWQ3NGUzYTg5MDZiYmQ5YmU3NjM5MWQ'
timestamp = int(time.time())
payload = '{}.{}'.format(timestamp, public_key)
hex_hash = hmac.new(secret_key.encode(), msg=payload.encode(), digestmod=hashlib.sha256).hexdigest()
signature = '{}.{}'.format(payload, hex_hash)


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


#BitCoin em Reais

#media_bitcoin_brl_dia = media_em_reais('BTCBRL')
       
#Litecoin em Reais

#media_litecoin_brl_dia = media_em_reais('LTCBRL')

#BitCoin Cash em Reais

#media_bitcoincash_brl_dia = media_em_reais('BCHBRL')

#Ethereum Cash em Reais

#media_ethereum_brl_dia = media_em_reais('ETHBRL')
#frase_tweet = f'O valor médio das criptomoedas é:\n Bitcoin(BTC) R$ {media_bitcoin_brl_dia} \n Litecoin(LTC) R$ {media_litecoin_brl_dia} \n Bitcoin Cash(BCH) R$ {media_bitcoincash_brl_dia} \n Ethereum(ETH) R$ {media_ethereum_brl_dia} \n #bitcoin #litecoin #bitcashcoin #ethereum'

import tweepy

consumer_key = 'kRAmwa1Gs4ILHeL8vWwmvAgUD'
consumer_secret = 'BeArzFADJLzzhhqjwpvcPyIqBsby2bDdcMXIlk6sNaPyu4NvWJ'
access_token = '949002549046235136-w10GiBBEOLJ2l7oMj82EGIHJvrGPKY5'
access_token_secret = 'vledjq7AbsZsczuDWLdIPinElpaxQ39havMUVGhIS5r5U'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

while True:
        media_bitcoin_brl_dia = media_em_reais('BTCBRL')
        media_litecoin_brl_dia = media_em_reais('LTCBRL')
        media_bitcoincash_brl_dia = media_em_reais('BCHBRL')
        media_ethereum_brl_dia = media_em_reais('ETHBRL')
        frase_tweet = f'O valor médio das criptomoedas é:\n Bitcoin(BTC) R$ {media_bitcoin_brl_dia} \n Litecoin(LTC) R$ {media_litecoin_brl_dia} \n Bitcoin Cash(BCH) R$ {media_bitcoincash_brl_dia} \n Ethereum(ETH) R$ {media_ethereum_brl_dia} \n #bitcoin #litecoin #bitcashcoin #ethereum'
        api.update_status(frase_tweet)
        time.sleep(900)
        
        
#api.update_status(frase_tweet)

