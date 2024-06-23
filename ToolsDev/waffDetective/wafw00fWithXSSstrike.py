import csv
import os
import re

originalcsvPath = "./target.csv"
filteredcsvPath= "./validomain.csv"

columnsNum = 6
urls = []
NoWafList = []


# Extracting Domain (http/https) 

with open(originalcsvPath, 'r') as f:
    lines = f.readlines()
    result = [line for line in lines if 'http' in line] #[line ...]： -> (for line in lines if 'http' in line) -> [line, line, line]
    print(result)

with open(filteredcsvPath, 'w') as f:
    for line in result:
        f.write(line)
print(result)

# Reading CSV files
with open(filteredcsvPath, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip Header title 
    for row in csvreader:
        if len(row) > columnsNum:
            value = row[columnsNum]
            urls.append(value)
print(urls)

# WAF exists? 
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
# WAF lists
print("No WAF detected list:", NoWafList)

with open("./NoWAFlist.txt", 'w') as f:
    for url in NoWafList:
        f.write(url + '\n')

# XssTrike (work)

vulUrlpattern  = re.compile(r'Vulnerable webpage: (.+)') ##rules 
xssPayload_pattern  = re.compile(r'Vector for (.+)')

for refXssTestUrl in NoWafList:

    xssOutput = os.popen(f'python3 xsstrike.py -u {refXssTestUrl} --crawl -l 4 --proxy -t 10').read() ##NO WAF XSS


    VulUrlmatch = vulUrlpattern.search(xssOutput)
    xssPayloadmatch = xssPayload_pattern.search(xssOutput)
    
    if VulUrlmatch :
        print(f"Vulnerable webpage:,{VulUrlmatch.group(0)} ->  {xssPayloadmatch.group(0)}")
    else :
        print("No REf XSS",{refXssTestUrl})
