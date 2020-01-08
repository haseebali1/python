import requests

from plotly.graph_objs import Bar
from plotly import offline

# make an api call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept' : 'application/vnd.github.v3+json'}
r = requests .get(url, headers=headers)

# store api response in a variable
response_dict = r.json()

# explore information about the repositories
repo_dicts = response_dict['items']

# get the names and the stars for the first twenty repos
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts[:20]:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_links.append(f"<a href='{repo_url}'>{repo_name}</a>")
    stars.append(repo_dict['stargazers_count'])
    label = f"{repo_dict['owner']['login']}<br />{repo_dict['description']}"
    labels.append(label)

# Make the bar graph
data = [{
    'type' : 'bar',
    'x' : repo_links,
    'y' : stars,
    'hovertext' : labels,
    'marker' : {
        'color' : 'rgb(60, 100, 150)',
        'line' : {'width' : 1.5, 'color' : 'rgb(25, 25, 25)'}
        },
    'opacity' : 0.6
    }]

my_layout = {
        'title' : 'Top 20 Most-Starred Python Repositories on Github',
        'xaxis' : {
            'title' : 'Repository',
            'titlefont' : {'size' : 24},
            'tickfont' : {'size' : 14}
            },
        'yaxis' : {
            'title' : 'Repository',
            'titlefont' : {'size' : 24},
            'tickfont' : {'size' : 14}
            }
        }

fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig, filename='python_repos.html')
