import urllib.request
import json
url = input("Enter location: ")
print("Retrieving", url)
data = urllib.request.urlopen(url).read().decode()
print("Retrieved", len(data) ,"characters")
info = json.loads(data)
count = 0
sum = 0
for counts in info['comments']:
    sum += int(counts['count'])
    count += 1
print("Count:", count)
print("Sum:", sum)
