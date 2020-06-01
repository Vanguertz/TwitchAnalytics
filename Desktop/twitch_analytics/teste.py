import twitch_integration

user_login = 'gaules'

query = twitch_integration.get_user_query(user_login)
response = twitch_integration.get_response(query)
twitch_integration.print_response(response)







