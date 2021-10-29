import csv

def readCSV(file):
    '''
    读取csv文件
    :param file: 输入文件路径
    :return: 返回列表
    '''
    rows = []
    with open(file, 'r', encoding='utf-8') as f:
        read = csv.reader(f)  # 返回一个可迭代对象
        for row in read:  # 一行一行的迭代
            rows.append(row)
    return rows
def readCSV_top_20rows(file):
    # 读取前20行
    rows = []
    with open(file, 'r', encoding='utf-8') as f:
        read = csv.reader(f)  # 返回一个可迭代对象
        for i, row in enumerate(read):  # 一行一行的迭代
            if i>=20:
                break
            rows.append(row)
    return rows

def overWriteCSV(rows,file): # data是列表
    with open(file,'w',encoding='utf-8',newline='') as f:
        write = csv.writer(f)
        write.writerows(rows)

def addWriteCSV(row,file): # data一次只加一行
    with open(file,'a',encoding='utf-8',newline='') as f:
        write = csv.writer(f)
        write.writerow(row)


if __name__ == '__main__':

    # rows = [
    #     ['1222','节点1'],
    #     ['3333','节点2']
    # ]
    # overWriteCSV(rows, './test.csv')
    row = ['122','节点3']
    # addWriteCSV(row,'./data/adminWeChatData.csv')
    read = readCSV_top_20rows('./data/log.csv')
    print(read)
    # self.historyData = fileReadAndWrite.readCSV('data/historyData.csv')
    # read = readCSV('./data/adminWeChatData.csv')
    # print(read)
    # print(len([[]]))
    # csv,当文本是空的,返回[], 当吸入一维数据自动转为二维,当读取数据自动转为2维度
