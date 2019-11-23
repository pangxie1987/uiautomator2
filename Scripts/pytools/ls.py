'''
Windows模拟ls命令
https://mp.weixin.qq.com/s/_9EERWgCbUpVuvYdTDedwQ
'''

import os
import argparse

parser = argparse.ArgumentParser(prog='ls', description='显示文件夹下的文件')

# 指定参数
parser.add_argument('-a', '--all', const=True, nargs='?', help='是否显示隐藏文件')
parser.add_argument('-d', '--directory', help='指定显示的目录，如果不指定，默认为当前目录')
parser.add_argument('-r', '--recursion', const=True, nargs='?', help='是否递归现实')

# 解析参数
args = parser.parse_args()

directory = args.directory

if directory:
    if not os.path.exists(directory):
        raise ValueError(f'{directory} do not exist')

    if not os.path.isdir(directory):
        raise ValueError(f'{directory} is not a directory')

else:
    directory = '.'


class LsCommand():
    def __init__(self, show_all=False, directory='.', recursion=False):
        '''
        :param show_all: 是否显示隐藏文件
        :param directory: 指定的文件目录
        :param recursion: 是否递归显示目录下的文件
        '''
        self.show_all = show_all
        self.recursion = recursion
        self.directory = os.path.abspath(directory)
        
    def handle_dir(self, directory, grade=1, placeholder='--'):
        '''
        处理目录
        :param directory: 文件目录
        :param grade: 目录层级
        :param placeholder: 子目录文件前面的占位符
        :return:
        '''
        # 判断是否为文件夹

        # grade是否增加过了

        # os.listdir: 列出当前文件夹下面的所有文件和文件夹
        # 遍历目录下的文件，文件夹
        pass

    def show_file_or_dir(self, file, prefix=''):
        # 如果不显示隐藏文件
        # 打印前缀和文件名
        pass

    def run(self):
        '''
        运行ls命令
        :return :
        '''
        pass

if __name__ == '__main__':
    ls = LsCommand(bool(args.all), directory, bool(args.recursion))
    ls.run()