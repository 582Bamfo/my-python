import json
import requests
import sys

class Contents:
    def __init__(self):
        self.ID = None
        self.Contents = None
        self.IsValid=True # added this line

def get_all_contents(urls):
    contents_list = []

    for url in urls:
        response = requests.get(url)

        content = Contents()
        data = response.json()

        content.ID = data['id']
        content.Contents = data['contents']
        try:
            validate(content)
        except:
            sys.exit(0)

        contents_list.append(content)

    return contents_list

def validate(content):

    lower_cased_contents = content.Contents.lower()#help
    if "invalid" in lower_cased_contents:#help
        content.IsValid = False#help
    return

def main():
    urls = [
        "https://mocki.io/v1/65c47e72-076d-4857-80fc-6b3b3d1957f6",
        "https://mocki.io/v1/fbdea14c-43b2-479f-a4b6-a0c427bdf6d8",
        "https://mocki.io/v1/4add6e30-8298-41ce-992a-b7373c0ee909",
        "https://mocki.io/v1/ab887433-4f96-4cd3-a0ff-e6faec6ba8ed",
    ]

    contents_list = get_all_contents(urls)

    for content in contents_list:
        print(content.__dict__)

if __name__ == "__main__":
    main()
