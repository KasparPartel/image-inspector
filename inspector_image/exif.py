from PIL import Image, ExifTags


def get_gps(path_to_image):
    with Image.open(path_to_image) as path_to_image:
        img_gps = path_to_image.getexif().get_ifd(0x8825)

    gps_list = []

    if img_gps is None:
        print("Sorry, image has no exif data.")
        return None
    else:
        for gps in [img_gps[2], img_gps[4]]:
            degrees = gps[0]
            minutes = gps[1]
            seconds = gps[2]

            decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)

            gps_list.append(decimal)

        return gps_list


