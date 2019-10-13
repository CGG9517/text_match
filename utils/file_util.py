
class FileUtil:

    @classmethod
    def get_file(cls, path):
        """
        获取文件内容，返回 line 列表
        :param path:
        :return:
        """
        with open(path, 'r') as f:
            lines = f.readlines()
            return lines;