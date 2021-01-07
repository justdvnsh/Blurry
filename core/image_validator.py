import imghdr


## Validate The image , if the submitted file is actually an image or not.
def validate_image(stream):
    header = stream.read(512) ## 512 bytes are sufficient to read the headers
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != "jpeg" else 'jpg')
