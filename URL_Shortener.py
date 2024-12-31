import requests

def URL_Shortener(full_link, link_name):

    API_Key = '812f50cff10c4cee95f70b4561f34d0bdda61'
    base_url = 'https://cutt.ly/api/api.php'

    payload = {'key': API_Key, 'short': full_link, 'name': link_name}

    response = requests.get(base_url, params=payload)

    data = response.json()
    print('')

    try:
        if data['url']['status'] == 7:
            title = data['url'].get('title', 'No title provided')
            short_link = data['url']['shortLink']

            print("Title : ", title)
            print("Link : ", short_link)
        else:
            print("Error status : ", data['url']['status'])
            print("Error description : ", data['url'].get('errorMessage', 'unknown error'))

    except ValueError:
        print("Error : Response is not in JSON format.")
        print("Error : unexpected response format/")

link = input("Enter your link: ")
Name = input("Enter your Title name for your link: ")
URL_Shortener(link, Name)