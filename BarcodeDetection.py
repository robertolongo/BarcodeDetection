import cv2
import imutils
from pyzbar.pyzbar import decode
import os


IMAGE_IN = r"C:\Users\rober\PycharmProjects\BarcodeDetection\data_in\NON_LEGGIBILE_doc09836820250923153800_009.jpg"
#IMAGE_IN = r"C:\Users\rober\PycharmProjects\BarcodeDetection\multi_barcode.jpg"
FOLDER_OUT = r"C:\Users\rober\PycharmProjects\BarcodeDetection\data_out"
FOLDER_IN = r"C:\Users\rober\PycharmProjects\BarcodeDetection\data_in"
ROTATE_DEG = 0

def read_barcode(full_filename, angle):

    barcode_list = []
    current_image = cv2.imread(full_filename)
    # Preprocess the image for a better detection
    img = cv2.cvtColor(current_image, cv2.COLOR_BGR2GRAY) # convert to grayscale
    img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)[1]  # apply threshold

    # Rotation
    if angle:
        img = imutils.rotate(img, angle=angle)

    # Extract the barcodes
    barcodes = decode(img)

    # Loop over detected barcodes
    for barcode in barcodes:
        # Extract barcode data and type
        barcode_value = barcode.data.decode("utf-8")
        barcode_type = barcode.type

        print("Barcode value:", barcode_value, " type:", barcode_type)

        barcode_list.append(barcode_value)



    return barcode_list

def main():
    '''
    document_image = cv2.imread(IMAGE_IN)
    image_rotated = imutils.rotate(document_image, angle=ROTATE_DEG)
    # image_rotated = imutils.rotate(image_rotated, angle=1)
    barcode_data = read_barcode(document_image, 0)
    cv2.imwrite(FOLDER_OUT + r"\\" + barcode_data[0] + ".jpg", image_rotated)
    '''

    directory = os.fsencode(FOLDER_IN)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        full_filename = os.path.join(FOLDER_IN, filename)
        print(full_filename)
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            #document_image = cv2.imread(full_filename)

            barcode_value_list = read_barcode(full_filename, 0)

            print(barcode_value_list)

        else:
            print('Not a valid image')




if __name__ == "__main__":
    main()





