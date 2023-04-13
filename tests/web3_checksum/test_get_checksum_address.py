import web3
from src.web3_checksum.get_checksum_address import get_checksum_address

correct_address = '0x4D49fa868E8d2d868E9e00db733791ed149a8928'
private_key = '0xbe920ee2705cb1c1e69b47fe3785a7279103a2202912b903c1ed0fe53115e5fd'
incorrect_address = correct_address.lower()


def test_private_key_case():
    assert (get_checksum_address(private_key=private_key) == correct_address)


def test_account_case():
    assert (get_checksum_address(account=web3.Account.from_key(private_key)) == correct_address)


def test_address_case():
    assert (get_checksum_address(address=incorrect_address) == correct_address)
