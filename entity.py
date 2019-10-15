class Ciyu:
    """
    汉字基本类
    """

    def __init__(self, _quanpin, _hanzi, _shouxie):
        self.quanpin = _quanpin
        self.hanzi = _hanzi
        self.shouxie = _shouxie


class Phrase:
    def __init__(self, _line):
        self.line = _line


if __name__ == '__main__':
    new_ciyu = Ciyu("zhongguo", "中国", "zg")
    print(new_ciyu.quanpin)
