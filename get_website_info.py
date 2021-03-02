"""
    sockets=1.0.0
"""
import sys
import json
import socket
from typing import List
from urllib.request import urlopen, Request


def get_website_info(sites: List[str]) -> dict:
    """
        Obtain site info by site name
    """
    GEO_IP_API_URL = 'http://ip-api.com/json/'
    try:
        result: dict = {}
        for site in sites:
            ip = socket.gethostbyname(site)
            req = Request(GEO_IP_API_URL+ip)
            response = urlopen(req).read()
            json_response = json.loads(response.decode('utf-8'))
            result_response = {
                'ip': ip,
                'city': json_response['city'],
                'region': json_response['regionName'],
                'country': json_response['country']
            }
            print(f"site:      {site}")
            print(f"ip:        {ip}")
            print(f"city:      {result_response['city']}")
            print(f"region:    {result_response['region']}")
            print(f"country:   {result_response['country']}")
            print(f"---------------------------------------")
            result[site] = result_response
        return result
    except Exception as e:
        print('error:', e)
        print("\nExiting...")
        sys.exit(0)


if __name__ == "__main__":
    sites: List[str] = [
        'www.facebook.com',
        'www.instagram.com',
        'www.google.com',
        'www.netflix.com',
    ]
    (get_website_info(sites))
