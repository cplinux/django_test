## 用途

该Django项目是用于构建Django的docker镜像的测试中使用的demo项目，可用于测试web访问和mysql链接。





## 结构

该项目是通过uwsgi当作http服务器，来启动Django项目。

```bash
├── Dockerfile	# 构建docker镜像
├── README.md
├── manage.py
├── myweb
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── people
│   ├── __init__.py
│   ├── admin.py   # admin页面
│   ├── apps.py
│   ├── models.py  # 数据库模型
│   ├── tests.py
│   └── views.py
├── requirements.txt  # 软件包依赖
├── setup.py  # 项目打包
├── start.sh  # 项目启动
└── uwsgi.ini	# uwsgi配置文件
```


