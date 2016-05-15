for i in {0..255}
do 
	ping -c 1 192.168.1.$i > /dev/null && arp 192.168.1.$i
done
