import csv
import os

open_kwargs = {'encoding': 'utf8'}


class DataProvider:

    @staticmethod
    def __getFilePath__(file_name):
        return fr"{os.getcwd()}/tests/resources/testdata/{file_name}.csv"

    @staticmethod
    def loadData1(file_name):
        with open(DataProvider.__getFilePath__(file_name), **open_kwargs) as f:
            for data in csv.reader(f):
                yield DataProvider.checkPass(data)

    @staticmethod
    def checkPass(data):
        data_modified = list.copy(data)
        if str(data_modified[0]).lower() == 'true':
            data_modified[0] = True
        else:
            data_modified[0] = False
        return data_modified
