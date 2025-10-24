import shutil
import os
import pathlib
import BarcodeDetection

IMAGE_IN = r"C:\Users\rober\PycharmProjects\BarcodeDetection\data_in\aaad1512196.jpg"
FOLDER_OUT = r"C:\Users\rober\PycharmProjects\BarcodeDetection\data_out"

def file_rename(file_name, output_folder):
    print(file_name)
    barcode_value_list = BarcodeDetection.read_barcode(file_name, 0)
    if len(barcode_value_list) > 0:
        extension = pathlib.Path(file_name).suffix
        new_file_name = os.path.join(output_folder, barcode_value_list[0] + extension)

        shutil.move(file_name, new_file_name)



file_rename(IMAGE_IN, FOLDER_OUT)