import xml.etree.ElementTree as ET
import urllib.request as ur

url = input("Enter location: ")
# http://py4e-data.dr-chuck.net/comments_465856.xml
# http://py4e-data.dr-chuck.net/comments_42.xml

total = 0
add = 0

print("Retrieving", url)
xml_file = ur.urlopen(url).read()
print("Retrieved", len(xml_file), "characters")

tree = ET.fromstring(xml_file)
counts = tree.findall('.//count')
for count in counts:
    add += int(count.text)
    total += 1

print("Count: ", total)
print("Sum: ", add)


# Output -->

# Enter location: http://py4e-data.   dr-chuck.net/comments_465856.xml
# Retrieving http://py4e-data.dr-chuck.net/comments_465856.xml
# Retrieved 4194 characters
# Count:  50
# Sum:  2270
