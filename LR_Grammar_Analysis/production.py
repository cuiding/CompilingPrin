# coding:utf-8
origin_production_list = [
    'P -> D S ',
    'D -> L id ; D | NULL ',
    'L -> int | float ',
    'S -> id = E ',
    'S -> if ( C ) S else S ',
    'S -> S ; S ',
    'C -> E > E ',
    'C -> E < E ',
    'C -> E == E ',
    'E -> E + T ',
    'E -> E - T ',
    'E -> T ',
    'T -> F ',
    'T -> T * F ',
    'T -> T / F ',
    'F -> ( E ) ',
    'F -> id ',
    ]

# 说明：列表中的状态并不是全部状态
production = ["P", "E", "D", "L", "S", "C", "T", "F"]
s = []
t = ['id', 'if', "+", "-", "/", "int10", "==", "(", ")", "float", "int", ";", "NULL", "="]


class Production_init(object):
    """构建所有状态"""
    def __init__(self):
        pass

    def _state_init(self, parma):
        for i in t:
            if parma == i:
                return 1
        for s in origin_production_list:
            if parma == s[:s.index(" ")]:
                print s, s[:s.index(" ")]

    def init(self):
        start = "P' -> .P"
        production.append(start)
        self._state_init("P")
        for i in origin_production_list:
            parma = i[:i.index(" ")]
            self._state_init(parma)


if __name__ == '__main__':
    Production_init().init()

