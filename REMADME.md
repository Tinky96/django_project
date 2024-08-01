# 游戏账号交易平台
## 使用 django 框架
### 注册项目
```
python manage.py startprojects projectname
```
### 注册应用
 ```
 python3 manage.py startapp polls
 ```
 ### 项目与应用的区别
 *一个应用可以被多个项目包含* 
 *一个项目可以包含多个应用*
 对于项目来说 一个应用类似于一个单独的功能 

 # 需求分析
 ## 1. 商品
 1.1 所有商品展示
 1.2 单个商品展示

 ## 2. 用户模块
 2.1 用户注册
 2.2 用户登录
 
 ## 3. 购物车模块
 3.1 显示购物车内所有商品
 3.2 加入购物车
 3.3 删除购物车

 ## 4.订单模块
 4.1 将结算商品展示到订单页面
 4.2 支付订单

 # 数据库设计
 ## 用户  
 ### 用户表 (User)
- 用户ID（UserID）：主键，唯一标识用户  
- 用户名（Username）：唯一，用于登录  
- 密码（Password）：存储加密后的密码  
- 电子邮件（Email）：唯一，用于找回密码  
## 商品
### Product模型具有以下字段：
- product_id（IntegerField，主键）：表示每个商品的唯一标识符。
- product_name（CharField）：存储商品的名称。
- product_description（TextField）：存储商品的描述。
- product_price（DecimalField）：存储商品的价格。
- product_number（CharField）：账号。
- product_key（CharField）：密码。
- User_id（AutoField，User模型）：表示该商品的售卖人
- category_id()
- created_at（DateTimeField，auto_now_add）：存储商品的创建时间。
### Category模型具有以下字段：
- category_id（IntegerField，主键）：表示每个分类的唯一标识符。
- category_name（CharField）：存储分类的名称。
- created_at（DateTimeField，auto_now_add）：存储分类的创建时间。
### ProductImage模型具有以下字段：
- image_id（AutoField，主键）：表示每个图片的唯一标识符。
- product（ForeignKey，关联Product模型）：表示与图片相关联的商品。
- image_path（CharField）：存储图片的路径。
-created_at（DateTimeField，auto_now_add）：存储图片的创建时间

## 订单表（Orders）：
- 订单ID（OrderID）：主键，唯一标识订单
- 游戏账号ID（AccountID）：外键，关联到游戏账号表的账号ID
- 买家ID（BuyerID）：外键，关联到用户表的用户ID，表示购买者
- 卖家ID（SellerID）：外键，关联到用户表的用户ID，表示出售者
- 交易金额（Amount）：表示交易金额
- 创建时间（CreatedTime）：表示订单创建的时间
- 状态（Status）：表示订单的状态，如待支付、已支付、已完成、已取消等

# 页面设计
## 商品
### 商品列表(index)
- 搜索
- 跳转  
- 显示商品列表
    - 商品详情
    - 注册
    - 用户主页

### 商品详情(goods)
- 显示商品详情(价格,图片,介绍)
- 跳转购买页面

### 购买页面
- 选择支付方式
- 支付

## 用户 
### 用户主页
- 显示用户信息
- 查看参与订单
- 查看订单详情
- 修改用户信息

### 注册

### 登录

### 上传商品


## 订单
### 订单列表页面



### 订单详情页面


# Vue项目文件详解
.
├── README.md   -- 描述文件
├── babel.config.js  -- 使用一些预设
├── jsconfig.json -- 
├── node_modules  -- 当前项目所有依赖的包
├── package-lock.json -- 版本管理使用的组件
├── package.json  -- 项目描述
├── public  -- 公共资源
├── src  -- 源码目录
└── vue.config.js  -- 