import cv2
import imutils
from pyzbar.pyzbar import decode
import os

IMAGE_IN = r"C:\Users\rober\PycharmProjects\BarcodeDetection\data_in\NON_LEGGIBILE_doc09836820250923153800_009.jpg"
#IMAGE_IN = r"C:\Users\rober\PycharmProjects\BarcodeDetection\multi_barcode.jpg"
IMAGE_OUT = r"C:\Users\rober\PycharmProjects\BarcodeDetection\data_out"
FOLDER_IN = r"C:\Users\rober\PycharmProjects\BarcodeDetection\data_in"
ROTATE_DEG = 0

def read_barcode(current_image, angle):

    barcode_list = []

    # Rotation
    img = imutils.rotate(current_image, angle=angle)

    # Extract the barcodes
    barcodes = decode(img)

    # Loop over detected barcodes
    for barcode in barcodes:
        # Extract barcode data and type
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type

        print("Barcode data:", barcode_data, " type:", barcode_type)

        barcode_list.append(barcode_data)



    return barcode_list

#image = cv2.imread(r"C:\Users\rober\PycharmProjects\BarcodeDetection\doc09917620250930090745_002.jpg")
document_image = cv2.imread(IMAGE_IN)
# image = cv2.imread(r"C:\Users\rober\PycharmProjects\BarcodeDetection\immagine.jpg")



'''for i in range(-10,10):
  print("Rotation ",i,":")
  image_rotated = imutils.rotate(image, angle=i)
  detect_and_decode_barcode(image_rotated)
  '''

image_rotated = imutils.rotate(document_image, angle=ROTATE_DEG)
#image_rotated = imutils.rotate(image_rotated, angle=1)
barcode_data = read_barcode(document_image, 0)
#cv2.imwrite(IMAGE_OUT + r"\\" + barcode_data[0] + ".jpg",image_rotated)


directory = os.fsencode(FOLDER_IN)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    full_filename = os.path.join(FOLDER_IN, filename)
    print(full_filename)
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        document_image = cv2.imread(full_filename)

        barcode_data = read_barcode(document_image, 0)

    else:
        print('Not a valid image')


