import requests
from discord import Webhook, RequestsWebhookAdapter
import time
target1 = 'https://api.bscscan.com/api?module=account&action=tokentx&address=0xB20bF6D7f60059dd5dE46F3F0F32665a259ea6C0&page=1&offset=10&startblock=0&endblock=999999999&sort=desc&apikey=NZKNZAZTGAXSWFXWN3APAC9GG387F7TWFK'
mURL = 'https://discord.com/api/webhooks/902651335550304338/RCiw92QwhmwEq5KzcN6Fy1mWINoIZSvlpbDgnaRWtLBldhlW2p4z19UyzW8lvtYvtYTO'
webhook = Webhook.from_url(mURL,adapter=RequestsWebhookAdapter())
response = requests.get(target1)
former = '0'
while True:
    result = response.json()['result'][0]
    blocknum = result['blockNumber']
    if blocknum != former:
        if result['from'] == '0xb20bf6d7f60059dd5de46f3f0f32665a259ea6c0':
            direction = 'OUT'
        else:
            direction = 'IN'
        value = result['value']
        webhook.send('Target: {}\nToken: {}\nDirection: {}\nValue: {}'.format('0xb20bf6d7f60059dd5de46f3f0f32665a259ea6c0',result['tokenName'],direction,value))
        former = blocknum
        time.sleep(10)