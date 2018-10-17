import csv
import os

open_kwargs = {'encoding': 'utf8'}


class DataProvider:

    @classmethod
    def load_data(cls, file_path, test_name):
        with open(cls._get_file_path(cls._extract_file_name(file_path)), **open_kwargs) as f:
            for data in csv.reader(f):
                if data.pop(0) == test_name:
                    yield data
                else:
                    pass

    @staticmethod
    def _extract_file_name(file_path):
        return os.path.splitext(os.path.basename(file_path))[0]

    @staticmethod
    def _get_file_path(file_name):
        return fr"{os.getcwd()}/tests/resources/testdata/{file_name}.csv"
