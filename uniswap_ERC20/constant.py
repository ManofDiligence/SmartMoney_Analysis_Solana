from web3 import Web3

# RPC endpoints
RPC = {
    # Found on https://ethereumnodes.com/
    'mainnet': 'https://cloudflare-eth.com/',
    # Found on https://www.allthatnode.com/polygon.dsrv 
    'polygon': 'https://polygon-mainnet-rpc.allthatnode.com:8545',
    # Found on https://umbria.network/connect/ethereum-testnet-g%C3%B6rli
    'goerli': 'https://eth-goerli.public.blastapi.io'
    }


# ERC20 token info

WETH = {
    
    'mainnet': {
        'symbol': 'WETH',
        'address': Web3.to_checksum_address(
            '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'
            ),
        'decimals': 18
        },
    'polygon': {
        'symbol': 'WETH',
        'address': Web3.to_checksum_address(
            '0x7ceb23fd6bc0add59e62ac25578270cff1b9f619'
            ),
        'decimals': 18
        },
    'goerli' :{
        'symbol': 'WETH',
        'address': Web3.to_checksum_address(
            '0xb4fbf271143f4fbf7b91a5ded31805e42b2208d6'
            ),
        'decimals': 18
    }
    }
LINK = {
    # 0x326c977e6efc84e512bb9c30f76e30c160ed06fb
    'goerli' :{
        'symbol': 'LINK',
        'address': Web3.to_checksum_address(
            '0x326c977e6efc84e512bb9c30f76e30c160ed06fb'
            ),
        'decimals': 18
    }
}

WBTC = {
    'mainnet': {
        'symbol': 'WBTC',
        'address' : Web3.to_checksum_address(
            '0x2260fac5e5542a773aa44fbcfedf7c193bc2c599'
            ),
        'decimals': 8
        },
    'polygon': {
        'symbol': 'WBTC',
        'address' : Web3.to_checksum_address(
            '0x1bfd67037b42cf73acf2047067bd4f2c47d9bfd6'
            ),
        'decimals': 8
        }
    }

USDC = {
    'mainnet': {
        'symbol': 'USDC',
        'address' : Web3.to_checksum_address(
            '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'
            ),
        'decimals': 6
        },
    'polygon': {
        'symbol': 'USDC',
        'address' : Web3.to_checksum_address(
            '0x2791bca1f2de4661ed88a30c99a7a9449aa84174'
            ),
        'decimals': 6
        }
    }

USDT = {
    'mainnet': {
        'symbol': 'USDT',
        'address' : Web3.to_checksum_address(
            '0xdAC17F958D2ee523a2206206994597C13D831ec7'
            ),
        'decimals': 6
        },
    'polygon': {
        'symbol': 'USDT',
        'address' : Web3.to_checksum_address(
            '0xc2132d05d31c914a87c6611c10748aeb04b58e8f'
            ),
        'decimals': 6
        },
    'goerli' :{
        'symbol': 'USDT',
        'address': Web3.to_checksum_address(
            '0xe583769738b6dd4E7CAF8451050d1948BE717679'
            ),
        'decimals': 18
    }
    }

DAI = {
    'mainnet': {
        'symbol': 'DAI',
        'address' : Web3.to_checksum_address(
            '0x6b175474e89094c44da98b954eedeac495271d0f'
            ),
        'decimals': 18
        },
    'polygon': {
        'symbol': 'DAI',
        'address' : Web3.to_checksum_address(
            '0x8f3cf7ad23cd3cadbd9735aff958023239c6a063'
            ),
        'decimals': 18
        }
    }