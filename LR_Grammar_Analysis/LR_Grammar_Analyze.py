#! usr/bin/env python
# coding:utf-8

from Lexical_Analysis.lexical_analyze import LexicalAnalyse
from production import origin_production_list, s, t  # 产生式


class LRGramAnalyze:
    def __init__(self, file_path):
        """initial"""
        self.LRX = open("LR.txt", "w")
        self.language = []
        with open("symbol_table.txt", "w") as f_token:
            f_out = open("token.txt", "w")
            LexicalAnalyse(file_path).fun_init(f_out, f_token)  # 调用词法分析器，生成TOKEN表
        self.grammer_analyze_init()
        self.grammer_analyse()

    def op_list_init(self, parma):
        self.language.append(parma)

    def grammer_analyze_init(self):
        with open("symbol_table.txt", "r") as f:
            self.text = f.read()
            f.close()
        self.text = self.text.split("\n")
        temp = []
        for i in range(1, 10):
            for line in self.text:
                if line.endswith(str(i)):
                    index = line.find(" ") - 1  # 去掉$符号
                    parma = line[:index]  # 符号
                    temp.append(parma)
            self.op_list_init(temp)
            temp = []  # 清空temp内存
            # 注：不能使用[:]的方式清理一个被调用的list，会发生数据提前清空的错误

    def grammer_Analyse(self, line, location):
        if location == 1 or location == 2 or location == 3:
            for word in line:
                for i in origin_production_list:
                    if i.find(word) != -1:
                        pass
                    else:
                        line[1] = "id"
            print >> self.LRX, "0            ", "NULL        ", self.msg+"$       ", "移入%s       " % line[0]
            try:
                for i in origin_production_list:
                    if i.find(line[0]) != -1:
                         locate = origin_production_list.index(i)
                         self.temp = origin_production_list[locate][0]
                         print >> self.LRX, "0" + str(locate), "          ", line[0], "       ",\
                             self.msg[len(line[0]):]+"$   ", "      按照%s归约" % i
                    else:
                        pass
            except Exception as e:
                print "can't find %s ->" % line[0], str(e)
            try:
                for j in origin_production_list:
                    if j.find(self.temp+" "+line[1]) != -1:
                        locate = origin_production_list.index(j)
                        print >> self.LRX, "0" + str(locate), "           ", self.temp, "          ", \
                            self.msg[len(line[0]):]+"$       ", "移入%s" % (line[1])
                    else:
                        pass
            except Exception as e:
                print "Error ->", str(e)
            try:
                for k in origin_production_list:
                    if k.find(self.temp+" "+line[1]+" "+line[2]) != -1:
                        locate = origin_production_list.index(k)
                        print >> self.LRX, "0" + str(locate), "          ", self.temp+line[1], "         ", \
                            self.msg[len(line[0])+len(line[1])+1:]+"$", "         移入%s" % (line[2])
                        print >> self.LRX, "0" + str(locate), "          ", origin_production_list[locate][0], "      "\
                                                            "      $", "           按照%s归约" % k
                        print >> self.LRX, "0" + str(locate), "           ", origin_production_list[locate-1][0], "  " \
                                                  "          $", "          按照%s归约"%origin_production_list[0]
                        print >> self.LRX, "0", "             ",origin_production_list[locate-1][0],  "              $", "            接受"
                    else:
                        pass

            except Exception as e:
                print "Error ->", str(e)

        elif location == 4 or location == 5:
            for word in line:
                for i in origin_production_list:
                    if i.find(word) != -1:
                        pass
                    else:
                        line[0], line[2] = "id", "id"
            print >> self.LRX, "0            ", "NULL        ", self.msg+"$      ", "移入%s       " % line[0]
            for j in origin_production_list:
                if j.find(line[0]+" "+line[1]) != -1:
                    locate = origin_production_list.index(j)
                    print >> self.LRX, "0", "           ", line[0], "          ", \
                        self.msg[len(line[0]):]+"$      ", "移入%s" % line[1]
                    print >> self.LRX, "0", "           ", line[0]+line[1], "          ",\
                        self.msg[len(line[0])+len(line[1]):]+"$      ", "移入%s" % line[0]
                else:
                    pass
            locat = 16
            print >> self.LRX, "0" + str(locat), "     ", line[0] + line[1] + line[2], "          ",\
                self.msg[len(line[0]) + len(line[1]) + len(line[2]):] + \
                "$      ", "按照%s归约" % origin_production_list[locat]
            temp = origin_production_list[locat][0]
            print >> self.LRX, "0" + str(locate) + str(locat), "     ", line[0] + line[1] + temp, "          ", \
                     self.msg[len(line[0]) + len(line[1]) + len(line[2]):] + "$      ", "按照%s归约" % origin_production_list[12]
            print >> self.LRX, "0" + str(locate) + str(locat) + str(12), "     ", line[0] + line[1] + origin_production_list[12][0], "          ", \
                     self.msg[len(line[0]) + len(line[1]) + len(line[2]):] + "$      ", "按照%s归约" % origin_production_list[11]
            print >> self.LRX, "0" + str(locate) + str(locat) + str(12) + str(3), "     ", line[0] + line[1] + origin_production_list[11][0], "          ", \
                     self.msg[len(line[0]) + len(line[1]) + len(line[2]):] + "$      ", "按照%s归约" % origin_production_list[3]
            print >> self.LRX, "0" + str(locate) + str(locat) + str(12) + str(3), "           ", origin_production_list[3][0], "          ", \
                     self.msg[len(line[0]) + len(line[1]) + len(line[2]):] + "$      ", "移入%s" % line[3]
            print >> self.LRX, "0" + str(locate) + str(5), "           ", origin_production_list[3][0] + line[3], "          ", \
                     self.msg[len(line[0]) + len(line[1]) + len(line[2]) + len(line[3]):] + "$      ", "按照%s归约" % origin_production_list[5]
            print >> self.LRX, "0", "           ", origin_production_list[3][0], "          ", \
                     self.msg[len(line[0]) + len(line[1]) + len(line[2]) + len(line[3]):] + "$      ", "接受"

    def grammer_analyse(self):
        location = 1
        for line in self.language:
            count = 0
            print >> self.LRX, "分析第%d行: "%int((self.language.index(line)) + 1),
            for word in line:
                count += 1
                print >> self.LRX, word,
            temp = ""
            for i in range(0, count):
                temp += "str(line[%d])+' '+" % i
            temp = temp[:-5]
            self.msg = eval(temp)
            print >> self.LRX, "\n结果如下: "
            print >> self.LRX, "STACK       ", "SYMBOL       ", "INPUT       ", "ACTION"
            self.grammer_Analyse(line, location)
            # sleep(9999)
            print >> self.LRX, "\n\n"
            location += 1


if __name__ == '__main__':
    file_name = "C.c"
    G = LRGramAnalyze(file_name)




