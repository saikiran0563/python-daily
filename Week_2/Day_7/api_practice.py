import requests

query = input("Enter repository search: ")

params = {
    "q": query,
    "per_page" : 5

}
try:
    response = requests.get("https://api.github.com/search/repositories",
        params=params,
        timeout = 5

    )
    response.raise_for_status()

    data = response.json()

    for repo in data["items"]:
        print(repo["full_name"])
        print(repo["stargazers_count"])
        print(repo["html_url"])
        print()

except requests.RequestException as e:
    print("Request failed:", e)


    