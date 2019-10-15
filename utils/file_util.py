class FileUtil:

    @classmethod
    def get_file(cls, path):
        """
        获取文件内容，返回 line 列表
        :param path:
        :return:
        """
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return [each.strip() for each in lines]
