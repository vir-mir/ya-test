# -*- coding: utf-8 -*-
import re


class FieldValidateException(Exception):
    pass


class Field(object):

    def __init__(self, value):
        self.value = value

    def clear(self):
        pass

    def validate(self):
        pass

    def get_value(self):
        self.clear()
        self.validate()
        return self.value


class FieldString(Field):

    def clear(self):
        self.value = str(self.value).strip()


class FieldStringSize(FieldString):

    def __init__(self, value, larger, less):
        self.larger = larger
        self.less = less
        super(FieldStringSize, self).__init__(value)

    def validate(self):
        super(FieldStringSize, self).validate()
        if not self.less > len(self.value) > self.larger:
            raise FieldValidateException('value not size field')


class FieldLogin(FieldString):

    def validate(self):
        super(FieldLogin, self).validate()

        if len(self.value) == 1 and re.search(r'^[a-z]$', self.value, re.IGNORECASE):
            return True

        if re.search(r'^[a-z]+([a-z0-9-.]+)?[a-z0-9]+$', self.value, re.IGNORECASE):
            return True

        raise FieldValidateException('invalid field')


class FieldLoginSize(FieldStringSize, FieldLogin):
    pass


class TestFieldLoginSize(FieldLoginSize):
    def __init__(self, value, larger=0, less=21):
        super(TestFieldLoginSize, self).__init__(value, larger, less)

    def get_value(self):
        try:
            super(TestFieldLoginSize, self).get_value()
            return True
        except FieldValidateException:
            return False


if __name__ == '__main__':
    # False
    print(TestFieldLoginSize('.').get_value())
    print(TestFieldLoginSize('-').get_value())
    print(TestFieldLoginSize(1).get_value())
    print(TestFieldLoginSize('ss123456789123467-.').get_value())
    print(TestFieldLoginSize('ss12345678912-3.467sd').get_value())

    # True
    print(TestFieldLoginSize('s').get_value())
    print(TestFieldLoginSize('s1').get_value())
    print(TestFieldLoginSize('ss12345678912-3.467').get_value())
    print(TestFieldLoginSize('ss12345678912-3.467s').get_value())
