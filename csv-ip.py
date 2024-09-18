import csv
import sys

# 定义输入和输出文件的路径
input_file = sys.argv[1]
output_file = sys.argv[2]

# 打开 CSV 文件进行读取
with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # 跳过表头
    next(csvreader)
    
    # 打开输出文件进行写入
    with open(output_file, 'w', newline='', encoding='utf-8') as txtfile:
        for row in csvreader:
            ip = row[0]
            port = row[1]
            # 格式化为 "IP:端口" 并写入到输出文件中
            txtfile.write(f'{ip}:{port}\n')

print(f'数据已提取并保存到 {output_file}')




