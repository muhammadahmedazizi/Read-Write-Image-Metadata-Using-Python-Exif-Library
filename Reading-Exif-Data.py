from exif import Image

folder_path = "E:\\PIAIC\\PIAIC-PROJECTS\\Read-Write-Image-Metadata-Using-Python-Exif-Library"
img_filename = 'biryani.jpg'
img_path = f'{folder_path}/{img_filename}'

with open(img_path, 'rb') as img_file:
    img = Image(img_file)

print(img.has_exif)

#print (sorted(img.list_all()))

# Make of device which captured image
#print(f'Make: {img.get("make")}')

# Model of device which captured image
print(f'Model: {img.get("model")}')

# Software involved in uploading and digitizing image
print(f'Software: {img.get("software")}')

# Name of photographer who took the image
print(f'Artist: {img.get("artist")}')

# Original datetime that image was taken (photographed)
print(f'DateTime (Original): {img.get("datetime_original")}')

# Details of flash function
print(f'Flash Details: {img.get("flash")}')

# Details of flash function
print(f'copyright Details: {img.get("copyright")}')
