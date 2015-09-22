import urllib.request
import urllib.parse
import json
import sys


# for item in data['objects']:
#    print(item['name'])

def main():
    request = select_locality()
    process_json(request)


def select_locality():
    api_key = '&api_key=YOUR_API_KEY'
    request = 'https://api.locu.com/v1_0/venue/search/'
    locale = '&locality='
    locale += input('Which city do you want to get information from? ')
    country = '?country='
    country += input('Which country is this city found in? ')
    country = country.replace(' ', '%20')
    print(country)
    request = request + country + locale + api_key
    print(request)
    return request


def process_json(request):
    response = urllib.request.urlopen(request)
    str_response = response.read().decode('utf-8')
    data = json.loads(str_response)
    f = open('output.txt', 'w')
    sys.stdout = f
    for item in data['objects']:
        print('Name: ' + item['name'])

if __name__ == '__main__':
    main()
