#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Made by Ano Mobb
# MultiFunction Bitcoin Cracker/ mfbc
# 

try:
    import hashlib, random, os, base64, binascii, ecdsa, base58, secrets, time, hmac, multiprocessing 
except ImportError:
    import subprocess
    subprocess.check_call(["python", '-m', 'pip', 'install', 'base58==1.0.0'])
    subprocess.check_call(["python", '-m', 'pip', 'install', 'ecdsa==0.13'])



loop = True




                                                                                                   
                                
def main():
    alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    while loop:
        privatekey = binascii.hexlify(os.urandom(32)).decode('utf-8').upper()
        pubkey = binascii.unhexlify(privatekey)
        s = ecdsa.SigningKey.from_string(pubkey, curve = ecdsa.SECP256k1)
        publickey = '04' + binascii.hexlify(s.verifying_key.to_string()).decode('utf-8')
        output = []
        var = hashlib.new('ripemd160')
        var.update(hashlib.sha256(binascii.unhexlify(publickey.encode())).digest())
        var = f"00{var.hexdigest()}{hashlib.sha256(hashlib.sha256(binascii.unhexlify(f'00{var.hexdigest()}'.encode())).digest()).hexdigest()[:8]}"
        count = [char != '0' for char in var].index(True) // 2
        n = int(var, 16)
        while n > 0:
            n, remainder = divmod(n, 58)
            output.append(alphabet[remainder])
        output.extend(alphabet[0] for _ in range(count))
        address = ''.join(output[::-1])
        extended_key = f"80{privatekey}"
        first_sha2561 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()
        second_sha2561 = hashlib.sha256(binascii.unhexlify(first_sha2561)).hexdigest()
        final_key = extended_key+second_sha2561[:8]
        WIF = base58.b58encode(binascii.unhexlify(final_key))
        database = open("data-base", "r")
        database.read().split()
        with open("data-base", "r") as m:
            add = m.read().split()
            for _ in add:
                continue
            if address in add:
                print("Found: " + ' ' + address)
                with open("Win.txt","a") as data:
                    data.write(
                        f"found {str(sect)}"
                        + "\n"
                        + address
                        + "\n"
                        + str(WIF)
                        + "\n"
                        + "\n"
                    )
            else: 
                print(f'{address} {str(WIF)}')


             

if __name__ == '__main__':
    thread = int(input("Enter number of thread's here: "))
    for _ in range(thread):
        multiprocessing.Process(target = main).start()
    
