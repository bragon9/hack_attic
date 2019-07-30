import requests 
from base64 import b64decode
import struct

response = requests.get('https://hackattic.com/challenges/help_me_unpack/problem?access_token=96d50621d8c2e08d')

response_dict = response.json()

encoded_string = response_dict['bytes']
decoded_string = b64decode(encoded_string)

# int: the signed integer value
# uint: the unsigned integer value
# short: the decoded short value
# float: surprisingly, the float value
# double: the double value - shockingly
# big_endian_double: you get the idea by now!

# 'iIhfdd'

unpacked_data = struct.unpack('iIhfdd', decoded_string)

print(unpacked_data)

post_object = requests.post('https://hackattic.com/challenges/help_me_unpack/solve?access_token=96d50621d8c2e08d', 
    json = {
        'int':unpacked_data[0],
        'uint':unpacked_data[1],
        'short':unpacked_data[2],
        'float':unpacked_data[3],
        'double':unpacked_data[4],
        'big_endian_double':unpacked_data[5]
        })

print(post_object.json())