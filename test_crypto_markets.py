#!/usr/bin/env python3

from crypto_markets import MarketType, fetch_markets


def test_fetch_markets():
    json_arr = fetch_markets("binance", MarketType['inverse_swap'])
    assert len(json_arr) > 0
    market = json_arr[0]
    assert market['exchange'] == 'binance'
    assert market['market_type'] == 'inverse_swap'
