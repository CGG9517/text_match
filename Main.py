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
    normal_pinyin_ciyu_dict = dict()  # 用于存放全拼拼音与词对象的对应关系
    first_pinyin_ciyu_dict = dict()  # 用于存放首写拼音与词对象的对应关系
    init_pinyin_ciyu_dict = dict()  # 用于存放声母与词对象的对应关系

    words = []  # 用于存放一行短语的分词结果

    for each_line in lines:
        _full_pinyin = PinyinUtil.get_lazy_pinyin(each_line)
        newPhrase = Phrase(each_line, _full_pinyin)
        words = WordHelper.seg(each_line)  # todo 分词
        for each_word in words:
            first_pinyin = PinyinUtil.get_first_pinyin(each_word)  # 获取首拼
            normal_pinyin = PinyinUtil.get_lazy_pinyin(each_word)  # 获取全拼
            init_pinyin = PinyinUtil.get_init_pinyin(each_word)  # 获取声母
            new_ciyu = Ciyu(each_word, normal_pinyin, first_pinyin)

            # 添加word
            if first_pinyin not in normal_pinyin_ciyu_dict:
                first_pinyin_ciyu_dict[first_pinyin] = list()
            first_pinyin_ciyu_dict[first_pinyin].append(each_word)

            if normal_pinyin not in normal_pinyin_ciyu_dict:
                normal_pinyin_ciyu_dict[normal_pinyin] = list()
            normal_pinyin_ciyu_dict[normal_pinyin].append(each_word)

            if init_pinyin not in init_pinyin_ciyu_dict:
                init_pinyin_ciyu_dict[init_pinyin] = list()
            init_pinyin_ciyu_dict[init_pinyin].append(each_word)

            # 添加phrase
            if each_word not in words_line_dict:
                words_line_dict[each_word] = list()

            words_line_dict[each_word].append(newPhrase)
    print(words_line_dict)

    pass
