import inspect
import os

from getEmotion import TiebaEmotion

save_dir = './emotion/'  # 保存路径

if __name__ == "__main__":
    # 判断保存路径是否已经创建
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    tb = TiebaEmotion()
    # get all information(method name, variable name) of a class
    all_members = inspect.getmembers(tb)
    # select all the instance methods
    instance_method = [
        name for name, member in all_members
        if inspect.ismethod(member) and not name.startswith('__')
    ]
    # recursively call all instance methods of the class
    for mathod_name in instance_method:
        method = getattr(tb, mathod_name)
        method(save_dir)