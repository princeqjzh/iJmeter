#!/usr/bin/env bash

# 压测脚本模板中设定的压测时间应为60秒
export jmx_template="PreClassMenu_auto"
export suffix=".jmx"
export jmx_template_filename="${jmx_template}${suffix}"
export os_type=`uname`

# 需要在系统变量中定义jmeter根目录的位置，如下
# export jmeter_path="/your jmeter path/"

# 清空nohup.out
cat /dev/null > nohup.out

# 强制杀掉JMeter进程
killJMeter()
{
    pid=`ps -ef|grep jmeter|grep java|grep ${jmx_filename}|awk '{print $2}'`
    echo "jmeter Id list :$pid"
    if [[ "$pid" = "" ]]
    then
      echo "no jmeter pid alive"
    else
      kill -9 $pid
    fi
}

# 压测并发数列表
thread_number_array=(2)
for num in "${thread_number_array[@]}"
do
    # 生成对应压测线程的jmx文件
    export jmx_filename="${jmx_template}_${num}${suffix}"
    export jtl_filename="test_${num}.jtl"
    export web_report_path_name="web_${num}"

    rm -f ${jmx_filename} ${jtl_filename}
    rm -rf ${web_report_path_name}

    cp ${jmx_template_filename} ${jmx_filename}
    echo "生成jmx压测脚本 ${jmx_filename}"

    if [[ "${os_type}" == "Darwin" ]]; then
        sed -i "" "s/thread_num/${num}/g" ${jmx_filename}
    else
        sed -i "s/thread_num/${num}/g" ${jmx_filename}
    fi

    # JMeter 静默压测
    nohup ${jmeter_path}/bin/jmeter -n -t ${jmx_filename} -l ${jtl_filename} -e -o ${web_report_path_name} &
    sleep 80
    killJMeter
    rm -f ${jmx_filename}
done
echo "自动化压测全部结束"

