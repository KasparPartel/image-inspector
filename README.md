## Introduction
Inspector-image is a steganography decoding program. It finds the hidden data using End-of-File (EoF) method to extract all the data from the image and finds the latitude and longitude from exif tags. 

## Dependencies
> ⚠️ **Warning:** You must have poetry to install dependencies!
[Poetry installation guide](https://python-poetry.org/docs/#installing-with-pipx)

To install dependencies run
```poetry install```

## Usage
```-steg``` analyzes the image and extracts the hidden data if present \
```-map``` returns the latitude and longitude from exif GPS tag if present

```poetry run python3 inspector_image/cli.py [FLAG] [IMAGE_PATH]``` \
OR \
```poetry run python inspector_image/cli.py [FLAG] [IMAGE_PATH]```

<b>Examples</b>
```
$ poetry run python3 inspector_image/cli.py -steg ./assets/secret-image.jpeg 

-----BEGIN PGP PUBLIC KEY BLOCK-----  
Version: 01

mQENBGIwpy4BCACFayWXCgHH2QqXkicbqD1ZlMUALpyGxDFiWh1SErFUPJOO/CgU
2688bAd26kxDSGShiL9YUOQJ6MS+zJ0KlBkeKPoQlPHRBVpH7vjcRbZNgDxd82uE
7mhM6AH+W3fAim/PhU3lm661UGMCHM3YLupa/N0Dhhmfimtg+0AimCoXk6Q6WJxg
ao8XY1Wqacd2L0ssASY5EkMahNgtX0Ri8snbTlImd5Jq/sC4buZq96IlxyhtX0ew
zD/md0U++8SxG9+gi+uuImqV8Wq1YHvJH5BtIbfcNG9V00+03ikEX9tppKxCkhzx
9rSqvyH6Uirs3FVhFtoXUSg8IeYgSH6p5tsVABEBAAG0CDAxQDAxLjAxiQEcBBAB
AgAGBQJiMKcuAAoJEAJuInmYDhhbO3gIAITZhEtLBj524y1oeBKI5fZDwgCQum6B
D9ZaUq1+dI98HsiRAiUqw1YbuJQgeUVGCmqXeC3E7VTPCPZsaCLfWWZVeosRIqB8
PwGxcY6vXHYR4S6T8rHwsNASw+Vo2pmQIGn4tABmtyappqJbwSz+5yg73DjYXiX/
e/f6i9nrFFsfMjjKd71cAyHjV8u0z7fGDXpR22vo7CdloXMxsZRyHjd/4ofUgvu0
6hWYG2zBWTXpwaYRU9u1NCr1gfKnukm8gbILSSgjr8pQ3OLWHleJXc0sCEJFKSbg
+I0KJP7Ccrxy0MaKYk0T0tYbBrvqQCzXqzAqcjn+1GoDDS1J8WBJopM=
=N8hc
-----END PGP PUBLIC KEY BLOCK-----
```
```
$ poetry run python3 inspector_image/cli.py -map ./assets/secret-image.jpeg

Latitude: 32.0866296534937
Longitude: 34.885130555555556
```

## What is steganography?
Steganography is the practice of hiding data in plain sight. You can hide data inside images, video, audio, digital content, files. There are different methods for hiding the data, but the one used in this exercise was End-Of-File (EOF) steganography. It means that the data was hidden after the main binary code had ended. 

The data for concealment is compressed and inserted after the EOF tag in the image file. All text or binary data behind the EOF tag in the image file is ignored when the image is viewed directly from an image viewer. That's where we can hide our data. 👾

