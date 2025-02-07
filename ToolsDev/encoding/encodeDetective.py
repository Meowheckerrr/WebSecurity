import chardet

# 假設文件名是字節字符串，這是 HTTP 返回的文件名
filename_bytes = bytes.fromhex("30 32 2E AA 4C A7 BB A9 F7 B4 5F BC 66 B5 AA C5 47 AE D1 28 B5 6F A4 E5")

# 使用 chardet 檢測編碼
result = chardet.detect(filename_bytes)
encoding = result['encoding']

if encoding:
    try:
        filename = filename_bytes.decode(encoding)
        print(f"解碼後的文件名: {filename}")
    except UnicodeDecodeError:
        print(f"無法使用檢測到的編碼 ({encoding}) 進行解碼。")
else:
    print("無法檢測到有效的編碼。")