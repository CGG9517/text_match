import jieba


class WordHelper(object):

    @classmethod
    def seg(cls, line):
        # todo 分词方法
        return jieba.cut_for_search(line)
