from abc import ABCMeta, abstractmethod
import abc

class AbstractOperation(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, operand_a, operand_b):
        self.operand_a = operand_a
        self.operand_b = operand_b
        super(AbstractOperation, self).__init__ #This is an explicit declaration. If not written, it is still executed implicitly.

'''
note that __meta__class is for python 2
class name(metaclass=ABCMeta) is for python 3
class name(ABC) is for python 3.7
'''



