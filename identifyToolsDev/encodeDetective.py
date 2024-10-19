import chardet

#Raw Data
response_bytes = b'\xe4\xbd\xa0\xe5\xa5\xbd'  

# Indentify Decode Type 
result = chardet.detect(response_bytes)
encoding = result['encoding']
confidence = result['confidence']

print(f"Detected encoding: {encoding} with confidence {confidence}")

# Decode it !
decoded_content = response_bytes.decode(encoding)
print(decoded_content)