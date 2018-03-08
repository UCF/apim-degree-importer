# Imports
import urllib2, json
from programs.program import Program

def main():
    API_URL = 'https://apim.ikm.ucf.edu/V1/main/college/all/status/active/career/all/location/all'

    response = urllib2.urlopen(API_URL)

    data = json.loads(response.read())

    degrees = []

    for d in data:
        degree = Program(d)
        degrees.append(degree)

    for degree in degrees:
        print degree.department

    return 0

if __name__ == '__main__':
    main()
