#wassim mac changer tool
#root-wassim

import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", dest="network_interface")
parser.add_option("-m", dest="new_mac")
options, arguments = parser.parse_args()

subprocess.call("ifconfig " + options.network_interface + " down", shell=True)
subprocess.call("ifconfig " + options.network_interface + " hw ether " + options.new_mac, shell=True)
subprocess.call("ifconfig " + options.network_interface + " up", shell=True)

print("[+] Changing MAC Address for " + options.network_interface + " to " + options.new_mac)