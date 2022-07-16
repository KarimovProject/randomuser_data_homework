import get_data

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    user = 0
    for i in data["results"]:
        user+=1
    return user
print(get_count_users(get_data.get_data("randomuser_data.json")))

    