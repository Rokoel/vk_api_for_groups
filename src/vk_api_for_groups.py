import requests
import os.path


class NoMessageOrImageException(Exception):
    """
    This Exception is raised when the post message is empty at all (no text and no attachments).
    """
    pass


class Api:
    """
    This is a class for a VK-API. It is made for groups' automation mostly (maybe something else will be added in
    the future).
    TODO: add ability to have more than one album per API instance
    TODO: add all types of attachments
    TODO: add ability to change group's settings
    """
    def __init__(self, forever_access_token, group_id, album_id='', ver=''):
        """
        Basic constructor, nothing interesting here. "Album" feature is unavailable for now.
        :param forever_access_token: A string that contains a token that is used for authorization.
        :param group_id: An integer that represents group id (NOT shortname). Usually negative
        :param album_id: An integer that represents album id.
        :param ver: A string that represents a version of api used by VK (not this module!). If it is not specified,
        latest version is used.
        """
        self.token = forever_access_token
        self.id = group_id
        if ver == '':  # if api version is unspecified, we use the latest one
            source = requests.get("https://vk.com/dev/versions")  # we are looking for its serial number in the VKs docs
            self.v = source.text.partition('<span class="dev_version_num fl_l ">')[2][0:5]  # getting first five symbols
            # (that SHOULD work, but VK may reduce length of serial number)
            # after the span block with specific class as you can see in a string above
            print("Leaving version unspecified is not recommended due to the instability"  # warning
                  "of the way we are getting latest version number.")
        self.v = ver
        # self.album = album_id  ! doesn't work at the time

    def return_attachment_url(self, link):
        """
        A method that will return a link to a file. If a path to a file is local, it will upload a file and then return
        the link to it.
        :param link: A string that contains a link to a file or a path.
        :return: link: A string that contains actual link to a file.
        TODO: actually add image uploading
        """
        if 'vk.com' in link:
            return link
        else:
            if not os.path.isfile(link):
                raise FileNotFoundError("Image was not found on your machine.")
            else:
                print("Image is found locally, but not uploaded (this function is work-in-progress) and so no url is"
                      "returned")
                return ""

    def send_post(self, post='', post_path='', image_url=''):
        """
        A method that allows a group admin to send posts to a group from a file or from the string simply.
        :param post: A string that represents post's text
        :param post_path: A string that represents a path to another text (located somewhere on the machine)
        :param image_url: A string that represents a url to an image attachment (is not supported now)
        :return: response: A json response

        TODO: add text formatting
        TODO: add attachment support
        """
        if post + post_path + image_url == '':
            raise NoMessageOrImageException("There is nothing to post!")

        message_to_post = post
        try:
            with open(post_path, 'r') as file:
                post_from_file = file.read()  # .replace('\n', '') ?
                message_to_post += post_from_file
        except FileNotFoundError:
            print("Text file from the path doesn't exist!")

        response = requests.post(
            'https://api.vk.com/method/wall.post', data={
                'access_token': self.token,
                'owner_id': self.id,
                'from_group': 1,
                'message': message_to_post,
                'signed': 0,
                'v': self.v
            }
        ).json()
        print(response)
        print("if a post was successful, that is what was posted:")
        print(message_to_post)
        return response  # maybe we should return the message?
