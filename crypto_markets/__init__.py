import json
from enum import IntEnum
from typing import Any, Dict, List, Optional

from crypto_markets._lowlevel import ffi, lib


class MarketType(IntEnum):
    '''Market type.'''
    unknown = lib.Unknown
    spot = lib.Spot
    linear_future = lib.LinearFuture
    inverse_future = lib.InverseFuture
    linear_swap = lib.LinearSwap
    inverse_swap = lib.InverseSwap

    american_option = lib.AmericanOption
    european_option = lib.EuropeanOption

    quanto_future = lib.QuantoFuture
    quanto_swap = lib.QuantoSwap

    move = lib.Move
    bvol = lib.BVOL


def fetch_markets(exchange: str,
                  market_type: MarketType) -> List[Dict[str, Any]]:
    json_ptr = lib.fetch_markets(
        ffi.new("char[]", exchange.encode("utf-8")),
        market_type.value,
    )
    if json_ptr == ffi.NULL:
        return []
    try:
        # Copy the data to a python string, then parse the JSON
        return json.loads(ffi.string(json_ptr).decode('UTF-8'))
    finally:
        lib.deallocate_string(json_ptr)
