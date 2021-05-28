"""Functions for processing network related tasks
"""
__copyright__ = "Copyright (C) 2021  Matt Ferreira"
__license__ = "Apache License"

import re

from sectools.regex import IP_ADDRESS

def extract_ips(text):
    """Given a string extract all the ip addresses
    
    args:
        text (str): String to extract ip addresses from

    return (list): List of IP Addresses
    """
    ip_addr_re = re.compile(IP_ADDRESS)

    ips = ip_addr_re.findall(text)
    
    return ips
    