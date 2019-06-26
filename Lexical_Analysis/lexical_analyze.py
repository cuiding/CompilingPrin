# usr/bin/env python
# encoding:utf-8


from lex_grammer import * # 词法分析源
import re


class LexicalAnalyse(object):
    def __init__(self, filename):
        """
        :param filename:
        :return text
        """
        with open(filename, 'r') as f:
            self.text = f.read()

    def analyse(self, parma):
        """
        :param parma:
        :return: Null
        """
        # print parma
        parma.strip()
        for i in divid_op:
            # 匹配分隔符
            if parma.find(i) != -1:
                print >> self.f_out, "[", i, "]", "--- [ 界限符 ]"
                y = 10 - len("界限符")
                x = 5 - len(parma)
                print >> self.f_token, parma + "$", x * " ", "(  -  , ",
                print >> self.f_token, "界限符 ", y*" ", ") ", str(self.count)
                parma = parma.replace(i, "")  # 将找到的字符串从符号串中删除
                return 1
            else:
                pass
        for j in math_op:
            # 匹配运算符
            if parma.find(j) != -1:
                if j == "<" and parma.find(">") != -1:
                    y = 10 - len("运算符")
                    x = 10 - len("界限符")
                    z = 5 - len(parma)
                    print >> self.f_token, parma + "$", x * " ", "(  -  , ",
                    print >> self.f_out, "[", j, "]", "--- [ 运算符 ]"
                    print >> self.f_token, "运算符 ", y*" ", ") ", str(self.count)
                    print >> self.f_out, "[", parma[1:parma.find(">")], "]", "--- [ 运算符 ]"
                    print >> self.f_token, "运算符 ", y*" ", ") ", str(self.count)
                    print >> self.f_out, "[", ">", "]", "--- [ 界限符 ]"
                    print >> self.f_token, "界限符 ", x*" ", ") ", str(self.count)
                    return 1
                else:
                    y = 10 - len("运算符")
                    print >> self.f_out, "[", j, "]", "--- [ 运算符 ]"
                    x = 5 - len(parma)
                    print >> self.f_token, parma + "$", x * " ", "(  -  , ",
                    print >> self.f_token, "运算符 ", y*" ", ") ", str(self.count)
                    return 1
            else:
                pass
        for key_word in key_word_list:
            # 匹配关键字
            if parma.find(key_word) != -1:
                y = 10 - len("关键字")
                print >> self.f_out, "[", key_word, "]", "--- [ 关键字 ]"
                x = 5 - len(parma)
                print >> self.f_token, parma + "$", x * " ", "(  -  , ",
                print >> self.f_token, "关键字 ", y*" ", ") ", str(self.count)
                parma = parma.replace(key_word, "")
                return 1
            else:
                pass
        for k in str(range(0, 10)):
            # 数字识别
            if parma[0] == k:
                if re.search('[a-zA-Z]', parma) or parma.find("_") != -1:
                    print >> self.f_out, "[", parma, "]", "--- [ ERROR: 数字不能放在变量首位! ]"
                    return -1
                else:
                    print >> self.f_out, "[", k, "]", "--- [ 数字 ]"
                    y = 10 - len("数字")
                    x = 5 - len(parma)
                    print >> self.f_token, parma + "$", x * " ", "(  -  , ",
                    print >> self.f_token, "数字 ", y*" ", ") ", str(self.count)
                    # parma = parma.replace(k, "")
                    return 1
            else:
                pass
        if len(parma) > 0:
            print >> self.f_out, "[", parma, "]", "--- [ 分隔符 ]"
            y = 10 - len("")
            x = 5 - len(parma)
            print >> self.f_token, parma + "$", x * " ", "(  -  , ",
            print >> self.f_token, "标识符 ", y*" ", ") ", str(self.count)
        else:
            pass

    def fun_init(self, f_out, f_token):
        text = self.text.split("\n")
        self.f_out = f_out
        self.f_token = f_token
        self.count = 1
        for line in text:
            # 分隔出每一行
            print >> self.f_out, "\nline: ", str(self.count)
            if line.find("//") != -1:
                print >> self.f_out, "[", line, "]", "--- [ 注释 ]"
            else:
                for word in line.split(" "):
                    word = word.strip()
                    if len(word) >= 1:
                        self.analyse(word)
                    else:
                        # print "Null"
                        pass
                # print >> self.f, line
            self.count += 1
        f_out.close()
        f_token.close()
        self.f_token.close()
        self.f_out.close()

    def keyword_analyse(self, parma):
        """
        :param parma:
        :return: True if parma is a keyword or False
        """
        for key in key_word_list:
            if key == parma:
                return True
            else:
                pass
        return False


if __name__ == '__main__':
    file_name = "C.c"  # 被分析的文件名
    f_out = open("token.txt", "w")
    f_token = open("symbol_table.txt", "w")
    LexicalAnalyse(file_name).fun_init(f_out, f_token)
