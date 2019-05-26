#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Made by Ano Mobb
# MultiFunction Bitcoin Cracker/ mfbc
# 

try:
    import hashlib, random, os, base64, binascii, ecdsa, base58, secrets, time, multiprocessing
except ImportError:
    import subprocess
    subprocess.check_call(["python", '-m', 'pip', 'install', 'base58==1.0.0'])
    subprocess.check_call(["python", '-m', 'pip', 'install', 'ecdsa==0.13'])

    

x = input("Enter mnemonic code words: ")
l = len(x.split())

    



       
def main():
    while True:
        lis = x.split()
        choices = []
        while len(choices) < l:
            selection = random.choice(lis)
            if selection not in choices:
                choices.append(selection)
                xa = ' '.join(choices)
                pvt1 = hashlib.sha256(xa.encode("utf-8")).hexdigest()
                privatekey1 = binascii.unhexlify(pvt1)
                s = ecdsa.SigningKey.from_string(privatekey1, curve = ecdsa.SECP256k1)
                publickey = '04' + binascii.hexlify(s.verifying_key.to_string()).decode('utf-8')
                extended_key1 = "80"+pvt1
                first_sha2561 = hashlib.sha256(binascii.unhexlify(extended_key1)).hexdigest()
                second_sha2561 = hashlib.sha256(binascii.unhexlify(first_sha2561)).hexdigest()
                final_key1 = extended_key1+second_sha2561[:8]
                WIF = base58.b58encode(binascii.unhexlify(final_key1))
                alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
                c = '0'; byte = '00'; zero = 0
                var = hashlib.new('ripemd160')
                var.update(hashlib.sha256(binascii.unhexlify(publickey.encode())).digest())
                a = (byte + var.hexdigest())
                doublehash = hashlib.sha256(hashlib.sha256(binascii.unhexlify(a.encode())).digest()).hexdigest()
                address = a + doublehash[0:8]
                for char in address:
                    if (char != c):
                        break
                    zero += 1
                zero = zero // 2
                n = int(address, 16)
                output = []
                while (n > 0):
                      n, remainder = divmod (n, 58)
                      output.append(alphabet[remainder])
                count = 0
                while (count < zero):
                    output.append(alphabet[0])
                    count += 1
                address = ''.join(output[::-1])
                print("Mnemonic code word: " + ' ' + str(xa)+ "\n" + str(address)+ ' ' + str(WIF)+ "\n")
                file = open('harvest1', 'a')
                file.write("Mnemonic code word: " + ' ' + str(xa)+ "\n" + str(address)+ ' ' + str(WIF)+ "\n"+ "\n")
                file.close()
                with open("data-base1", "r") as m:
                    add = m.read().split()
                    for ad in add:
                        continue
                    if address in add:
                        print("Found: " + ' ' +str(address))
                        data = open("Win1.txt","a")
                        data.write("found " + str(xa)+"\n" +str(address)+"\n"+str(WIF)+"\n"+"\n")
                        data.close()
                
                     
  


main()
