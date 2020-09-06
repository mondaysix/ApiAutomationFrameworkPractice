# coding:utf-8

from optparse import OptionParser
import pytest
import os

root_path = os.path.abspath(".")


def parse_option():
    """
    添加命令行参数，并解析
    :return:
    """
    option_parser = OptionParser()  # dest是存储的变量 action=store 表示将命令行参数值保存到options对象里
    option_parser.add_option("-e", "--environment",
                             dest="env",
                             action="store",
                             help="Please choose an environment for this application: test, prod")
    option_parser.add_option("-p", "--project",
                             dest="project",
                             action="store",
                             help="Please choose an project: server,client")
    opts, args = option_parser.parse_args()
    return opts, args  # options 保存有命令行参数值  args由positional arguments组成的列表


def main():
    """
    读取命令行参数，并以pytest运行
    :return:
    """

    (options, args) = parse_option()
    env = str(options.env).split("=")[1]#prod
    project = str(options.project).split("=")[1]#client
    environment_file = root_path + "/environment.txt"#环境选择的文件路径

    case_path = root_path + "/testcases/" + project#测试案例存放的路径
    report_path = root_path + "/reports/allure/xml/"#测试报告存放的路径

    try:
        with open(environment_file, 'w') as f:
            f.write(env)
            f.write("\n")
            f.write(project)
    except FileNotFoundError:
        print(environment_file, "File Not Found!")

    pytest.main(["-v", "-s", "--alluredir", report_path, case_path])# --alluredir参数的作用是指出生成的报告文件夹
    #-v: 丰富信息模式, 输出更详细的用例执行信息
    #-s: 显示程序中的print/logging输出


if __name__ == "__main__":
    main()
    #run.py -e=prod -p=client
    #allure generate ./reports/allure/xml -o ./reports/html --clean