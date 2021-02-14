"""
    sockets=1.0.0
"""
import sys
import socket
from typing import List


def get_website_ip(sites: List[str]) -> dict:
    """
        Obtain ip by site name
    """
    try:
        result: dict = {}
        for site in sites:
            ip = socket.gethostbyname(site)
            print(f"ip of {site} is: {ip} ")
            result[site] = ip
        return result
    except:
        print("\nExiting...")
        sys.exit(0)


if __name__ == "__main__":
    sites: List[str] = [
        'www.facebook.com',
        'www.instagram.com',
        'www.google.com',
        'www.netflix.com',
    ]
    get_website_ip(sites)
