# Convert hex to base64
# The string:
# 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# Should produce:
# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t

import pybase64

def hexTobase64(hex):
    decoded_hex = bytes.fromhex(hex)
    encoded_b64 = pybase64.b64encode(decoded_hex)
    return encoded_b64.decode()


# x = hexTobase64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
# print(x)
