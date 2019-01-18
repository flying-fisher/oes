#!/usr/bin/env python3
# coding=utf-8
import re
import xlwt
import sys
import os
try:  # 导入模块
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

#################################################读取配置文件#########################################################
def handle_config():
    #配置文件配置DBid，配置sql文件名
    config = ET.parse("db2dbConfig.xml").getroot()
    walkData(config)
def walkData(root):  
    #遍历每个子节点  
    global resourceFile
    global resultFile
    global resourceHost
    global destHost
    global resourceDB
    global destDB
    children_node = root.getchildren()  
    if len(children_node) == 0: 
        return  
    for child in children_node:  
        if child.tag == 'resourceFile':
            resourceFile = child.text.strip()
        if child.tag == 'resultFile':
            resultFile = child.text.strip()
        if child.tag == 'resourceDB':
            resourceDB = child.text.strip()
        if child.tag == 'destDB':
            destDB = child.text.strip()
        if child.tag == 'resourceHost':
            resourceHost = child.text.strip()
        if child.tag == 'destHost':
            destHost = child.text.strip()
        walkData(child)  
    return
#######################################################全局变量##########################################################
resourceFile = ''
resultFile = ''
resourceDB = ''
destDB = ''
resourceHost = ''
destHost = ''
#################################################读取sql脚本并写结果#######################################
def main_process():
    tableName = ''                #表名
    cols = []                     #字段名
    stageId = 0                   #自增的stageId
    with open('result.xml', 'w') as fpw:
        with open("test.sql", "r+") as fr:
            fpw.writelines('<?xml version="1.0" encoding="UTF-8"?>\n')
            fpw.writelines("<Conf>\n")
            #开始解析sql文件
            line = fr.readline().lower()
            while line:
                if line.find("create") >= 0 and line.find("table") >= 0:
                    #截取数据库名后的表名，并去掉后面的)
                    tableName = line[line.find("."):-1].replace("(","").strip()
                elif line.find("primary key") >= 0:
                    line = fr.readline()
                    continue
                elif line.strip() == ')':
                    #从这继续往下写
                    stageId = stageId + 1
                    handle_stage(fpw,tableName,cols,stageId)
                    #右括号代表create table语句的结束，重置cols
                    cols = []
                    #去掉两个create语句间无用的字符
                    line = fr.readline().lower()
                    while line.find("create") < 0 and line.find("table") < 0 and line:
                        line = fr.readline().lower()
                    continue
                elif len(line.strip()) > 0:
                    #通过分割，把create table语句中的字段名挑出来
                    cols.append(re.split(" |	",line.strip())[0])
                line = fr.readline().lower()
            #写末尾
            fpw.writelines("</Conf>\n")
def handle_stage(fpw,tableName,cols,stageId):
    fpw.writelines("\t<stage id=\"" + str(stageId) + "\" describe=\"\">\n")
    handle_drowout(fpw,tableName,cols)
    handle_load(fpw,tableName,cols)
    fpw.writelines("\t</stage>\n")
def handle_drowout(fpw,tableName,cols):
    fpw.writelines("\t\t<drawout DBid=\""+resourceHost+"\"><![CDATA[\n")
    fpw.writelines("select\n")
    tmpStr = ''
    for col in cols:
        tmpStr += col + ','
    fpw.writelines(tmpStr[:-1]+"\n")  #去掉多余的逗号
    fpw.writelines("from\n")
    fpw.writelines(tableName[1:]+"\n")  #去掉多余的.号
    fpw.writelines("]]></drawout>\n")
def handle_load(fpw,tableName,cols):
    fpw.writelines("\t\t<Load DBid=\""+destHost+"\" tableName=\""+tableName[1:]+"\">\n")
    handle_dimension(fpw,cols)
    handle_cols(fpw,cols)
    fpw.writelines("\t\t</Load>\n")
def handle_dimension(fpw,cols):
    fpw.writelines("\t\t\t<Dimension>\n")
    #如果dimension没有会报错，就随便弄了一个
    handle_col(fpw,cols[0])
    fpw.writelines("\t\t\t</Dimension>\n")
def handle_cols(fpw,cols):
    fpw.writelines("\t\t\t<Cols>\n")
    for col in cols:
        #因为随便把一列弄到dimension了，这里就不要了
        if col == cols[0]:
            continue
        handle_col(fpw,col)
    fpw.writelines("\t\t\t</Cols>\n")
def handle_col(fpw,col):
    fpw.writelines("\t\t\t\t<col name=\""+col+"\">["+col+"]</col>\n")


#######################################################主函数########################################################
if __name__ == '__main__': 
    handle_config()
    main_process()
