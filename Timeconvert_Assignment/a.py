import re
s = "3 hour 15 minutes"
hm = re.findall("\d+", s) #returns list containing ['hr', 'min']
print("Extractor =",hm)
hm = [int(x) for x in hm]
print(hm[0]*60+hm[1])