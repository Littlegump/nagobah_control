#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import sys
import os

def layer1():
    print """
欢迎来到dago_control界面！！！
--------Layer1--------:
1. list operation
2. delete operation
3. modify operation
4. exit dago_control
""",
    choice = raw_input("This is layer1, 请选择操作类型(输入数字)：")
    return choice

def layer2():
    print """
--------Layer2--------:<list>
1. list all jobs
2. list a job
3. list a task
4. back to Layer1
""",
    choice = raw_input("This is layer2 请选择操作类型(输入数字)：")
    return choice

def layer3():
    """这里必须调用api，以为设计依赖性问题"""
    print """
--------Layer2--------:<delete>
1. delete all jobs
2. delete a job
3. delete a task
4. back to Layer1
""",
    choice = raw_input("This is layer2 请选择操作类型(输入数字)：")
    return choice

def layer4():
    """这里必须调用api，以为设计依赖性问题"""
    print """
--------Layer2--------:<edit>
1. delete all jobs
2. delete a job
3. delete a task
4. back to Layer1
""",
    choice = raw_input("This is layer2 请选择操作类型(输入数字)：")
    return choice

def delete_all_jobs():
    pass

def delete_all_jobs():
    pass

def delete_all_jobs():
    pass

def function_list():
    print "list"
    choice2 = layer2()
    while choice2 != 4:
        if choice2 == "1":
        # 这里显示全部的job
            os.system('clear')
            print "jobname:tasks:ntes"
        elif choice2 == "2":
            job_name = raw_input("input your choice job_name: ")
        elif choice2 == "3":
            pass
        return

def function_delete():
    print "delete"

def function_edit():
    print "edit"

def main():
    try:
        choice = layer1()
        while choice != '4':
            if choice == '1':
                function_list()
            elif choice == "2":
                function_delete()
            elif choice == "3":
                function_edit()
            choice = layer1()









    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    main()
