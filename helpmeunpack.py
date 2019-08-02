import requests 
from base64 import b64decode
import struct

# Get input data.
response = requests.get('https://hackattic.com/challenges/help_me_unpack/problem?access_token=96d50621d8c2e08d')
response_dict = response.json()

# Get the base64 encoded string and decode.
encoded_string = response_dict['bytes']
decoded_string = b64decode(encoded_string)

# Unpack the data.
unpacked_data = struct.unpack('iIhfdd', decoded_string)
# print(unpacked_data)

# Send the answer.
post_object = requests.post('https://hackattic.com/challenges/help_me_unpack/solve?access_token=96d50621d8c2e08d', 
    json = {
        'int':unpacked_data[0],
        'uint':unpacked_data[1],
        'short':unpacked_data[2],
        'float':unpacked_data[3],
        'double':unpacked_data[4],
        'big_endian_double':unpacked_data[4]
        })

# Check the answer.
print(post_object.json())