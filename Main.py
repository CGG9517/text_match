# this is the Main file
from utils.file_util import FileUtil
from utils.wordhelper import WordHelper


if __name__ == '__main__':
    # todo 首先导入语料文件，建立索引
    path = ''
    lines = FileUtil.get_file(path)
    words_line_dict = dict()  # 用于存放词与短语的对应关系

    words = []  # 用于存放一行短语的分词结果
    # todo 分词
    for each_line in lines:
        words = WordHelper.seg(each_line)



    pass