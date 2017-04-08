from sqlobject import *

class Deposit(SQLObject):

    class sqlmeta:
        lazyUpdate = True

    '''
    Deposit Object
    '''
    ## properties
    name = StringCol(length=255, default=None)
    bank = ForeignKey("Bank")
    interest_rate = DecimalCol()
    min_amount = IntCol()
