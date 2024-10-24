#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Libraries
from struct import pack, unpack
from uuid import UUID

class Signatures(object):
    def __init__(self):
        super(Signatures, self).__init__()

    def parseGrpc(self, data):
    	return pack("!?i", False, len(data)) + data

    def unpackGrpc(self, data):
    	ret = []

    	while data:
    		try:
    			_, length = unpack("!?i", data[:5])
    			message = unpack("!%is" % length, data[5 : 5 + length])[0]
    		except Exception:
    			return None

    		data = data[5 + length:]
    		ret.append(message)

    	return ret

    def reverseString(self, string):
        return string[::-1]

    def getBits(self, guid, start, length):
        return int.from_bytes(bytearray.fromhex("".join([self.reverseString(x) for x in "-".join(format(x, "02x") for x in UUID(guid.replace("-", "")[::-1]).bytes).split("-")]))[start : start + length], byteorder="little", signed=False)

    def getUuid(self, lowBits, highBits):
        return str(UUID(bytes=(lowBits.to_bytes(8, byteorder="little") + highBits.to_bytes(8, byteorder="little"))[::-1]))

def main():
	signatures = Signatures()

	lowBits = signatures.getBits("5317c9b0-a7bc-43fa-8b86-6c47ce167138", 0, 8)
	highBits = signatures.getBits("5317c9b0-a7bc-43fa-8b86-6c47ce167138", 8, 8)
	uuidFromBits = signatures.getUuid(lowBits, highBits)

	print("[?] Low bits -->", lowBits)
	print("[?] High bits -->", highBits)
	print("[?] Uuid from bits -->", uuidFromBits)

if __name__ == "__main__":
	main()