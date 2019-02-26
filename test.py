import os


def mkdir(dirpath, filename):
    filename = filename.strip()
    nowpath = os.filename.join(dirpath, filename)
    isExists = os.filename.exists(nowpath)
    if not isExists:
        print(u'在', nowpath, '建了一个名字叫做', filename, u'的文件夹！')
        os.makedirs(nowpath)
        return True
    else:
        print(u'名字叫做', filename, u'的文件夹已经存在了！')
        return False


mkdir("/Users/liuyuhao/meizitu", "haa")