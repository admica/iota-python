# -*- coding: utf-8 -*-

import iota
from iotapy.storage import converter

HASH_TRITS_LENGTH = 243
TRANSACTION_TRITS_LENGTH = 8019


def get_key(bytes_: bytes):
    # Convert key bytes to iota.TransactionHash
    if not isinstance(bytes_, bytes):
        raise TypeError

    key = iota.TransactionHash.from_trits(converter.from_binary_to_trits(bytes_, 243))
    return key


def get(bytes_: bytes):
    if bytes_ is None:
        return None
    if not isinstance(bytes_, bytes):
        raise TypeError

    ti = converter.from_binary_to_trits(bytes_, TRANSACTION_TRITS_LENGTH)
    return iota.Transaction.from_tryte_string(iota.TryteString.from_trits(ti), bytes_)


def save(value: iota.Transaction):
    if not value:
        return b''

    return converter.from_trits_to_binary(value.as_tryte_string().as_trits())
