def extract_data_after_eof(path_to_image):
    with open(path_to_image, 'rb') as f:
        content = f.read()

    # Find the end of jpeg image denoted by FF D9 in hexadecimal
    EOF = b'\xFF\xD9'
    position = content.find(EOF)

    if position != -1:
        position += len(EOF)
        data_after_eof = content[position:]
        return data_after_eof.decode('utf-8')
    else:
        return None
