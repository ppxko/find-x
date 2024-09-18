import json
import sys

class Record:
    def __init__(self, url, port, title, ip):
        self.url = url
        self.port = port
        self.title = title
        self.ip = ip

def main():
    if len(sys.argv) < 2:
        print("请提供文件名，例如: python yourscript.py other.txt other.txt")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, 'r', encoding='utf-8') as file, open(output_file, 'w', encoding='utf-8') as out_file:
            for line in file:
                # 将单引号替换为双引号
                corrected_line = line.replace("'", '"')

                try:
                    # 解析JSON数据
                    record_data = json.loads(corrected_line)
                    record = Record(**record_data)

                    # 格式化IP和端口为"ip port"
                    output = f"{record.ip} {record.port}\n"

                    # 写入输出文件
                    out_file.write(output)
                except json.JSONDecodeError as e:
                    print(f"解析JSON出错: {e}")
                    continue

    except FileNotFoundError as e:
        print(f"无法打开文件 {input_file}: {e}")
    except IOError as e:
        print(f"文件读写出错: {e}")

if __name__ == "__main__":
    main()




