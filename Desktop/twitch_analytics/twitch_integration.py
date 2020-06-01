import requests, json

BASE_URL = 'https://api.twitch.tv/helix/'
HEADERS = {'Client-ID': 'u1xqb7g16b8qusuu4q7aopat5rgrvw', "Authorization": "Bearer bhtbsan3kmze921e1te2n9dr9yuyfa"}
INDENT = 2


# get response from twitch API call
def get_response(query):
    url = BASE_URL + query
    response = requests.get(url, headers=HEADERS)
    return response


# used for debugging the result
def print_response(response):
    response_json = response.json()
    print_response = json.dumps(response_json, indent=INDENT)
    print(print_response)


# get the current live stream info, given a username
def get_user_streams_query(user_login):
    return 'streams?user_login={0}'.format(user_login)


def get_user_query(user_login):
    return 'users?login={0}'.format(user_login)


def get_user_videos_query(user_id):
    return 'videos?user_id={0}&first=50'.format(user_id)


def get_games_query():
    return 'games/top'
