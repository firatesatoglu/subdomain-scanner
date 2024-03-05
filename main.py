from plugins.bevigil_subscanner import bevigil_subscanner
from plugins.crtsh_subscanner import crt_sh_subscanner
from plugins.dnsrepo_subscanner import dnsrepo_subscanner
from plugins.hackertarget_subscanner import hackertarget_subscanner
from plugins.rapiddns_subscanner import rapiddns_subscanner
from plugins.securitytrails_subscanner import securitytrails_subscanner
from plugins.shodan_subscanner import shodan_subscanner
from plugins.sslmate_subscanner import sslmate_subscanner
from plugins.subdomainfinderio_subscanner import subdomainfinderio_subscanner
from plugins.threadcrowd_subscanner import threadcrowd_subscanner
from plugins.virustotal_subscanner import virustotal_subscanner
from plugins.webarchive_subscanner import webarchive_subscanner
from plugins.whoxml_subscanner import whoxml_subscanner

from datetime import datetime
import argparse
import pprint

# import socket
# def get_ip_address(subdomain):
#     try: return socket.gethostbyname(subdomain)
#     except: return None

def run_search(keyword):
    subdomain_list = []

    # subdomain_list.extend(bevigil_subscanner(keyword))
    # subdomain_list.extend(crt_sh_subscanner(keyword))
    # subdomain_list.extend(dnsrepo_subscanner(keyword))
    subdomain_list.extend(hackertarget_subscanner(keyword))
    # subdomain_list.extend(rapiddns_subscanner(keyword))
    # subdomain_list.extend(securitytrails_subscanner(keyword))
    # subdomain_list.extend(shodan_subscanner(keyword))
    # subdomain_list.extend(sslmate_subscanner(keyword))
    # subdomain_list.extend(subdomainfinderio_subscanner(keyword))
    # subdomain_list.extend(threadcrowd_subscanner(keyword))
    # subdomain_list.extend(virustotal_subscanner(keyword))
    # subdomain_list.extend(webarchive_subscanner(keyword))
    # subdomain_list.extend(whoxml_subscanner(keyword))

    subdomain_list= list(set(subdomain_list))
    subdomain_list.sort()

    pprint.pprint(subdomain_list)
    print(f"Total subdomains found: {len(subdomain_list)}")

argparser = argparse.ArgumentParser(description="Awasome Subdomain Finder")
argparser.add_argument("keyword", help="Keyword to search subdomains")
args= argparser.parse_args()

if __name__ == "__main__":
    run_search(args.keyword)