# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import requests
import json
app_id = '800dcc4e'
app_key = 'f9bfcbcd14359462605191486ca4269f'
language = 'pt'
word_id = 'irmão'
url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/'  + language + '/'  + word_id.lower()
# url Normalized frequency
urlFR = 'https://od-api.oxforddictionaries.com:443/api/v2/stats/frequency/word/'  + language + '/?corpus=nmc&lemma=' + word_id.lower()
r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
print("code {}\n".format(r.status_code))
print("text \n" + r.text)
print("json \n" + json.dumps(r.json()))