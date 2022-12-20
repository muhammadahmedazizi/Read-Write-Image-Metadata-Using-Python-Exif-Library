from exif import Image

folder_path = "E:\\PIAIC\\PIAIC-PROJECTS\\Read-Write-Image-Metadata-Using-Python-Exif-Library"
img_filename = 'sofitel-Front-View.jpg'
img_path = f'{folder_path}/{img_filename}'

with open(img_path, 'rb') as img_file:
    img = Image(img_file)

print(img.has_exif)

img.copyright = 'Ceremonialdelights 2022'
img.artist = 'Muhammad Ahmed'

# Check updated metadata
print(f'Copyright: {img.get("copyright")}')

# Check updated metadata
print(f'Artist: {img.get("Artist")}')

# Write image with modified EXIF metadata to an image file
with open(f'{folder_path}/modified_{img_filename}', 'wb') as new_image_file:
        new_image_file.write(img.get_file())