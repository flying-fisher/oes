# coding=utf-8
import xlwt
import sys
import os
try:  # 导入模块
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
    
col = 0
row = 0   
#FDDCell
def handle_RNC(root, excel):        
    RNCs = root.getiterator("RNC")
    for RNC in RNCs:    
        NodeBs = RNC.getiterator("NodeB")
        for NodeB in NodeBs:
            handle_NodeB(RNC,NodeB,excel)
def handle_NodeB(RNC,NodeB,excel):
    FDDCells = NodeB.getiterator("FDDCell")
    for FDDCell in FDDCells:
        handle_FDDCell(RNC,NodeB,FDDCell,excel)
def handle_FDDCell(RNC,NodeB,FDDCell,excel):
    global row
    global col
    excel.write(row, col, RNC.get("id").strip())
    col = col + 1
    excel.write(row, col, NodeB.get("id").strip())
    col = col + 1
    excel.write(row, col, FDDCell.get("id").strip())
    col = col + 1
    excel.write(row, col, RNC.get("version").strip())
    col = col + 1
    excel.write(row, col, RNC.get("model").strip())
    col = col + 1
    cellId = FDDCell.getiterator("cellId")
    for node in cellId:    
        excel.write(row, col, node.text.strip())         
        col = col + 1
    dualCellIds = FDDCell.getiterator("dualCellId")
    for dualCellId in dualCellIds:
        dualCellIdValue = dualCellId.getiterator("value")
        tmp = []
        for node in dualCellIdValue:
            tmp.append(node.text.strip())
            tmp.append(',')    
        tmp = tmp[:-1]
        excel.write(row, col, tmp)
        col = col + 1
    localCellId = FDDCell.getiterator("localCellId")
    for node in localCellId:    
        excel.write(row, col, node.text.strip())         
        col = col + 1
    locationAreaCode = FDDCell.getiterator("locationAreaCode")
    for node in locationAreaCode:    
        excel.write(row, col, node.text.strip())         
        col = col + 1
    twinCellLists = FDDCell.getiterator("twinCellList")
    for twinCellList in twinCellLists:
        twinCellListValue = twinCellList.getiterator("value")
        tmp = []
        for node in twinCellListValue:  
            tmp.append(node.text.strip())
            tmp.append(',')
        tmp = tmp[:-1]
        excel.write(row, col, tmp)
        col = col + 1
    row = row+1
    col = 0
    
#BTSCELL
def handle_BTSCell(root, excel):        
    BTSEquipments = root.getiterator("BTSEquipment")
    for BTSEquipment in BTSEquipments:    
        BTSCells = BTSEquipment.getiterator("BTSCell")
        for BTSCell in BTSCells:
            handle_BTS(BTSEquipment,BTSCell,excel)
def handle_BTS(BTSEquipment,BTSCell,excel):
    global row
    global col
    excel.write(row, col, BTSEquipment.get("id").strip())
    col = col + 1
    excel.write(row, col, BTSCell.get("id").strip())
    col = col + 1
    excel.write(row, col, BTSEquipment.get("version").strip())
    col = col + 1
    excel.write(row, col, BTSEquipment.get("model").strip())
    col = col + 1
    antennaAccessLists = BTSCell.getiterator("antennaAccessList")
    for antennaAccessList in antennaAccessLists:
        antennaAccessListValue = antennaAccessList.getiterator("value")
        tmp = []
        for node in antennaAccessListValue:
            tmp.append(node.text.strip())
            tmp.append(',')    
        tmp = tmp[:-1]
        excel.write(row, col, tmp)
        col = col + 1
    localCellId = BTSCell.getiterator("localCellId")
    for node in localCellId:    
        excel.write(row, col, node.text.strip())         
        col = col + 1
    row = row+1
    col = 0
#RRH
def handle_RemoteRadioHead(root, excel):        
    BTSEquipments = root.getiterator("BTSEquipment")
    for BTSEquipment in BTSEquipments:    
        RemoteRadioHeads = BTSEquipment.getiterator("RemoteRadioHead")
        for RemoteRadioHead in RemoteRadioHeads:
            handle_RRH(BTSEquipment,RemoteRadioHead,excel)
def handle_RRH(BTSEquipment,RemoteRadioHead,excel):
    global row
    global col
    excel.write(row, col, BTSEquipment.get("id").strip())
    col = col + 1
    excel.write(row, col, RemoteRadioHead.get("id").strip())
    col = col + 1
    excel.write(row, col, BTSEquipment.get("version").strip())
    col = col + 1
    excel.write(row, col, BTSEquipment.get("model").strip())
    col = col + 1
    antennaAccessLists = RemoteRadioHead.getiterator("antennaAccessList")
    for antennaAccessList in antennaAccessLists:
        antennaAccessListValue = antennaAccessList.getiterator("value")
        tmp = []
        for node in antennaAccessListValue:
            tmp.append(node.text.strip())
            tmp.append(',')    
        tmp = tmp[:-1]
        excel.write(row, col, tmp)
        col = col + 1
    row = row+1
    col = 0
    
def hand_Config(root,config, label, file):
    global col
    global row
    row = 0
    col = 0
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Sheet1')
    titles = config.getiterator(label)
    for title in titles:    
        titleValue = title.text.split(",")
        for node in titleValue:
            #strip同java的trim
            ws.write(row, col, node.strip())
            col = col + 1
    row = row + 1
    col = 0
    if label == 'cell':
        handle_RNC(root,ws)
    if label == 'bts':
        handle_BTSCell(root,ws)
    if label == 'rru':
        handle_RemoteRadioHead(root,ws)
    wb.save(file)
        
if __name__ == '__main__': 
    #配置文件的解析
    rootdir = '/home/tmn/newtmn/wlzy_wcdma/data/alc'
    list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    file = ''
    for i in range(0,len(list)):
        path = os.path.join(rootdir,list[i])
        if os.path.isfile(path):
            file = path
    root = ET.parse(file).getroot()
    config = ET.parse("config.xml").getroot()
    hand_Config(root, config, "cell", "/home/tmn/newtmn/wlzy_wcdma/interfance_file/fddcell.xls")
    hand_Config(root, config, "bts", "/home/tmn/newtmn/wlzy_wcdma/interfance_file/btscell.xls")
    hand_Config(root, config, "rru", "/home/tmn/newtmn/wlzy_wcdma/interfance_file/rrh.xls")