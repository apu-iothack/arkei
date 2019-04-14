from bs4 import BeautifulSoup
import requests
import re
import time

#small database of registered names and assigned IPs
names = {'Lecturer PC':'192.168.0.101', 'Emir Saidov': '192.168.0.104' , 'Karthik Arunasalam':'192.168.0.100','Shanazar Valiyev':'192.168.0.103', 'Irshad Shaik':'192.168.0.105',
         'Amirlan':'192.168.0.106' }

#while loop to constantly keep checking connected to the router hosts and their IP addresses 
while True:
    source = requests.get ('http://192.168.0.1/st_wlan.php').text #access configuration website of the router by its ip address and fetch information about connected hosts
    soup = BeautifulSoup(source, 'lxml') #parse the information
    f = open("IP.txt","w+",encoding='utf-8') #save information to notepad
    f.write('%s' % soup)
    f.close()
    f = open("IP.txt", "r")
    logfile = list(open('IP.txt', 'r').read().split('\n'))
    for entry in logfile:
        ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}', entry) #parse information and gather all ip addresses
        for ip in ips:
            print (ip)
            if ip == names['Karthik Arunasalam']:  #to check if any ip address assigned to particular user from the database
                print("Karthik Arunasalam\n")
            elif ip == names['Lecturer PC']:
                print ('Lecturer PC\n')
            elif ip == names['Emir Saidov']:
                print ('Emir Saidov\n')
            elif ip == names['Shanazar Valiyev']:
                print ('Shanazar Valiyev\n')
            elif ip == names['Irshad Shaik']:
                print ('Irshad Shaik\n')
            elif ip == names['Amirlan']:
                print ('Amirlan Sabalakov\n')
    print('\n-----------------------------\n')
    time.sleep(2)
    True


    

