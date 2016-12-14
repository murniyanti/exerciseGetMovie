from urllib2 import Request, urlopen, URLError
#import omdb
import json
s = raw_input()
print type(s)
# Enter your code here.
url = 'http://www.omdbapi.com/?s='+s
response = urlopen(url)
data = json.load(response)

countMovie = 0
for i in range(len(data["Search"])):
    print data["Search"][i]["Title"]
    countMovie = countMovie + 1
print countMovie