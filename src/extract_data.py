import numpy as np
import os
import csv
import matplotlib.pyplot as plt
import torch
<<<<<<< HEAD
=======
import torch.utils.data as data
>>>>>>> fccba075dc509dcbf311fb90c05a749ca392ae15

class GetDataFromCSV:
    PUBLIC_TRAIN_START_POINT = 0
    TRAIN_END_POINT = 28708 #28708 samples for training
    PUBLIC_TEST_START_POINT = 28709
    PUBLIC_TEST_END_POINT = 35887 #3589*2 samples for training
    PRIVATE_TEST_END_POINT = 35887

    DIR_PATH = os.path.dirname(os.path.realpath(__file__))
    DATA_CSV_FILE = DIR_PATH + '/../data/fer2013/fer2013.csv'

    IMAGE_SIZE = 48 * 48

    def get_training_data(cls):
        train_data_y = np.zeros([cls.TRAIN_END_POINT, 1], dtype="uint8")
        train_data_x = np.zeros([cls.TRAIN_END_POINT, 48, 48], dtype="uint8")
        with open(cls.DATA_CSV_FILE, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            _, = next(reader)
            for k, data in enumerate(reader):
                if k < cls.TRAIN_END_POINT:
                    pixels_formated = [int(a) for a in data[1].split(" ")]
                    target = int(data[0])
                    pixels_in_picture_format = np.reshape(pixels_formated, [48, 48])
                    train_data_y[k, :] = target
                    train_data_x[k, :, :] = pixels_in_picture_format
<<<<<<< HEAD

=======
                # break
>>>>>>> fccba075dc509dcbf311fb90c05a749ca392ae15
        return train_data_x, train_data_y

    def get_test_data(cls):
        test_data_y = np.zeros([cls.PRIVATE_TEST_END_POINT - cls.PUBLIC_TEST_START_POINT, 1], dtype="uint8")
        test_data_x = np.zeros([cls.PRIVATE_TEST_END_POINT - cls.PUBLIC_TEST_START_POINT, 48, 48], dtype="uint8")
        with open(cls.DATA_CSV_FILE, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            _ = next(reader)
            for k, data in enumerate(reader):
                if k > cls.TRAIN_END_POINT:
                    k_mod = k - cls.PUBLIC_TEST_START_POINT
                    pixels_formated = [int(a) for a in data[1].split(" ")]
                    target = int(data[0])
                    pixels_in_picture_format = np.reshape(pixels_formated, [48, 48])
                    test_data_y[k_mod, :] = target
                    test_data_x[k_mod, :, :] = pixels_in_picture_format
        return test_data_x, test_data_y

    def get_all_data(cls):
        data_y = np.zeros([cls.PRIVATE_TEST_END_POINT, 1], dtype="uint8")
        data_x = np.zeros([cls.PRIVATE_TEST_END_POINT, 48, 48], dtype="uint8")
        with open(cls.DATA_CSV_FILE, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            _ = next(reader)
            for k, data in enumerate(reader):
                k_mod = k - cls.PUBLIC_TEST_START_POINT
                pixels_formated = [int(a) for a in data[1].split(" ")]
                target = int(data[0])
                pixels_in_picture_format = np.reshape(pixels_formated, [48, 48])
                data_y[k_mod, :] = target
                data_x[k_mod, :, :] = pixels_in_picture_format

        return data_x, data_y

    def get_first_record(cls):
        data_y = np.zeros([1, 1], dtype="uint8")
        data_x = np.zeros([1, 48, 48], dtype="uint8")
        with open(cls.DATA_CSV_FILE, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            _ = next(reader)
            for k, data in enumerate(reader):
                pixels_formated = [int(a) for a in data[1].split(" ")]
                target = int(data[0])
                pixels_in_picture_format = np.reshape(pixels_formated, [48, 48])
                data_y[0, :] = target
                data_x[0, :, :] = pixels_in_picture_format

        return data_x, data_y

class MyDataset(data.Dataset):
    def __init__(self, images, labels):
        self.images = images
        self.labels = labels

    def __getitem__(self, index):
        img, target = self.images[index], self.labels[index]
        return img, target

    def __len__(self):
        return len(self.images)

if __name__ == "__main__":
    datacsv = GetDataFromCSV()
<<<<<<< HEAD
    image, labels = datacsv.get_training_data()
    #print(len(image))
    print(labels)
=======
    image, labels = datacsv.get_test_data()
    image = torch.from_numpy(image).view(-1, 1, 48, 48)
    test_dataset = MyDataset(image, labels)
    print(len(image))
    print(len(labels))
>>>>>>> fccba075dc509dcbf311fb90c05a749ca392ae15
