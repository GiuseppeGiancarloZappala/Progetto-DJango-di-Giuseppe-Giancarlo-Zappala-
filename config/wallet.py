from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/93d262c2238643a684d464fda6ab67f8'))
account = w3.eth.account.create()
privateKey = account.privateKey.hex()
address = account.address

print (f"L'indirizzo è {address}\n La chiave: {privateKey}")