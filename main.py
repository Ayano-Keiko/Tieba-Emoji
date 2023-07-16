import os

from getEmotion import TiebaEmotion

save_dir = './emotion/'  # 保存路径

if __name__ == "__main__":
    # 判断保存路径是否已经创建
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    
    tb = TiebaEmotion()
    tb.tenth(save_dir)