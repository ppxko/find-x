#!/bin/bash

# 定义输入和输出文件
input_file="ip.txt"
output_file="realip.txt"

# 清空输出文件
> $output_file

# 读取ip.txt中的每一行
while IFS=: read -r ip port; do
    # 使用curl进行测试
    result=$(curl -A "trace" --ssl-no-revoke --resolve cf-ns.com:$port:$ip https://cf-ns.com:$port/cdn-cgi/trace -s --connect-timeout 2 --max-time 10 | grep "uag")

    # 检查是否返回 uag=trace
    if [[ $result == *"uag=trace"* ]]; then
        echo "$ip:$port" >> $output_file
        echo "Success: $ip:$port"
    fi
done < "$input_file"
