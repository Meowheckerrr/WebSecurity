
import urllib.parse

decodeText = "%B0%AA%B6%AF%A5%AB"

encodeText = "Meow"
# decoding 
try:
    decoded_text = urllib.parse.unquote_to_bytes(decodeText).decode('cp950', errors='replace')
    # decoded_text = urllib.parse.unquote_to_bytes(decodeText).decode('big5', errors='replace')
except Exception as e:
    decoded_text = str(e)

# # Encoding 
# encodeText = urllib.parse.unquote_to_bytes(encodeText).encode('cp950',errors='replace')


print(decoded_text)
