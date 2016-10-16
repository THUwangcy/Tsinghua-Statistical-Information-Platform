### 问卷保存和发布api     
   o	发GET请求（design.ajax中的script）
        •	参数列表：
            	act_id：int类型，表示要操作的问卷id
    o	分别连接到api的save_act(request)和publish_act(request)函数
        •	需要返回JSON：
            	status：string类型，需要为“ok”   
            
### 单选题编辑api
    o	发POST请求（single_modal中的script）：
        •	使用handleFormPost，form字典格式：
            	status：目前未定义
            	qst_type：string类型，当前问题的类型（即single）
            	questions_id：int类型，当前问题id
            	option_num：int类型，选项个数
            	csrfmiddlewaretoken：没用
            	qst_title：string类型，问题的题面描述
            	option[x]_field：string类型，表示第x个选项的文本内容，其中[x]为可变数字，取值从1到option_num，比如“option1_field“，表示第一个选项内容
    o	连接到api的modify_qst（request）函数
        •	其中的dict表示上述字典
        •	需要返回JSON：
            	status：string类型，表示状态，需要是“ok”
            
### api有疑问   
    后端测试中对api传入的数据有疑问都可以在网页上进行相应的操作，之后查看interface文件夹中的static_database.txt，就可以看到具体输出实例



### 项目目录：       
    - .git ...............git管理目录       
    - .idea ..............使用PyCharm自动生成的目录，不用管       
    - doc ................之后要写的各种文档，现在为空       
    - src ................Django代码文件夹，即Django创建工程时最顶层的文件夹     
        - api ............本质上是一个app，用来暴露后端的接口，所有调用后端的接口在这里新建python文件呈现      
        - dance ..........django的工程名（最顶层文件夹不是dance而是src是因为我把它改了，更清晰一些），里面的settings.py用来设置，这里已添加创建的三个app     
        - database .......数据库app，所有后端的数据库相关操作在这里新建python文件实现       
        - interface ......用户界面app，其中存放所有html、js、css文件，里面的view.py用来渲染网页模板来动态显示呈现给用户的界面      
        da.sqlite3 .......自带的数据库文件，不用的话可以不管      
        manage.py ........工程管理文件，运行服务器用这个      
    - imgs ...............之后可能要用到的图片资源      
    README.md

### 管理页面：
    username: admin
    password: whynotdance     
    
### 注意：     
    pull下来后先运行python manage.py migrate