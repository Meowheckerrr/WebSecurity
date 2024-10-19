import csv
import os
import re

columnsNum = 2
urls = []
NoWafList = []

# 讀取 CSV 檔案並提取第三個欄位 (Domain)
with open('testing.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # 跳過標題行

    for row in csvreader:
        value = row[columnsNum]
        urls.append(value)

print(urls)

# WAF 檢測
pattern = re.compile(r'No WAF detected')


for url in urls:
    output = os.popen(f'wafw00f {url}').read()
    
    
    # Match Pattern 
    
    match = pattern.search(output)
    if match:
        print(f"No WAF detected: {url}")
        NoWafList.append(url)
    else:
        print(f"WAF detected or other result for {url}")

# WAF list 
print("No WAF detected list:", NoWafList)