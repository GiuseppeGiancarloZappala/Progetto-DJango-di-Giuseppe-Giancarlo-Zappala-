from web3 import Web3


def sendTransactions(message):
    w3=Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/93d262c2238643a684d464fda6ab67f8'))
    address='0x0b4576b8A35c9E4D4D8C8fCc36A5b90FC53fa8E3'
    privateKey='0xf9019bc7675452732d28eead62348999e5875f7d439842eb2dec547bf278cc98'
    nonce=w3.eth.getTransactionCount(address)
    gasPrice=w3.eth.gasPrice
    value=w3.toWei(0,'ether')
    signedTx=w3.eth.account.signTransaction(dict(
        nonce=nonce,
        gasPrice=gasPrice,
        gas=100000,
        to='0x0000000000000000000000000000000000000000',
        value=value,
        data=message.encode('utf-8')
    ), privateKey)

    Tx=w3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId=w3.toHex(Tx)
    return txId
