import requests

def get_repos(username):
    url = f"https://www.example.com    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Returns a list of repositories
    else:
        return f"Error: {response.status_code}"

# Example usage:
repos = get_repos('username')  # Replace 'username' with the actual example username
print(repos)
