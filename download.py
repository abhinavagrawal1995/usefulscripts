#Script to download all files from a web page
#Written by gR00T
import re
import os
webpage="name of the webpage. ex: index.html"
webpath="link to parent folder of the webpage to create absolute path ex : google.com/folder/folder2/" #must have slash in the end
os.system("wget "+webpath+webpage)
#index.html or whatever downloaded filename is
with open(webpage, 'r') as myfile:
    data=myfile.read().replace('\n', '')
    #replace file extaensions with whatever is needed
p = re.compile("(?:(?:ftp|http|https)://)?[a-z0-9_\./]+\.(?:rm|pdf|doc|eps|tar\.gz|tex|txt)", re.IGNORECASE)
found=re.findall(p,data)
#make sub directory
os.system("mkdir files")
for line in found :
	#check if each link is absolute. add website path if relative
	if(!re.findall('^(?:ftp|http|https)://',line)):
		line=webpath+line
	os.system("wget --directory-prefix=files/ "+line)

