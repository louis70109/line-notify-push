# LINE Notify Docker Container

# Message

```shell
docker run --rm -e TOKEN=YOUR_TOKEN -e MESSAGE="HELLO" louis70109/lotify-push-container
```

# Image

```shell
docker run --rm -e TOKEN=YOUR_TOKEN -e MESSAGE="HELLO" -e IMAGE_URL="https://example.com/1.png" louis70109/lotify-push-container
```

# Sticker

```shell
docker run --rm -e TOKEN=YOUR_TOKEN -e MESSAGE="HELLO" -e STICKER_ID=1 -e PACKAGE_ID=1 louis70109/lotify-push-container
```