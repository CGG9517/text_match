from pypinyin import pinyin, lazy_pinyin, Style
class PinyinUtil:

    @classmethod
    def get_lazy_pinyin(cls, chin_words):
        """
        返回汉语词组的拼音
        :param chin_words: 汉语词组
        :return: 如：'中心' 返回 ['zhong', 'xin']
        """
        return lazy_pinyin(chin_words)

    @classmethod
    def get_first_pinyin(cls, chin_words):
        """
        返回词组的首写字母
        :param chin_words: 汉语词组
        :return:
        """
        return lazy_pinyin(chin_words, style=Style.FIRST_LETTER, strict=False)


if __name__ == '__main__':
    lazy_pinyin_ = PinyinUtil.get_lazy_pinyin("还钱")
    print(lazy_pinyin_)
    print(PinyinUtil.get_first_pinyin("还不够"))