import csv	

file = open('client_historical.csv','r')
reader = csv.reader(file, delimiter=',', quotechar="'")
out = ''
for r in reader:
	print(len(r))
	if(len(r) == 41):
		mac = r[2]
		print(mac)
		r[2] = mac[:8]
	out += (','.join(r))+'\n'
out_file = open('new_client_historical.csv','w')
out_file.write(out)
out_file.close()