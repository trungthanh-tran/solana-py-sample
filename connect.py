import asyncio
from solana.rpc.async_api import AsyncClient

ENDPOINT_MAIN = "https://api.mainnet-beta.solana.com"
ENDPOINT_TESTNET = "https://api.testnet.solana.com"
ENDPOINT_DEVNET = "https://api.devnet.solana.com"

async def main():
    async with AsyncClient(ENDPOINT_MAIN) as client:
        res = await client.is_connected()
    print(res)  # True

    # Alternatively, close the client explicitly instead of using a context manager:
    client = AsyncClient(ENDPOINT_MAIN)
    res = await client.is_connected()
    print(res)  # True
    await client.close()

asyncio.run(main())