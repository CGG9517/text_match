class Ciyu:
    """
    汉字基本类
    """

    def __init__(self, _hanzi, _quanpin, _shouxie):
        self.quanpin = _quanpin
        self.hanzi = _hanzi
        self.shouxie = _shouxie

    def __eq__(self, o: object) -> bool:
        if isinstance(o, self.__class__):
            return hash(self) == hash(o)
        else:
            return False

    def __hash__(self) -> int:
        return hash(self.hanzi)


class Phrase:
    def __init__(self, _line):
        self.line = _line


if __name__ == '__main__':
    new_ciyu = Ciyu("zhongguo", "中国", "zg")
    print(new_ciyu.quanpin)
