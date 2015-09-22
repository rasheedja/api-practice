import urllib.request
import json


# for item in data['objects']:
#    print(item['name'])

def main():
    request = select_locality()
    process_json(request)


def select_locality():
    api_key = '&api_key=YOUR_API_KEY'
    request = 'https://api.locu.com/v1_0/venue/search/?locality='
    print('Which locale do you want to get information from?')
    locale = input()
    request = request + locale + api_key
    return request


def process_json(request):
    response = urllib.request.urlopen(request)
    str_response = response.readall().decode('utf-8')
    data = json.loads(str_response)
    for item in data['objects']:
        print('Name: ' + item['name'])

if __name__ == '__main__':
    main()
