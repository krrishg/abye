from sqlobject import *

from branch import Branch
from loan import Loan
from deposit import Deposit

class Bank(SQLObject):

    class sqlmeta:
        lazyUpdate = True

    '''
    Bank Object
    '''
    ## properties
    name = StringCol(length=255, default=None)
    branches = MultipleJoin("Branch")
    loans = MultipleJoin("Loan")
    deposits = MultipleJoin("Deposit")
