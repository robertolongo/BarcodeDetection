import shutil
import os
import pathlib
import BarcodeDetection

# Config - BEGIN
IMAGE_IN = r"C:\Users\rober\PycharmProjects\BarcodeDetection\data_in\aaad1512196.jpg"
FOLDER_IN = r"C:\Users\rober\PycharmProjects\BarcodeDetection\data_in"
FOLDER_OUT = r"C:\Users\rober\PycharmProjects\BarcodeDetection\data_out"
#Config - END

def file_rename(file_name, output_folder):
    #print(file_name)
    barcode_value_list = BarcodeDetection.read_barcode(file_name, 0)
    if len(barcode_value_list) > 0:
        extension = pathlib.Path(file_name).suffix
        new_file_name = os.path.join(output_folder, barcode_value_list[0] + extension)
        try:
            shutil.move(file_name, new_file_name)
            print("renamed")
        except OSError:
            print("Could not move file")


def batch_rename(input_folder, output_folder):
    print("input_folder:", input_folder)
    print("output_folder:", output_folder)

    directory = os.fsencode(input_folder)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        full_filename = os.path.join(input_folder, filename)
        print()
        print(full_filename)
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            file_rename(full_filename, output_folder)
        else:
            print('Not a valid image')



def main():
    #file_rename(IMAGE_IN, FOLDER_OUT)
    batch_rename(FOLDER_IN, FOLDER_OUT)


if __name__ == "__main__":
    main()
