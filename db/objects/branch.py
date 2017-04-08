from sqlobject import *

class Branch(SQLObject):
    class sqlmeta:
        lazyUpdate = True

    bank = ForeignKey("Bank")
