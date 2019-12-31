import urllib.request 
import json

test_data = 'http://127.0.0.1:5000'
get_data = 'http://127.0.0.1:5000/api/get_data({})'
put_data = 'http://127.0.0.1:5000/api/put_data({},{})'

#getting the data
name1 = input('enter the name : ')
data = urllib.request.urlopen(get_data.format(name1))
x = json.loads(data.read())
print(x['id'])
print(x['name'])
print(x['location'])

#putting the data
print('enter name and location : ',end='')
name1 = input()
loc1 = input()
put = urllib.request.urlopen(put_data.format(name1,loc1))
x = put.read()
print (x)