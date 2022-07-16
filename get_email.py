import email
import get_data
import json

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    
    email = []
    for i in data["results"]:
        for e,l in dict(i).items():
            if e == "email":
                    email.append(l)
    return email

print(get_email(json.loads(open("randomuser_data.json", 'r').read())))