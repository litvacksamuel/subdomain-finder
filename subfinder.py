#!/usr/bin/env python3

import sys
from ping3 import ping, verbose_ping

if len(sys.argv) > 1:
	domain = sys.argv[1]

	wordlist = "subdomains-10000.txt"

	with open(wordlist, "r") as f:
		for subdomain in f.readlines():
			subdomain = subdomain.replace("\n", "")
			res = ping(subdomain + "." + domain)
			if res:
				print(subdomain + "." + domain + " exists!")
else:
	print("Usage: subbrute.py domain")
