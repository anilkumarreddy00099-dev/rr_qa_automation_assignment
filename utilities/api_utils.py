import requests

def fetch_movies(category):
    # use a demo API key or the correct one if available
    url = f"https://api.themoviedb.org/3/{category}?api_key=demo_key"
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json().get("results", [])
        return [m.get("title", "") for m in data]
    return []
