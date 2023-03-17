from web3 import Web3, HTTPProvider
from web3.contract import Contract
from explorer_utils import fmt_hash, fmt_hash_str
import requests
import json

INFURA_API_KEY = open('api_secret.txt', 'r').read().strip()
# note: you will need to create a file called api_secret.txt or you will get this error:
# FileNotFoundError: [Errno 2] No such file or directory: 'api_secret.txt'

RPC_URL = f"https://mainnet.infura.io/v3/{INFURA_API_KEY}"

ABI_ERC721 = open('abi_erc721.json', 'r').read().strip()
NFT_COLLECTION_ADDRESS = "0x7D8820FA92EB1584636f4F5b8515B5476B75171a" # Murakami Flowers
TRANSACTION_ID = "0x0a8d164829769eefeff1aebe125f711e79094d1827c0e2b41f7ceecb85317a7e" # Murakami Flowers NFT transfer transaction

w3 = Web3(HTTPProvider(RPC_URL))
eth = w3.eth

if w3.isConnected():
  print("ETH node connection ok")

# ----

# get the most recent block
block_latest = eth.get_block('latest')