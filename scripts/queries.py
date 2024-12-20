query_telecom_data = """ 
    SELECT 
    "Bearer Id", 
    "Handset Type",
    "Handset Manufacturer",
    "IMSI",
    "MSISDN/Number",
    "Dur. (ms)",
    "Total DL (Bytes)",
    "Total UL (Bytes)",
    "Social Media DL (Bytes)",
    "Social Media UL (Bytes)",
    "Google DL (Bytes)",
    "Google UL (Bytes)",
    "Email DL (Bytes)",
    "Email UL (Bytes)",
    "YouTube DL (Bytes)",
    "YouTube UL (Bytes)",
    "Netflix DL (Bytes)",
    "Netflix UL (Bytes)",
    "Gaming DL (Bytes)",
    "Gaming UL (Bytes)",
    "Other DL",
    "Other UL"
FROM public.xdr_data;  
"""
