from PyFlow.Core import PinBase
from PyFlow.Core.Common import *


class BoolPin(PinBase):
    """doc string for BoolPin"""
    def __init__(self, name, parent, direction, **kwargs):
        super(BoolPin, self).__init__(name, parent, direction, **kwargs)
        self.setDefaultValue(False)

    @staticmethod
    def IsValuePin():
        return True

    @staticmethod
    def supportedDataTypes():
        return ('BoolPin', 'IntPin',)

    @staticmethod
    def pinDataTypeHint():
        return 'BoolPin', False

    @staticmethod
    def color():
        return (255, 0, 0, 255)

    @staticmethod
    def processData(data):
        return bool(data)

    def setData(self, data):
        try:
            self._data = self.processData(data)
        except:
            self._data = self.defaultValue()
        PinBase.setData(self, self._data)
