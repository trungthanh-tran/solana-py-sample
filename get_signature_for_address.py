from solana.rpc.api import Client
from solders.pubkey import Pubkey
from solders.rpc.responses import GetSignaturesForAddressResp,RpcConfirmedTransactionStatusWithSignature

# Initialize the client
client = Client("https://api.mainnet-beta.solana.com")

# Define the address you want to query
address = "BVG3BJH4ghUPJT9mCi7JbziNwx3dqRTzgo9x5poGpump"
# Get pubkey
pubkey = Pubkey.from_string(address)
# Fetch the signatures
responses = client.get_signatures_for_address(pubkey, limit=10)

rpcs = responses.value

for rpc in rpcs:
    print (rpc)