#!/usr/bin/env python
import sys

def KSA(key):
    keylength = len(key)

    S = range(256)

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        # S[i], S[j] = S[j], S[i]
        S[i] ^= S[j]
        S[j] ^= S[i]
        S[i] ^= S[j]

    return S


def PRGA(S):
    i = 0
    j = 0
    while True:
	    i = (i + 1) % 256
	    j = (j + S[i]) % 256
	    S[i], S[j] = S[j], S[i]
	    #tmp = S[i]
	    #S[i] = S[j]
	    #S[j] = tmp

	    K = S[(S[i] + S[j]) % 256]
	    yield K


def RC4(key):
	S = KSA(key)
	return PRGA(S)


if __name__ == '__main__':

	file = open('testRC4.txt','r')
	plaintext = file.read()
	file.close()

	key = 'rc4moica'

	def convert_key(s):
	    return [ord(c) for c in s]
	key = convert_key(key)

	keystream = RC4(key)

	fileENC = open('testRC4.enc','w')
	for c in plaintext:
		#sys.stdout.write("%02X" % (ord(c) ^ keystream.next()))
		fileENC.write("%02X" % (ord(c) ^ keystream.next()))

	fileENC.close()

	res = open('testRC4.enc','r')
	print res.read()
	res.close()