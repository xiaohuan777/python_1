## Jmeter+Ant+Jenkins接口自动化测试平台

### jenkins是什么？

Jenkins是一个开源的、提供友好操作界面的持续集成(CI)工具。主要用于持续、自动的构建/测试软件项目、监控外部任务的运行。通常与版本管理工具(SCM)、构建工具结合使用。常用的版本控制工具有SVN、GIT，构建工具有Maven、Ant、Gradle。


### 环境依赖
JDK环境配置
Jmeter安装
Ant安装环境变量配置
Jenkins安装


### Jenkins安装
下载地址：https://jenkins.io/download/

下载后安装到指定的路径即可，默认启动页面为localhots:8080,如果8080端口被占用无法打开，可以进入到jenkins安装目录，找到jenkins.xml配置文件打开，修改如下代码的端口号即可。

``` 
<arguments>-Xrs -Xmx256m -Dhudson.lifecycle=hudson.lifecycle.WindowsServiceLifecycle -jar "%BASE%\jenkins.war" --httpPort=8080 --webroot="%BASE%\war"</arguments>
```

mac环境下，需要执行 `java -jar jenkins.war` 来启动Jenkins服务。
具体安装方法参考 https://www.jianshu.com/p/8eee4b73db24


![图片名字]（图片url）


### 平台搭建
#### 依赖文件配置
* 首先在Jmeter目录下面新建一个文件夹 loadTest (文件夹名称不要使用下划线，空格字符),并将Jemter测试脚本放置到该文件夹中。
* 将Jmeter extras 文件中的 ant-jmeter-1.1.1.jar 放到Ant中的 lib文件夹中
* 将Jmeter extras 文件中的 jmeter-results-detail-report_21.xsl ,build.xml、collapse.png、expand.png 放到 ant目录中的 bin目录下面。

#### build.xml配置
在Ant的bin目录中打开build.xml文件找到以下内容
```
<property name="testpath" value="${user.dir}"/>
<property name="jmeter.home" value="${basedir}/.."/>
<property name="report.title" value="Load Test Results"/>

<!-- Name of test (without .jmx) -->
<property name="test" value="Test"/>
```

#### 参数说明

* testpath 测试计划，这里用于存放测试脚本、测试生成的文件、测试报告
* jmeter.home Jmeter目录路径
* report.title 测试报告的标题
* test jmeter测试脚本的名称（无需后缀.jmx）
  
这里根据自己的环境修改为
```
<property name="testpath" value="C:\apache-jmeter-4.0\loadTest"/>
<property name="jmeter.home" value="C:\apache-jmeter-4.0"/>
<property name="report.title" value="Httpbin API Test Report"/>

<!-- Name of test (without .jmx) -->
<property name="test" value="httpbin_test"/>
```

#### Ant构建
执行如下命令进行构建
`ant -buildfile C:\apache-ant-1.10.5\bin\build.xml`

结果如下

![图片名字]（图片url）

进入到loadTest文件夹可以看到生成如下文件：

![图片名字]（图片url）

打开html测试报告httpbin_test.html 报告内容如下：

![图片名字]（图片url）


### 集成到Jenkins

在Jenkins新建一个任务LoadTest

在构建选项中选择Invoke Ant 然后在Build File输入build.xml配置文件路径。需要点击高级选项后才可以显示Build File

![图片名字]（图片url）

执行之后可以看到控制台输出和teminal的控制台输出是一样的

![图片名字]（图片url）

如果想定制构建则可以在构建触发器中选择Build periodically 如果想每个工作日下班18时执行，则可以如下设置：

![图片名字]（图片url）

### 邮件推送

#### 安装插件
1. 系统设置->管理插件->可选插件，搜索Performance plugin(Jmeter报告需要)，安装此插件
   
![图片名字]（图片url）

2. 因为需要用到ANT和JDK，所以需要在jenkins中添加插件，选择点击“系统管理”，之后在Global Tool Configuration的界面看到ant和jdk选项，然后将自己本地的ANT和JDK地址填写上
   
![图片名字]（图片url）

3. 进入“系统管理”>>>“插件管理”安装邮件通知插件Email Ext Recipients Column Plugin，Email Extension Plugin
![图片名字]（图片url）


#### 配置、测试邮件

1. 进入“系统设置”
![图片名字]（图片url）

2. 设置Jenkins地址和管理员邮箱（不设置管理员邮箱无法发送邮件）
![图片名字]（图片url）

3. 配置系统管理员的邮件属性，点击“高级”
![图片名字]（图片url）

4. 找到SMTP服务器地址和端口号及设置163邮箱的POP3/SMTP服务
![图片名字]（图片url）


5. 配置系统管理员的邮件属性
![图片名字]（图片url）

6. 配置“邮件通知”，点击“高级”
![图片名字]（图片url）

7. 然后进入到具体的某一job中配置邮件通知
8. 点击“add trigger”
9. 添加附件
10. 将构建日志压缩作为附件也添加到邮件当中发送，需要注意的是，每一次构建都会产生一个报告文档，仓库里会包含有之前构建的所有的报告文档，所以需要打包的是当前这次产生的报告文档，不是之前的构建产生的文档
11. 点击应用“apply”，然后保存
12. 测试能否收到了邮件，点击“立即构建”  
13. 邮件测试结果(收到邮件)