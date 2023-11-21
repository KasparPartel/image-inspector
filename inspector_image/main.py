import argparse

from eof_stegano import extract_data_after_jpeg
from exif import get_gps

CLI_FLAGS = ["-map", "-steg"]
PARSER_DESCRIPTION = (
    "Welcome to inspector-image v1.0.0\nOPTIONS: \n-map         Find location of the image\n-steg         "
    "Find hidden data inside the image\n")


def init_parser(flags, description):
    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawDescriptionHelpFormatter)

    for f in flags:
        parser.add_argument(f)

    return parser


def get_flag(args):
    if args.map is not None:
        return ["-map", args.map]
    elif args.steg is not None:
        return ["-steg", args.steg]
    else:
        return [None, None]


def main():
    parser = init_parser(CLI_FLAGS, PARSER_DESCRIPTION)
    args = parser.parse_args()
    full_flag = get_flag(args)
    flag = full_flag[0]
    flag_value = full_flag[1]

    if flag == "-steg":
        data = extract_data_after_jpeg(flag_value)
        if data is not None:
            print(data)
        else:
            print("No EOF found in the file.")

    if flag == "-map":
        gps = get_gps(flag_value)
        if gps is not None:
            print(f"Latitude: {gps[0]}")
            print(f"Longitude: {gps[1]}")
        else:
            print("GPS data is not present in image")


if __name__ == '__main__':
    main()
