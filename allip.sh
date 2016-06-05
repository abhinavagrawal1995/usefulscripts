for i in {1..254}
do 
	ping -c 1 192.168.1.$i > /dev/null && arp 192.168.1.$i
done
