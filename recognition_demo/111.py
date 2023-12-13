import os

# 设置要清理的文件夹路径
folder_path = 'save'

# 遍历文件夹中的所有文件和子文件夹
for root, dirs, files in os.walk(folder_path):
    for filename in files:
        # 删除文件
        os.remove(os.path.join(root, filename))
   
