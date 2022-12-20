
from exif import Image

folder_path = "E:\\PIAIC\\PIAIC-PROJECTS\\Read-Write-Image-Metadata-Using-Python-Exif-Library"
img_filename = 'sample.jpg'
img_path = f'{folder_path}/{img_filename}'

with open(img_path, 'rb') as img_file:
    img = Image(img_file)

print(img.has_exif)

print (sorted(img.list_all()))

# View existing value for body_serial_number attribute
print(f'Body Serial Number - Before: {img.get("brightness_value")}')

# Delete body_serial_number attribute
img.delete('brightness_value')

# Check updated metadata
print(f'Body Serial Number - After: {img.get("brightness_value")}')