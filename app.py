#!/usr/bin/env python3

from crawler import filter_network_packet

def main():
    res = filter_network_packet('https://www.aponet.de/apotheke/notdienstsuche/Berlin/%20/5', r'https://www\.aponet\.de/apotheke/notdienstsuche\?tx_aponetpharmacy_search')
    print(f"Response Status Code: {res.status_code}")
    print(res.text)

if __name__ == "__main__":
    main()