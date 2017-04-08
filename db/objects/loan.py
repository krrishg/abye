
from sqlobject import *


class Loan(SQLObject):

    class sqlmeta:
        lazyUpdate = True

    '''
    Loan Object
    '''
    ## properties
    name = StringCol(length=255, default=None)
    bank = ForeignKey("Bank")
    interest_rate = DecimalCol()
    max_amount = IntCol()
