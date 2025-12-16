import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crypto_agama.agama_trezor import t_connect,t_connect_first, get_btc_address


print("[ start] ")
print("You must have your Trezor (electronic hardware wallet) connected")
client = t_connect_first() # get_default_client()

print("="*50)

address, path = get_btc_address(client,show_disp=False)
print(path, "default bitcoin SPENDADDRESS address 0:", address) # SPENDADDRESS: 1/16Mk...
print("-"*50)

address, path = get_btc_address(client,"SPENDP2SHWITNESS",1)
print(path, "bitcoin SPENDP2SHWITNESS address:", address) # SPENDP2SHWITNESS: 1/16Mk...
print("-"*50)

address, path = get_btc_address(client,"SPENDWITNESS",0)
print(path, "bitcoin SPENDWITNESS address:", address) # SPENDWITNESS: 1/16Mk...
print("-"*50)

address, path = get_btc_address(client,"SPENDTAPROOT",1)
print(path, "bitcoin SPENDTAPROOT address:", address) # SPENDTAPROOT: 1/16Mk...
print("-"*50)


"""
You must have your Trezor (electronic hardware wallet) connected
------------------------------------------------------------
- connecting to Trezor (get_default_client)


44'/0'/0'/0/0 default bitcoin SPENDADDRESS address 0: 16MkCp4e3sSCc...8ZKJ7BBZ9dHhV - LEGACY ACCOUNTS ok
--------------------------------------------------
49'/0'/0'/0/0 bitcoin SPENDP2SHWITNESS address:       3DSrzWmuP31W9...eEMJWGEqrkxFj - LEGACY SEGWIT ACCOUNTS ok
--------------------------------------------------
84'/0'/0'/0/0 bitcoin SPENDWITNESS address:           bc1qdkknh0drn...fmxzwsrp80cnp - DEFAULT ACCOUNTS ok
--------------------------------------------------
86'/0'/0'/0/1 bitcoin SPENDTAPROOT address:           bc1pq37dqchmun...hnlgdwrxwssuxkzw - 1 ok / 0?

"""



print("ok, finish")
