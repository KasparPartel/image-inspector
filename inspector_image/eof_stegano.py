def extract_data_after_jpeg(image_path):
    with open(image_path, 'rb') as f:
        content = f.read()

    # Find the end of jpeg image denoted by FF D9 in hexadecimal
    EOF = b'\xFF\xD9'
    position = content.find(EOF)

    if position != -1:  # FF D9 found in the file
        position += len(EOF)  # Skip past FF D9
        data_after_eof = content[position:]
        return data_after_eof.decode('utf-8')
    else:
        print("No EOF found in the file.")
        return None
