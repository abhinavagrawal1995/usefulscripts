#!/bin/bash
 #This script finds video file using search substring and plays it
printf "\n\tWhich File you wanna play?: "
read file_name
echo -e "\tYou entered file : $file_name \n\nMy search shows following possibilities:\n\nNo.| \t Name"
 
echo -e "------------------------------------------------"
 
find . \( -iname "*$file_name*.mp4" -o -iname "*$file_name*.avi" -o -iname "*$file_name*.mkv" \)  > ./search.txt
 
#Takes each file name and removes everything from name until the last '/' from left is found
 
count=1
color=30
cat ./search.txt | while read line
do
	let color++
	printf "\e[1;${color}m"	
	printf "%-2d | " $count
 	echo $line | sed 's/.*\///g'  
	printf "\e[0m"
	let count++
	if [ $color -eq 38 ]; then
		let color=30
	fi
done
 
printf "\nSelect Option: "
read choice
 
 
echo -e "\n\nThe file is located at path:\n"
 
cat ./search.txt | sed ''$choice'q;d' | sed 's/ /\\ /g' | sed 's/(/\\(/g' | sed 's/)/\\)/g' | sed "s/'/\\\'/g" | sed 's/&/\\&/g'
 
echo -e "\nLaunching with VLC..."
 
cat ./search.txt | sed ''$choice'q;d' | sed 's/ /\\ /g' | sed 's/(/\\(/g' | sed 's/)/\\)/g' | sed "s/'/\\\'/g" | sed 's/&/\\&/g' | xargs vlc --fullscreen 2>/dev/null & disown
 
#echo -e "\nUsage: vlc 'copied_string'\n"
 
echo -e "\n"
 
exit 0

