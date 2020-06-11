## DemoAPI
```
本文总结介绍接口测试框架开发,web测试开发，环境使用python3+selenium3+unittest测试框架及ddt数据驱动，采用Excel管理测试用例等集成测试数据功能，以及使用HTMLTestRunner来生成测试报告，目前有开源的poman、Jmeter等接口测试工具，为什么还要开发接口测试框架呢？因接口测试工具也有存在几点不足。
* 测试数据不可控制。比如接口返回数据不可控，就无法自动断言接口返回的数据，不能断定是接口程序引起，还是测试数据变化引起的错误，所以需要做一些初始化测试数据。接口工具没有具备初始化测试数据功能，无法做到真正的接口测试自动化。
* 无法测试加密接口。实际项目中，多数接口不是可以随便调用，一般情况无法摸拟和生成加密算法。如时间戳和MDB加密算法，一般接口工具无法摸拟。
* 扩展能力不足。开源的接口测试工具无法实现扩展功能。比如，我们想生成不同格式的测试报告，想将测试报告发送到指定邮箱，又想让接口测试集成到CI中，做持续集成定时任务。
```
## 测试框架处理流程
```
api测试框架处理过程如下：
* 首先初始化清空数据库表的数据，向数据库插入测试数据；（非必要）
* 调用被测试系统提供的接口，先数据驱动读取excel用例一行数据；
* 发送请求数据，根据传参数据，向数据库查询得到对应的数据；（非必要）
* 将查询的结果组装成JSON格式的数据，同时根据返回的数据值与Excel的值对比判断，并写入结果至指定Excel测试用例表格；
* 通过单元测试框架断言接口返回的数据，并生成测试报告，最后把生成最新的测试报告HTML文件发送指定的邮箱。

web测试框架处理过程如下：
* 调用测试实例
* 测试实例调用公共函数登陆网站，测试各项指标，判断指标点击结果
* 通过单元测试框架断言接口返回的数据，并生成测试报告，最后把生成最新的测试报告HTML文件发送指定的邮箱。
```
## 测试框架结构目录介绍
```
目录结构介绍如下：
* PathConfig/:                 文件路径配置
* image                     截图文件
* config/:                 测试用例模板文件及数据库和发送邮箱配置文件
* db_fixture/:             初始化接口测试数据
* lib/:                    程序核心模块。包含有excel解析读写、发送邮箱、发送请求、生成最新测试报告文件
* package/:                存放第三方库包。如HTMLTestRunner，用于生成HTML格式测试报告
* report/:                 生成接口自动化测试报告
* test_case/:               用于编写接口自动化测试用例
    * all_sta：该目录测试用例文件。根据测试文件匹配规则，以“_sta.py”命名的文件被当作自动化web测试用例执行,以“*API.py”命名的文件被当作自动化web测试用例执行。
    * models：该目录下存放了一些公共的配置函数及公共类。
    * page_obj：该目录用于存放测试用例的页面对象（Page Object）。根据自定义规则，以“*Page.py”命名的文件为封装的页面对象文件。
    
* run_demo.py：             执行所有接口测试用例的主程序
* requirements.txt：          依赖包
* test_api.py：               flask实例
```
# ubuntu安装环境

## 1.导入依赖包
```
pip3 install -r filename.txt
```
## 2.下载并安装最新的Google Chrome版本
```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i --force-depends google-chrome-stable_current_amd64.deb
```
## 3.下载并安装最新的amd64 chromedriver版本
```

LATEST=$(wget -q -O - http://chromedriver.storage.googleapis.com/LATEST_RELEASE)
wget http://chromedriver.storage.googleapis.com/$LATEST/chromedriver_linux64.zip

unzip chromedriver_linux64.zip

chmod +x chromedriver

mv chromedriver /usr/bin/
```
## 4.安装依赖
```
pip3 install selenium
apt-get install libnss3
若libnss3安装失败则
添加新源
deb http://security.ubuntu.com/ubuntu precise-security main
apt-get update
apt-get install -f
```
## 5.设置python路径
```
export PYTHONPATH=$PYTHONPATH:/root/zabbix_obj/
```
## 6.安装HTMLTestRunnerCN
```
https://github.com/findyou/HTMLTestRunnerCN
将安装HTMLTestRunnerCN拷贝到python site-packages目录
```
# centos安装
```
安装google的epel源

[google]
name=Google-x86_64
baseurl=http://dl.google.com/linux/rpm/stable/x86_64
 
enabled=1
gpgcheck=0
gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub

yum update , 然后yum install google-chrome-stable
chromedriver下载

参照ubuntu安装
```
## 测试结果展示
* HTML报告
![Image](https://github.com/yingoja/DemoAPI/blob/master/share/screeshots/report1.JPG)

