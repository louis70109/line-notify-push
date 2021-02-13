import os

from lotify.client import Client

if __name__ == '__main__':
    lotify = Client()
    message = os.getenv("MESSAGE")
    token = os.getenv("TOKEN")
    image = os.getenv('IMAGE_URL')
    sticker = os.getenv('STICKER_ID')
    package = os.getenv('PACKAGE_ID')
    if image:
        lotify.send_message_with_image_url(
            message=message,
            access_token=token,
            image_fullsize=image,
            image_thumbnail=image)
    elif sticker and package:
        lotify.send_message_with_sticker(
            message=message,
            access_token=token,
            sticker_id=sticker,
            sticker_package_id=package
        )
    else:
        lotify.send_message(message=message, access_token=token)
    print('end')
