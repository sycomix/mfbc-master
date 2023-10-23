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







def main():
    fobj = "dictionary.txt"
    while True:
        file = open(fobj, "r")
        choices=[]
        with file as f:
            words = f.read().split()
            for word in words:
                x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
                xa = random.choice(x)
                sent = [random.choice(words) for _ in range(int(xa))]
                if sent not in choices:
                    choices.append(sent)
                    sect = ' '.join(sent)
                    pvt1 = hashlib.sha256(sect.encode("utf-8")).hexdigest()
                    privatekey1 = binascii.unhexlify(pvt1)
                    s = ecdsa.SigningKey.from_string(privatekey1, curve = ecdsa.SECP256k1)
                    publickey = '04' + binascii.hexlify(s.verifying_key.to_string()).decode('utf-8')
                    extended_key1 = f"80{pvt1}"
                    first_sha2561 = hashlib.sha256(binascii.unhexlify(extended_key1)).hexdigest()
                    second_sha2561 = hashlib.sha256(binascii.unhexlify(first_sha2561)).hexdigest()
                    final_key1 = extended_key1+second_sha2561[:8]
                    WIF = base58.b58encode(binascii.unhexlify(final_key1))
                    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
                    c = '0'
                    zero = 0
                    var = hashlib.new('ripemd160')
                    var.update(hashlib.sha256(binascii.unhexlify(publickey.encode())).digest())
                    a = f'00{var.hexdigest()}'
                    doublehash = hashlib.sha256(hashlib.sha256(binascii.unhexlify(a.encode())).digest()).hexdigest()
                    address = a + doublehash[:8]
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
                    print(
                        "Mnemonic code word: "
                        + ' '
                        + sect
                        + "\n"
                        + address
                        + ' '
                        + str(WIF)
                        + "\n"
                    )
                    with open('harvest', 'a') as file:
                        file.write(
                            "Mnemonic code word: "
                            + ' '
                            + sect
                            + "\n"
                            + address
                            + ' '
                            + str(WIF)
                            + "\n"
                            + "\n"
                        )
                    with open('addr-uncheck', 'a') as file:
                        file.write(f'{address} ')
                    with open("data-base", "r") as m:
                        add = m.read().split()
                        for _ in add:
                            continue
                        if address in add:
                            print("Found: " + ' ' + address)
                            with open("Win.txt","a") as data:
                                data.write(f"found {sect}" + "\n" + address + "\n" + str(WIF) + "\n" + "\n")
                
                     
  


if __name__ == '__main__':
    thread = int(input("Enter number of thread's here: "))
    for _ in range(thread):
        multiprocessing.Process(target = main).start()
        
