
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