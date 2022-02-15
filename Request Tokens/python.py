#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Libraries
from hashlib import sha256
from time import time

# Variables
hashPattern = "0001110111101110001111010101111011010001001110011000110001000110"
secret = "iEk21fuwZApXlz93750dmW22pw389dPwOk"

def requestToken(token, timestamp):
	firstHash = sha256(str("{}{}".format(secret, token)).encode("utf-8")).hexdigest()
	secondHash = sha256(str("{}{}".format(timestamp, secret)).encode("utf-8")).hexdigest()

	return "".join([firstHash[i] if c == "0" else secondHash[i] for i, c in enumerate(hashPattern)])

def main():
	print(requestToken("m198sOkJEn37DjqZ32lpRu76xmw288xSQ9", time() * 1000))

main()