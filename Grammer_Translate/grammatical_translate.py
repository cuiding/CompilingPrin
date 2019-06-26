# usr/bin/env python
# encoding:utf-8

from Lexical_Analysis.lexical_analyze import LexicalAnalyse
from LR_Grammar_Analysis.LR_Grammar_Analyze import LRGramAnalyze
from LR_Grammar_Analysis.production import t


# origin_prodution_list = [
#     'P -> D S ',
#     'D -> L id ; D | NULL ',
#     'L -> int | float ',
#     'S -> id = E ',
#     'S -> if ( C ) S else S ',
#     'S -> S ; S ',
#     'C -> E > E ',
#     'C -> E < E ',
#     'C -> E == E ',
#     'E -> E + T ',
#     'E -> E - T ',
#     'E -> T ',
#     'T -> F ',
#     'T -> T * F ',
#     'T -> T / F ',
#     'F -> ( E ) ',
#     'F -> id ',
#     ]
#
# # 说明：列表中的状态并不是全部状态
# production = ["P", "E", "D", "L", "S", "C", "T", "F"]
# s = []
# t = ['id', 'if', "+", "-", "/", "int10", "==", "(", ")", "float", "int", ";", "NULL", "="]


class Grammar_Translation(object):
    """Grammar Translation Class"""
    def __init__(self):
        """Initial
        This func is to make token file and symbol table file
        and start grammar translation
        """
        self.f = open("code.txt", "w")
        file_name = "C.c"
        f_token = open("token.txt", "w")
        f_symbol = open("symbol_table.txt", "w")
        LexicalAnalyse(file_name).fun_init(f_token, f_symbol)  # 词法分析
        LRGramAnalyze(file_name)  # 语法分析
        self.grammar_translate()

    def translate_other(self, parma):
        """translate from C.c which isn't a statement sentence"""
        try:
            if parma.find(t[1]) != 1:
                print >> self.f, str(100),  "     ", parma[:-2]
            else:
                pass
            self.translate_Other()
        except Exception as e:
            print "Error -> ", str(e)

    def translate_if(self):
        try:
            if self.text[5].find(t[0]) != 1:
                text = " goto %d" % (len(t)*7+6)
                print >> self.f, str(102), "     ", self.text[5]+text
            else:
                pass
            self.translate_x()
        except Exception as e:
            print "Error -> ", str(e)

    def translate_x(self):
        try:
            if self.text[4].find(t[0]) != 1:
                text = "goto %d" % (len(t)*7+9)
                print >> self.f, str(103), "     ", text
            else:
                pass
            self.translate_X()
        except Exception as e:
            print "Error -> ", str(e)

    def translate_X(self):
        try:
            if self.text[4].find(t[0]) != 1:
                text = "t1 = a+b"
                Text = "c = t1"
                print >> self.f, str(104), "     ", text
                print >> self.f, str(105), "     ", Text
                print >> self.f, str(106), "     ", "goto"
            else:
                pass
            self.translate_xx()
        except Exception as e:
            print "Error -> ", str(e)

    def translate_xx(self):
        try:
            if self.text[4].find(t[0]) != 1:
                text = "t2 = a-b"
                Text = "c = t2"
                print >> self.f, str(107), "     ", text
                print >> self.f, str(108), "     ", Text
            else:
                pass
            self.print_msg()
        except Exception as e:
            print "Error -> ", str(e)

    def translate_Other(self):
        try:
            if self.text[4].find(t[0]) != 10:
                print >> self.f, str(101), "     ", self.text[4][:-2]
            else:
                pass
            self.translate_if()
        except Exception as e:
            print "Error -> ", str(e)

    def print_msg(self):
        self.f.close()
        with open("code.txt", 'r') as f:
            text = f.read()
            text = text.split("\n")
            for i in text:
                print i

    def translate_line(self, parma):
        """translate from C.c single sentence"""
        # print parma
        if parma.find(t[10]) != -1:
            # statement sentence
            pass
        else:
            self.translate_other(parma)

    def grammar_translate(self):
        """grammar translation func"""
        f_source = open("C.c", 'r')
        self.text = f_source.read()
        self.text = self.text.split("\n")
        print >> self.f, "源程序"
        for i in self.text:
            print >> self.f, str(i)
        print >> self.f, "\n三地址代码"
        self.translate_line(self.text[3])


if __name__ == '__main__':
    Grammar_Translation()




