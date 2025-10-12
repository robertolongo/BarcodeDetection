import cv2
import imutils
from pyzbar.pyzbar import decode

IMAGE_IN = r"C:\Users\rober\PycharmProjects\BarcodeDetection\NON_LEGGIBILE_doc09917620250930090745_002.jpg"
#IMAGE_IN = r"C:\Users\rober\PycharmProjects\BarcodeDetection\multi_barcode.jpg"
IMAGE_OUT = r"C:\Users\rober\PycharmProjects\BarcodeDetection"
ROTATE_DEG = 1

def read_barcode(current_image):
    # Convert to grayscale
    #gray = cv2.cvtColor(current_image, cv2.COLOR_BGR2GRAY)

    # Extract the barcodes
    barcodes = decode(current_image)

    # Loop over detected barcodes
    for barcode in barcodes:
        # Extract barcode data and type
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type

        print("Barcode data:", barcode_data, " type:", barcode_type)

        return barcode_data
    return "no_barcode_found"

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
barcode_data = read_barcode(image_rotated)
cv2.imwrite(IMAGE_OUT + r"\\" + barcode_data + ".jpg",image_rotated)

