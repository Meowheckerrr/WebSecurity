def get_last_filename_from_txt(txt_file_path):
    try:
        # 打开.txt文件
        with open(txt_file_path, 'r') as file:
            # 读取文件内容
            content = file.read()

            # 使用换行符分割内容，得到每一行
            lines = content.split('\n')

            # 去除空白行并获取每一行的最后一个文件名
            last_filenames = [line.split('/')[-1].strip() for line in lines if line.strip()]

            # 如果有文件，则返回最后一个文件名列表
            if last_filenames:
                return last_filenames
            else:
                return ["文件中没有有效的文件名。"]
    except FileNotFoundError:
        return ["文件不存在。"]

# 替换为你的.txt文件路径
txt_file_path = "apiEnodpoint.txt"

# 获取每一行的最后一个文件名
result = get_last_filename_from_txt(txt_file_path)

# 打印结果
for filename in result:
    print(filename)