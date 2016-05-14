# /usr/bin/env python 2.7

import shodan

def scan():
    try:
        ShodanKeyString = "API_KEY"
        ShodanApi = shodan.Shodan(ShodanKeyString)
        scan_results = ShodanApi.search("apache")
        for result in scan_results['matches']:
            print "IP: %s" % result['ip_str']
            print result['data']
            print ''
    except shodan.APIError, e:
            print "There is an error: %s" % e
if __name__ == "__main__":
    scan()

