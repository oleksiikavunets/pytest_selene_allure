import re


class BaseControl:

    xpath = None
    css = None

    @staticmethod
    def splitcamel(name):
        return re.sub('(?!^)([A-Z][a-z]+)', r' \1', name).split()[-1]
  #  @property
  #  def click(self):
  #      pass

