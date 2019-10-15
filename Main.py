# this is the Main file
from utils.file_util import FileUtil
from utils.wordhelper import WordHelper
from utils.pinyin_util import *
from entity import *


if __name__ == '__main__':
    # todo 首先导入语料文件，建立索引
    path = 'testLines.txt'
    lines = FileUtil.get_file(path)
    words_line_dict = dict()  # 用于存放词与短语对象的对应关系
    normal_pinyin_ciyu_dict = dict()  # 用于存放拼音与词对象的对应关系
    first_pinyin_ciyu_dict = dict()  # 用于存放拼音与词对象的对应关系

    words = []  # 用于存放一行短语的分词结果

    for each_line in lines:
        newPhrase = Phrase(each_line)
        words = WordHelper.seg(each_line)  # todo 分词
        for each_word in words:
            first_pinyin = PinyinUtil.get_first_pinyin(each_word)  # 获取首拼
            normal_pinyin = PinyinUtil.get_lazy_pinyin(each_word)  # 获取全拼
            new_ciyu = Ciyu(each_word, normal_pinyin, first_pinyin)

            # if each_word not in fir

            if each_word not in words_line_dict:
                words_line_dict[each_word] = list()

            words_line_dict[each_word].append(newPhrase)
    print(words_line_dict)

    pass
