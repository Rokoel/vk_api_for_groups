from src.vk_api_for_groups import Api

token = '_______________________________________________________________________________________'  # your token here
# you can get the token by going to this link and copying the part in the resulting link (link you were redirected to)
# https://oauth.vk.com/authorize?client_id=APP_ID&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=wall,offline&response_type=token&v=API_VERSION
# where APP_ID is your app id and API_VERSION is api version, that you use

group_id = -000000000  # your group's (or user's if you'd like, but it is not tested for users) id
# you can know your id from your shortname by using this link: https://vk.com/dev/utils.resolveScreenName and using a
# window in the bottom

api = Api(token, group_id, ver=5.131)  # you may leave the version blank in order to use the latest one

message = "Hello, World!"
path_to_a_post = "An/absolute/path/to/file.txt"  # tested with .txt file

api.send_post(post=message, post_path="")  # leave post_path blank or just don't write it, if you want
