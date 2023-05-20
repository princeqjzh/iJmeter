#!/usr/bin/env bash

# 压测脚本中设定的压测时间应为20秒
export jmx_filename="order_auto.jmx"

# 需要在系统变量中定义jmeter根目录的位置，如下
# export jmeter_path="/your jmeter path/"

echo "自动化压测开始"

rm -rf webreport
mkdir -p webreport
echo "" > webreport/index.html


# 压测并发数列表
thread_number_array=($thread_number_list)
for num in "${thread_number_array[@]}"
do
    echo "压测并发数 ${num}"
    # 定义jtl结果文件名与压测报告路径
    export jtl_filename="test_${num}.jtl"
    export web_report_path_name="web_${num}"

    rm -f ${jtl_filename}
    rm -rf ${web_report_path_name}

    # JMeter 静默压测 + 生成html压测报告
    ${jmeter_path}/bin/jmeter -n -t ${jmx_filename} -l ${jtl_filename}  -Jthread=${num} -e -o ${web_report_path_name}
    echo "结束压测并发数 ${num}"
    echo "<a href='${web_report_path_name}'>${web_report_path_name}</a><br><br>" >> webreport/index.html
done
echo "自动化压测全部结束"

