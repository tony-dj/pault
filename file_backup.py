#!/usr/bin/env python
#_*_ coding=utf-8 _*_
import sys
import os
import re
import filecmp
import shutil
import commands

def compareme(dir1,dir2,list1 = []):
    dircomp = filecmp.dircmp(dir1,dir2)
    # 将源目录中的新文件和改动过文件加入source_list
    only_in_one = dircomp.left_only
    diff_in_one = dircomp.diff_files
    [ list1.append(os.path.join(dir1,x)) for x in only_in_one ]
    [ list1.append(os.path.join(dir1,x)) for x in diff_in_one ]
    # 如果源目录和目标存在相同子目录，则递归执行
    if len(dircomp.common_dirs) > 0:
        for item in dircomp.common_dirs:
            compareme(os.path.join(dir1,item),os.path.join(dir2,item),list1)
    return list1

def make_sub_dir(dir1,dir2):
    #在备份文件夹中创建新目录
    source_list = compareme(dir1,dir2)
    dest_list = []
    create_bool = False
    for item in source_list:
        dest_file = re.sub(dir1,dir2,item)
        dest_list.append(dest_file)
        if os.path.isdir(item):
            if not os.path.exists(dest_file):
                os.makedirs(dest_file)
                create_bool = True
    if create_bool:
        make_sub_dir(dir1,dir2)

def gen_bk_dir(dir1,dir2):
    # 根据源目录文件列表source_list生成目标文件列表dest_list
    dest_list = []
    list1 = []
    source_list = compareme(dir1,dir2,list1)
    for item in source_list:
        dest_file = re.sub(dir1,dir2,item)
        dest_list.append(dest_file)
    return source_list,dest_list    

def main():
    if len(sys.argv) > 2:
        dir1 = sys.argv[1]
        dir2 = sys.argv[2]
    else:
        print 'Usage:',sys.argv[0],'source_dir backup_dir'
        sys.exit()

    dir1 = os.path.abspath(dir1)
    dir2 = os.path.abspath(dir2)
    make_sub_dir(dir1,dir2)
    data = commands.getstatusoutput('ls -lR /root/stu/test2')
    for line in data:
        print line
    s_list,d_list = gen_bk_dir(dir1,dir2)
    print 'update_item:'
    print s_list
    copy_pair = zip(s_list,d_list)
    for item in copy_pair:
    	shutil.copyfile(item[0],item[1]) 

if __name__ == '__main__':
    main()



   
        
