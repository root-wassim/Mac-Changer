#wassim mac changer tool
#root-wassim

import subprocess
import optparse
import re

parser = optparse.OptionParser()
parser.add_option("-i","--interface", dest="network_interface", help="The place to put the network interface")
parser.add_option("-m","--mac", dest="new_mac",help="The place to put the new mac address")

options, arguments = parser.parse_args()


if not options.network_interface and not options.new_mac :
    print("[-] Specify an interface and mac address ")
    exit()

elif not options.new_mac :
    print("[-] Specify a mac address ")
    exit()

elif not options.network_interface :
    print("[-] Specify an interface  ")
    exit()


subprocess.call("ifconfig " + options.network_interface + " down", shell=True)
subprocess.call("ifconfig " + options.network_interface + " hw ether " + options.new_mac, shell=True)
subprocess.call("ifconfig " + options.network_interface + " up", shell=True)

print("[+] Changing MAC Address for " + options.network_interface + " to " + options.new_mac)

ifconfig_check = subprocess.check_output("ifconfig " + options.network_interface, shell=True).decode("UTF-8")
check = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", ifconfig_check)


if check[0] == options.new_mac :
    print("[+] Mac address has changed successfully")

else :
    print("[-] Changing mac to " + options.new_mac + " was failled")    