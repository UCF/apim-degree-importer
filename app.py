# Imports
import urllib2, json, sys
from programs.program import Program
from programs.subplan import Subplan

def main():
    """
    The main execution block

    This script accepts a single required argument:

    <apim_url> string The URL of the APIM system
    """
    APIM_URL = ''

    if len(sys.argv) < 2:
        sys.exit('The APIM Error is required')
    else:
        APIM_URL = sys.argv[1]

    response = urllib2.urlopen(APIM_URL)

    data = json.loads(response.read())

    degrees = []

    for d in data:
        degree = Program(d)
        degrees.append(degree)

    for degree in (x for x in degrees if x.has_online == True):
        print degree.online_subplan.code

    return 0

if __name__ == '__main__':
    main()
