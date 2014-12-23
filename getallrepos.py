print ('write a program to list all the repos from given url which is not forked i.e. "fork" = False.https://api.github.com/users/mralexgray/repos')
path = "https://api.github.com/users/mralexgray/repos"

import urllib2, json
response  = urllib2.urlopen('https://api.github.com/users/mralexgray/repos')
data = json.load(response)
for j in data:
	if j["fork"] == False:
		print j['name']


#pprint(data)
#json_data.close()
