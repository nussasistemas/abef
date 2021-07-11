# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import  requests
import json
app_id = 'alanhfs'
app_key = '$Djhu1984'
language = 'pt'
word_id = 'irmão'
#url = 'https://dictapi.lexicala.com/test'  + language + '/'  + word_id.lower()

url = 'https://dictapi.lexicala.com/login -u alanhfs:$Djhu1984'

r = requests.get(url, headers = {'user' : app_id, 'pass' : app_key})
print("code {}\n".format(r.status_code))
print("text \n" + r.text)
print("json \n" + json.dumps(r.json()))