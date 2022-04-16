# CYBR4580
# Last Updated: April 10th, 2022


# To use, insert the IPs to be monitored into MonitorList.txt
#
# This script will automatically create a Blacklist folder and download the latest lists of known infected, malicious, or compromised IP addresses.  
# After downloading threat intel lists, it will check all IPs listed in MonitorList against the known infected lists and display any matching results. 


import os
import sys
import urllib.request
import requests



# Read in MyList file for comparisons
with open('./MonitorList.txt') as f:
     lines = f.read().splitlines()

# Create the BlackLists directory to hold the CSVs
try:
	path = "./BlackLists"
	os.mkdir(path)
except:
	print("Unable to create a new BlackLists folder, it appears it already exists. This script will now utilize the previously made folder.")

# Download and save the blacklists to be used.
print(".")
print("..")
print("...")
print("Starting the process of updating threat intellgience feeds, this may take several minutes.")
print(".")
print("..")
print("...")
try:
	print("Downloading DeBlockList, please wait...")
	#urllib.request.urlretrieve('https://lists.blocklist.de/lists/all.txt', './BlackLists/deblocklist.txt')
	print("Downloading Spamhaus Drop list, please wait...")
	urllib.request.urlretrieve('https://github.com/SecOps-Institute/SpamhausIPLists/blob/master/drop.txt', './BlackLists/Spamhaus.txt')
	print("Downloading Tor Exit Node list, please wait...")
	urllib.request.urlretrieve("https://github.com/SecOps-Institute/Tor-IP-Addresses/blob/master/tor-exit-nodes.lst", "./BlackLists/TorExitNodes.txt")
	print("Downloading Abuse.ch Drop list, please wait...")
	urllib.request.urlretrieve('https://feodotracker.abuse.ch/downloads/ipblocklist.txt', './BlackLists/Abuse.txt')
	print("Downloading Emerging Threats list, please wait...")
	urllib.request.urlretrieve("https://rules.emergingthreats.net/blockrules/compromised-ips.txt", "./BlackLists/emergingthreats.txt")


except:
	print("One or more blacklists may not have downloaded correctly, check the BlackLists folder to investigate any missing files.")


try:
	with open('./BlackLists/deblocklist.txt') as z:
     		temp = z.read().splitlines()
     	
	for i in lines:
     		for ii in temp:
     			if i == ii:
     				print ("\33[1;31;40m WARNING " + i + " Was found in the DeBlockList threat list.")
     				
	with open('./BlackLists/Spamhaus.txt') as y:
     		temp = y.read().splitlines()
     	
	for i in lines:
     		for ii in temp:
     			if i == ii:
     				print ("\33[1;31;40m WARNING " + i + " Was found in the Spamhaus threat list.")
     				
	with open('./BlackLists/TorExitNodes.txt') as x:
     		temp = x.read().splitlines()
     	
	for i in lines:
     		for ii in temp:
     			if i == ii:
     				print ("\33[1;31;40m WARNING " + i + " Was found in the TorExitNodes threat list.")
     				
	with open('./BlackLists/Abuse.txt') as w:
     		temp = w.read().splitlines()
     	
	for i in lines:
     		for ii in temp:
     			if i == ii:
     				print ("\33[1;31;40m WARNING " + i + " Was found in the Abuse.ch threat list.")
     				
	with open('./BlackLists/emergingthreats.txt') as v:
     		temp = v.read().splitlines()
     	
	for i in lines:
     		for ii in temp:
     			if i == ii:
     				print ("\33[1;31;40m WARNING " + i + " Was found in the Emerging Threats threat list.")
except:
	print("\033[0;37;40m An error occured when searching the blacklist files, please double check all files exist.\33")
     	
