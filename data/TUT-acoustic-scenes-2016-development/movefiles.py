import os
import csv
import shutil
import sys


def getFileList(metaFile):
    FileList = {}
    with open(metaFile, 'rt') as f:
        for row in csv.reader(f, delimiter='\t'):
            if len(row) == 2:
                # Scene meta
                filePath = row[0]
                scene = row[1]
                if scene in FileList:
                    FileList[scene].append(filePath)
                else:
                    FileList[scene] = [filePath]
    return FileList


def checkpath(path):
    # mkdir
    if not os.path.isdir(path):
        os.makedirs(path)


def copy_files(rootpath, filelist):
    for k,v in filelist.items():
        sub_path = os.path.join(rootpath, k)
        checkpath(sub_path)
        for file in v:
            if os.path.isfile(file):
                # copy
                # shutil.copy("oldfile", "newfile")
                shutil.copy(file,sub_path)
                print 'move ' + os.path.split(file)[1] + ' to ' + sub_path


def main(argv):
    FileList = getFileList('meta.txt')
    root_path = 'dataset/'
    checkpath(root_path)
    #copy_files(root_path,FileList)


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except (ValueError, IOError) as e:
        sys.exit(e)




