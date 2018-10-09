import csv
import os

open_kwargs = {'encoding': 'utf8'}


class DataProvider:

    @staticmethod
    def __extractFileName__(file_path):
        return os.path.splitext(os.path.basename(file_path))[0]

    @staticmethod
    def __getFilePath__(file_name):
        return fr"{os.getcwd()}/tests/resources/testdata/{file_name}.csv"

    @staticmethod
    def __checkPass__(data):
        data_modified = list.copy(data)
        if str(data_modified[0]).lower() == 'true':
            data_modified[0] = True
        else:
            data_modified[0] = False
        return data_modified

    @staticmethod
    def loadData(file_path, test_name):
        with open(DataProvider.__getFilePath__(DataProvider.__extractFileName__(file_path)), **open_kwargs) as f:
            for data in csv.reader(f):
                if data.pop(0) == test_name:
                    yield DataProvider.__checkPass__(data)
                else:
                    pass
