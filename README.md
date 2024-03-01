# Awasome Subdomain Scanner
This tool is a subdomain scanner that uses multiple sources to find subdomains. Tool offers a fast and effective way to collect subdomains. It collects information by crawling some special services and using API endpoints with some other services.

Some of the subdomain sources are as follows: **bevigil, crtsh, dnsrepo, hackertarget, rapiddns, securitytrails, shodan, sslmate, subdomainfinderio, threadcrowd, virustotal, webarchive, whoxml**

You no need to get API key for all of them, but some of them need API key. You can get API keys from their websites and set them in the .env file. Need to API keys for the following services: shodan, whoxml, sslmate, binaryedge, hunterhow, securitytrails, bevigil


    usage: main.py [-h] keyword
    
    Awasome Subdomain Finder
    
    positional arguments:
      keyword     Keyword to search subdomains
    
    options:
      -h, --help  show this help message and exit

## Example

example usage: **python3 main.py example.tld**
```
Bevigil Subdomain Scanner Done! Total Subdomains Found: 7
Crt.sh Subdomain Scanner Done! Total Subdomains Found: 29
DnsRepo Subdomain Scanner Done! Total Subdomains Found: 38
HackerTarget Subdomain Scanner Done! Total Subdomains Found: 45
RapidDNS Subdomain Scanner Done! Total Subdomains Found: 191
SecurityTrails Subdomain Scanner Done! Total Subdomains Found: 295
Shodan.io Subdomain Scanner Done! Total Subdomains Found: 109
SSLMate Subdomain Scanner Done! Total Subdomains Found: 45
Subdomainfinder.io Subdomain Scanner Done! Total Subdomains Found: 14
Threadcrowd Subdomain Scanner Done! Total Subdomains Found: 50
Virustotal Subdomain Scanner Done! Total Subdomains Found: 327
Webarchive Subdomain Scanner Done! Total Subdomains Found: 81
Whoxml Subdomain Scanner Done! Total Subdomains Found: 202

['aday-asset.<hidden>.<tld>',
 'akdeniz.<hidden>.<tld>',
 'alfa.<hidden>.<tld>',
 'ankara.<hidden>.<tld>',
 'api-app.<hidden>.<tld>',
 'api-candidate.<hidden>.<tld>',
 'api-common.<hidden>.<tld>',
 'api-content.<hidden>.<tld>',
 'api-gateway-app.<hidden>.<tld>',
 'api-gateway-v2.<hidden>.<tld>',
 'api-gateway.<hidden>.<tld>',
 'api-v2.<hidden>.<tld>',
 'api-web.<hidden>.<tld>',
 'api.<hidden>.<tld>',
 'applicationsearchapi.<hidden>.<tld>',
 'applicationsearchapi2.<hidden>.<tld>',
 'ares.<hidden>.<tld>',
 'arge.<hidden>.<tld>',
 'asset.<hidden>.<tld>',
 'assistant.<hidden>.<tld>',
 'ats-api.<hidden>.<tld>',
 'ats-hrvenueapi.<hidden>.<tld>',
 'ats-pdf-api.<hidden>.<tld>',
 'ats-sentry.<hidden>.<tld>',
 'ats-socket.<hidden>.<tld>',
 'ats.<hidden>.<tld>',
 ...
 ...
 ...
 ]
Total subdomains found: 523
```
