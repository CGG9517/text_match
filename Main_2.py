# this is the Main file
from utils.file_util import FileUtil
from utils.wordhelper import WordHelper
from utils.pinyin_util import *
from entity import *


def append_new_val_in_dict(_dict, _key, _new_val):
    if _key not in _dict:
        _dict[_key] = list()
    _dict[_key].append(_new_val)
    return


def get_word_2_pinyin_dict():
    path = 'testLines.txt'
    lines = FileUtil.get_file(path)
    # words_line_dict = dict()  # 用于存放词与短语对象的对应关系
    _normal_pinyin_phrase_dict = dict()  # 用于存放全拼拼音与短语对象的对应关系
    _first_pinyin_phrase_dict = dict()  # 用于存放首写拼音与短语对象的对应关系
    _init_pinyin_phrase_dict = dict()  # 用于存放声母与短语对象的对应关系
    words = []  # 用于存放一行短语的分词结果
    for each_line in lines:
        _full_pinyin = ''.join(PinyinUtil.get_lazy_pinyin(each_line))
        _init_pinyin = ''.join(PinyinUtil.get_init_pinyin(each_line))
        _first_pin = ''.join(PinyinUtil.get_first_pinyin(each_line))
        newPhrase = Phrase(each_line, _full_pinyin)

        append_new_val_in_dict(_normal_pinyin_phrase_dict, _full_pinyin, newPhrase)
        append_new_val_in_dict(_first_pinyin_phrase_dict, _first_pin, newPhrase)
        append_new_val_in_dict(_init_pinyin_phrase_dict, _init_pinyin, newPhrase)
    return _normal_pinyin_phrase_dict, _first_pinyin_phrase_dict, _init_pinyin_phrase_dict


def match_and_put(_str, _dict, _target_list):
    for each in _dict.keys():
        if _str in each:
            _target_list.extend([item.line for item in _dict[each]])


if __name__ == '__main__':
    while (1==1):
        in_str = input("请输入拼音：")
        result = []
        for each_dict in get_word_2_pinyin_dict():
            match_and_put(in_str, each_dict, result)

        print(result)
