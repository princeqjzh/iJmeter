# 压力测试项目，练习用
包含： JMeter压测脚本，模拟被测试的接口应用，自动化压测样例代码

1. jmeter演示知识点:
- Get请求编写
- Get请求的传参
- 获取返回值
- Post请求编写
- Post请求传参数
- 获取返回值
- JSON解析
- 正则匹配
- 动态参数传递
- 公共参数配置
- CSV导入参数配置

2. 模拟接口服务的启动方法
路径：iJmeter/application
python3 ${path}/orderservice.py

3. 自动化压测
- 代码位置： automation/auto_stress_test.sh
- 运行之前需要在本机配置环境变量 jmeter_path，将其指向jmeter安装的根目录
    export jmeter_path=/jmeter_root_path/
- 自动化压测会在运行时依次、自动执行并发压测，并发数 10 20 30 40 50， 每组压测60秒
- 运行代码的时候请先确保当前路径处于automation目录下，然后运行 ./auto_stress_test.sh
