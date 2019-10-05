#! /usr/bin/env python
"""
Usage: Base Features for SFDC Interaction

"""
CISCO_CEC_USERNAME = 'adallah'
CISCO_CEC_PASSWORD = 'Naya2009$'

SALESFORCE_ENDPOINT = "ciscosales.my.salesforce.com"
BDB_AUTH_URL = "https://{username}:{password}@scripts.cisco.com/api/v2/auth/login"

USER_SOQL = """
    SELECT
        Id
    FROM User
    WHERE Email in ({item}) or Username in ({item})
"""

DEAL_SOQL = """
        SELECT
            Id,
            Name,
            SE_Status__c
        FROM Opportunity
        WHERE DealID__c in ({item})
"""

OP_RES_SOQL = """
        SELECT
            ID,
            Resource_Username__c,
            Resource_Name__c
        FROM Resource_Request_Assignment__c
        WHERE Opportunity_Name__c in ({item})
"""

NAME_SOQL = """
    SELECT
        Name
    FROM User
    WHERE Id in ({items})
"""

import time
import sys
import os
from webdriver_manager.chrome import ChromeDriverManager
from pprint import pprint
from selenium import webdriver
from simple_salesforce import Salesforce

from typing import (
    Tuple,
    Iterable,
    Dict,
    Any,
    List,
    Union,
    Optional,
    Sequence,
    Iterator,
    Type,
    TypeVar,
    Callable,
)

SFDCType = Iterator[Dict[str, Any]]

class CiscoError(Exception):
    pass


class CookieNotFound(CiscoError):
    pass


def get_sid_cookie(username: str, password: str) -> str:
    """Retrieves Salesforce session id (sid) using Cisco CEC credentials

    Args:
        username: Cisco CEC username
        password: Cisco CEC password

    Returns:
        session id (sid) cookie
    """

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    #driver = webdriver.Chrome(chrome_options=options, executable_path='/usr/bin/chromedriver')

    url = BDB_AUTH_URL.format(username=username, password=password)
    driver.get(url)
    cisco_sso_cookie = driver.get_cookie("ObSSOCookie")
    if not cisco_sso_cookie:
        raise CookieNotFound("Authentication Fail")

    driver.get(f"https://{SALESFORCE_ENDPOINT}")
    time.sleep(0.5)
    driver.get(f"https://{SALESFORCE_ENDPOINT}/404")
    sid_cookie = driver.get_cookie("sid")
    driver.quit()
    if not sid_cookie:
        raise CookieNotFound("SFDC Login Fail")
    return sid_cookie["value"]

def get_salesforce_connector(sid: str = None) -> Salesforce:
    """Returns Salesforce object which can be queried

    Args:
        sid: salesforce sid cookie

    Returns:
        Salesforce object
    """

    if sid is None:
        sid = get_sid_cookie(
            username=CISCO_CEC_USERNAME,
            password=CISCO_CEC_PASSWORD,
        )

    return Salesforce(instance=SALESFORCE_ENDPOINT, session_id=sid, version="43.0")


def get_sfdc_records(salesforce_api: Salesforce, soql_query: str) -> SFDCType:
    """Returns records list with OrderedDict

    Args:
        salesforce_api: Salesforce object soql_query: SOQL query string

    Returns:
        SFDC Iterator[Dict[str, Any]]
    """
    records = salesforce_api.query_all(soql_query)["records"]
    return records

def get_sfdc_records_by_items_list(
    salesforce_api: Salesforce, soql_query: str, items: Iterable[str]) -> SFDCType:
    soql_items = ", ".join("'{}'".format(item) for item in items)
    soql_query = soql_query.format(items=soql_items)
    #print(soql_query)
    return get_sfdc_records(salesforce_api, soql_query)

def get_sfdc_records_by_item(
    salesforce_api: Salesforce, soql_query: str, item: str) -> SFDCType:
    soql_item = "'{}'".format(item)
    soql_query = soql_query.format(item=soql_item)
    #print(soql_query)
    return get_sfdc_records(salesforce_api, soql_query)


def sync_from_sfdc_by_item(salesforce_api, soql_str, item):
    data = get_sfdc_records_by_item(
            salesforce_api, soql_str, item
    )
    return data

def sync_from_sfdc_by_items_list(salesforce_api, soql_str, items):
    data = get_sfdc_records_by_items_list(
            salesforce_api, soql_str, items
    )
    return data


def get_id(data):
    try:
        return(data[0]["Id"])
    except:
        raise CiscoError("ID not found.\n Please check that the Deal ID/User is valid.")

def get_names(data):
    aux_list = []
    for i in range(0,len(data)):
        aux_list.append(data[i]["Name"])

    return aux_list

def get_rescource_names(data):
    ressource_name_set = set()
    for i in range(0, len(data)):
        if (data[i]["Resource_Name__c"] != None):
            ressource_name_set.add(data[i]["Resource_Name__c"])
    return ressource_name_set


def show_deal_id(salesforce_connector, deal_id):

    invalid_msg = "Sorry, Deal ID not found!"
    try:
        print("INFO: Getting USER ID...")
        deal_id_data = sync_from_sfdc_by_item(salesforce_connector, DEAL_SOQL, deal_id)
        #user_id = get_id(user_id_data)
        return deal_id_data
    except:
        return invalid_msg

def show_others(salesforce_connector, deal_id):

    invalid_msg = "Sorry, Deal ID not found!!  am not working at all "+ deal_id
    try:
        print("INFO: Map DEAL ID to OPPORTUNITY ID...")
        deal_id_data = sync_from_sfdc_by_item(salesforce_connector, DEAL_SOQL, deal_id)
        opportunity_id = get_id(deal_id_data)
        opportunity_names = get_names(deal_id_data)
        #print(opportunity_id)
    except:
        return invalid_msg

    for opportunity_name in opportunity_names:
        print("INFO: Getting OPPORTUNITY RESOURCES...")
        deal_id_data = sync_from_sfdc_by_item(salesforce_connector, OP_RES_SOQL, opportunity_id)
        resource_name_set = get_rescource_names(deal_id_data)
        #print(resource_name_set)

        if deal_id_data:
            print("INFO: Getting USER NAME...")
            user_name_data = sync_from_sfdc_by_items_list(salesforce_connector, NAME_SOQL, resource_name_set)
            #print(user_name_data)

            return user_name_data
        else:
            return "Sorry, no records found."

def main(did):
    print("\nINFO: Getting SID Cookie for {}".format(CISCO_CEC_USERNAME))
    sid_cookie = get_sid_cookie(CISCO_CEC_USERNAME, CISCO_CEC_PASSWORD)
    #print(sid_cookie)

    print("INFO: Connecting to SFDC...")
    salesforce_connector = get_salesforce_connector(sid_cookie)
    #print(salesforce_connector)

    id = show_deal_id(salesforce_connector,did)
    print(id)
    ses = show_others(salesforce_connector,did)
    print(ses)
    res = {
        'msg' : id,
        'more' : ses
    }
    return res


if __name__ == '__main__':
    main()


   
