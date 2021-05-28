"""Collection of commonly used regular expressions.
"""
__copyright__ = "Copyright (C) 2021  Matt Ferreira"
__license__ = "Apache License"

# Networking
IP_ADDRESS = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
MAC_ADDRESS = r'((?:[A-F0-9a-f]{2}[:-]){5}(?:[A-F0-9a-f]{2}))'

# Personally Identifiable Information (PII)
SSN = r'(sn|soc|social|ssn|=|\+|_|\#|:|;|\.|-|\s|^){1,3}\d{3}(=|\+|_|\#|:|;|\.|-|\s){1,3}\d{2}(=|\+|_|\#|:|;|\.|-|\s){1,3}\d{4}(sn|soc|social|ssn|=|\+|_|\#|:|;|\.|-|\s|$){1,3}'

# Credit Cards
MASTERCARD = r'(\W|^)5[1-5][0-9]{2}[\s-]{1}\d{4}[\s-]{1}\d{4}[\s-]{1}\d{4}[\s.-]{1}(\W|$)'
VISA = r'(\W|^)4[0-9]{3}[\s-]{1}\d{4}[\s-]{1}\d{4}[\s-]{1}\d{4}[\s.-]{0,1}(\W|$)'
DISCOVER = r'(\W|^)6(?:011|5[0-9]{2})[\s-]{1}\d{4}[\s-]{1}\d{4}[\s-]{1}\d{4}[\s.-]{0,1}(\W|$)'
AMEX = r'(\W|^)[#\-]{0,1}\s{0,1}\d{4}[\s-]{1}\d{6}[\s-]{1}\d{5}[\s.-]{0,1}(\W|$)'

# CURRENCY
US_CURRENCY = r'\$?(?:[0-9]{1,3},(?:[0-9]{3},)*[0-9]{3}|[0-9]+)(?:\.[0-9][0-9])?)'

# Other
EMAIL_ADDRESS = r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'