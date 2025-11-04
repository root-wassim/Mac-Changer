#wassim mac changer tool
#root-wassim

import subprocess
import optparse
import re
import sys

def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest="network_interface", help="The place to put the network interface")
    parser.add_option("-m","--mac", dest="new_mac",help="The place to put the new mac address")

    options, arguments = parser.parse_args()


    if not options.network_interface and not options.new_mac :
        parser.error("[-] Specify an interface and mac address , type -h for help")
    
    elif not options.new_mac :
        parser.error("[-] Specify a mac address , type -h for help")

    elif not options.network_interface :
        parser.error("[-] Specify an interface  , type -h for help")

    return options    



def change_mac(network_interface ,new_mac):
    try:
        subprocess.check_call(["ifconfig", network_interface, "down"])
        subprocess.check_call(["ifconfig", network_interface, "hw", "ether", new_mac])
        subprocess.check_call(["ifconfig", network_interface, "up"])
    except subprocess.CalledProcessError as e:
        print(f"[-] Failed to run ifconfig commands: {e}")
        sys.exit(1)

    print("[+] Changing MAC Address for " + network_interface + " to " + new_mac)



def check_mac(network_interface ,new_mac):
    try:
        ifconfig_check = subprocess.check_output(["ifconfig", network_interface]).decode("utf-8")
    except subprocess.CalledProcessError as e:
        print(f"[-] Failed to run ifconfig: {e}")
        sys.exit(1)

    check = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", ifconfig_check)

    if check[0] == new_mac :
        print("[+] Mac address has changed successfully")
    else :
        print("[-] Changing mac to " + new_mac + " was failled")  


if __name__ == "__main__":
   
   options = get_argument()
   change_mac(options.network_interface,options.new_mac)
   check_mac(options.network_interface,options.new_mac)   
