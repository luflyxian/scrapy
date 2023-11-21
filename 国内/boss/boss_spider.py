# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import os.path

import pymysql
import time
import datetime
import hashlib
import re
import redis
import random
import execjs
import requests
import threadpool
# import requests
from urllib.parse import unquote, quote
from requests import Session
from urllib3 import disable_warnings
# from bs4 import BeautifulSoup
from queue import Queue
import threading
import json
import math
from pprint import pprint
from threading import Lock

lock = Lock()
Industry_dict = [{'url': '100108', 'firstJobType': '技术', 'secondJobType': '后端开发', 'thirdJobType': 'Hadoop'},
                 {'url': '100119', 'firstJobType': '技术', 'secondJobType': '后端开发', 'thirdJobType': 'Erlang'},
                 {'url': '100123', 'firstJobType': '技术', 'secondJobType': '后端开发', 'thirdJobType': '全栈工程师'},
                 {'url': '100122', 'firstJobType': '技术', 'secondJobType': '后端开发', 'thirdJobType': '数据采集'},
                 {'url': '100116', 'firstJobType': '技术', 'secondJobType': '后端开发', 'thirdJobType': 'Golang'},
                 {'url': '100113', 'firstJobType': '技术', 'secondJobType': '后端开发', 'thirdJobType': 'Ruby'},
                 {'url': '100124', 'firstJobType': '技术', 'secondJobType': '后端开发', 'thirdJobType': 'GIS工程师'},
                 {'url': '100103', 'firstJobType': '技术', 'secondJobType': '后端开发', 'thirdJobType': 'PHP'},
                 {'url': '100106', 'firstJobType': '技术', 'secondJobType': '后端开发', 'thirdJobType': 'C#'},
                 {'url': '100110', 'firstJobType': '技术', 'secondJobType': '后端开发', 'thirdJobType': 'Delphi'},
                 {'url': '100101', 'firstJobType': '技术', 'secondJobType': '后端开发', 'thirdJobType': 'Java'},
                 {'url': '100105', 'firstJobType': '技术', 'secondJobType': '后端开发', 'thirdJobType': 'C'},
                 {'url': '100199', 'firstJobType': '技术', 'secondJobType': '后端开发', 'thirdJobType': '后端开发'},
                 {'url': '100114', 'firstJobType': '技术', 'secondJobType': '后端开发', 'thirdJobType': 'Node.js'},
                 {'url': '100112', 'firstJobType': '技术', 'secondJobType': '后端开发', 'thirdJobType': 'Perl'},
                 {'url': '100107', 'firstJobType': '技术', 'secondJobType': '后端开发', 'thirdJobType': '.NET'},
                 {'url': '100102', 'firstJobType': '技术', 'secondJobType': '后端开发', 'thirdJobType': 'C++'},
                 {'url': '100111', 'firstJobType': '技术', 'secondJobType': '后端开发', 'thirdJobType': 'VB'},
                 {'url': '100121', 'firstJobType': '技术', 'secondJobType': '后端开发',
                  'thirdJobType': '语音/视频/图形开发'},
                 {'url': '100109', 'firstJobType': '技术', 'secondJobType': '后端开发', 'thirdJobType': 'Python'},
                 {'url': '100202', 'firstJobType': '技术', 'secondJobType': '移动开发', 'thirdJobType': 'Android'},
                 {'url': '100205', 'firstJobType': '技术', 'secondJobType': '移动开发', 'thirdJobType': '移动web前端'},
                 {'url': '100201', 'firstJobType': '技术', 'secondJobType': '移动开发', 'thirdJobType': 'HTML5'},
                 {'url': '100208', 'firstJobType': '技术', 'secondJobType': '移动开发', 'thirdJobType': 'JavaScript'},
                 {'url': '100203', 'firstJobType': '技术', 'secondJobType': '移动开发', 'thirdJobType': 'iOS'},
                 {'url': '100299', 'firstJobType': '技术', 'secondJobType': '移动开发', 'thirdJobType': '移动开发'},
                 {'url': '100211', 'firstJobType': '技术', 'secondJobType': '移动开发', 'thirdJobType': 'UE4'},
                 {'url': '100210', 'firstJobType': '技术', 'secondJobType': '移动开发', 'thirdJobType': 'COCOS2DX'},
                 {'url': '100209', 'firstJobType': '技术', 'secondJobType': '移动开发', 'thirdJobType': 'U3D'},
                 {'url': '100206', 'firstJobType': '技术', 'secondJobType': '移动开发', 'thirdJobType': 'Flash开发'},
                 {'url': '100309', 'firstJobType': '技术', 'secondJobType': '测试', 'thirdJobType': '软件测试'},
                 {'url': '100310', 'firstJobType': '技术', 'secondJobType': '测试', 'thirdJobType': '渗透测试'},
                 {'url': '100307', 'firstJobType': '技术', 'secondJobType': '测试', 'thirdJobType': '游戏测试'},
                 {'url': '100302', 'firstJobType': '技术', 'secondJobType': '测试', 'thirdJobType': '自动化测试'},
                 {'url': '100304', 'firstJobType': '技术', 'secondJobType': '测试', 'thirdJobType': '性能测试'},
                 {'url': '100305', 'firstJobType': '技术', 'secondJobType': '测试', 'thirdJobType': '测试开发'},
                 {'url': '100308', 'firstJobType': '技术', 'secondJobType': '测试', 'thirdJobType': '硬件测试'},
                 {'url': '100301', 'firstJobType': '技术', 'secondJobType': '测试', 'thirdJobType': '测试工程师'},
                 {'url': '100306', 'firstJobType': '技术', 'secondJobType': '测试', 'thirdJobType': '移动端测试'},
                 {'url': '100303', 'firstJobType': '技术', 'secondJobType': '测试', 'thirdJobType': '功能测试'},
                 {'url': '100401', 'firstJobType': '技术', 'secondJobType': '运维/技术支持',
                  'thirdJobType': '运维工程师'},
                 {'url': '100408', 'firstJobType': '技术', 'secondJobType': '运维/技术支持',
                  'thirdJobType': '系统安全'},
                 {'url': '100402', 'firstJobType': '技术', 'secondJobType': '运维/技术支持',
                  'thirdJobType': '运维开发工程师'},
                 {'url': '100405', 'firstJobType': '技术', 'secondJobType': '运维/技术支持',
                  'thirdJobType': 'IT技术支持'},
                 {'url': '100409', 'firstJobType': '技术', 'secondJobType': '运维/技术支持', 'thirdJobType': 'DBA'},
                 {'url': '100407', 'firstJobType': '技术', 'secondJobType': '运维/技术支持',
                  'thirdJobType': '网络安全'},
                 {'url': '100404', 'firstJobType': '技术', 'secondJobType': '运维/技术支持',
                  'thirdJobType': '系统工程师'},
                 {'url': '100406', 'firstJobType': '技术', 'secondJobType': '运维/技术支持',
                  'thirdJobType': '系统管理员'},
                 {'url': '100403', 'firstJobType': '技术', 'secondJobType': '运维/技术支持',
                  'thirdJobType': '网络工程师'},
                 {'url': '100511', 'firstJobType': '技术', 'secondJobType': '数据', 'thirdJobType': '数据分析师'},
                 {'url': '100599', 'firstJobType': '技术', 'secondJobType': '数据', 'thirdJobType': '数据'},
                 {'url': '100506', 'firstJobType': '技术', 'secondJobType': '数据', 'thirdJobType': 'ETL工程师'},
                 {'url': '100507', 'firstJobType': '技术', 'secondJobType': '数据', 'thirdJobType': '数据仓库'},
                 {'url': '100509', 'firstJobType': '技术', 'secondJobType': '数据', 'thirdJobType': '数据挖掘'},
                 {'url': '100512', 'firstJobType': '技术', 'secondJobType': '数据', 'thirdJobType': '数据架构师'},
                 {'url': '100508', 'firstJobType': '技术', 'secondJobType': '数据', 'thirdJobType': '数据开发'},
                 {'url': '100817', 'firstJobType': '技术', 'secondJobType': '项目管理', 'thirdJobType': '硬件项目经理'},
                 {'url': '100601', 'firstJobType': '技术', 'secondJobType': '项目管理', 'thirdJobType': '项目经理'},
                 {'url': '100605', 'firstJobType': '技术', 'secondJobType': '项目管理', 'thirdJobType': '实施顾问'},
                 {'url': '100604', 'firstJobType': '技术', 'secondJobType': '项目管理', 'thirdJobType': '项目专员'},
                 {'url': '100606', 'firstJobType': '技术', 'secondJobType': '项目管理', 'thirdJobType': '实施工程师'},
                 {'url': '100602', 'firstJobType': '技术', 'secondJobType': '项目管理', 'thirdJobType': '项目主管'},
                 {'url': '100607', 'firstJobType': '技术', 'secondJobType': '项目管理',
                  'thirdJobType': '需求分析工程师'},
                 {'url': '100603', 'firstJobType': '技术', 'secondJobType': '项目管理', 'thirdJobType': '项目助理'},
                 {'url': '100810', 'firstJobType': '技术', 'secondJobType': '硬件开发', 'thirdJobType': 'ARM开发'},
                 {'url': '100805', 'firstJobType': '技术', 'secondJobType': '硬件开发', 'thirdJobType': '电路设计'},
                 {'url': '100804', 'firstJobType': '技术', 'secondJobType': '硬件开发', 'thirdJobType': '单片机'},
                 {'url': '100806', 'firstJobType': '技术', 'secondJobType': '硬件开发', 'thirdJobType': '驱动开发'},
                 {'url': '100802', 'firstJobType': '技术', 'secondJobType': '硬件开发', 'thirdJobType': '嵌入式'},
                 {'url': '100816', 'firstJobType': '技术', 'secondJobType': '硬件开发', 'thirdJobType': '射频工程师'},
                 {'url': '100801', 'firstJobType': '技术', 'secondJobType': '硬件开发', 'thirdJobType': '硬件工程师'},
                 {'url': '100803', 'firstJobType': '技术', 'secondJobType': '硬件开发', 'thirdJobType': '自动化'},
                 {'url': '100811', 'firstJobType': '技术', 'secondJobType': '硬件开发', 'thirdJobType': 'PCB工艺'},
                 {'url': '100809', 'firstJobType': '技术', 'secondJobType': '硬件开发', 'thirdJobType': 'DSP开发'},
                 {'url': '100808', 'firstJobType': '技术', 'secondJobType': '硬件开发', 'thirdJobType': 'FPGA开发'},
                 {'url': '100807', 'firstJobType': '技术', 'secondJobType': '硬件开发', 'thirdJobType': '系统集成'},
                 {'url': '100999', 'firstJobType': '技术', 'secondJobType': '前端开发', 'thirdJobType': '前端开发'},
                 {'url': '100901', 'firstJobType': '技术', 'secondJobType': '前端开发', 'thirdJobType': 'web前端'},
                 {'url': '100904', 'firstJobType': '技术', 'secondJobType': '前端开发', 'thirdJobType': 'HTML5'},
                 {'url': '100902', 'firstJobType': '技术', 'secondJobType': '前端开发', 'thirdJobType': 'JavaScript'},
                 {'url': '100903', 'firstJobType': '技术', 'secondJobType': '前端开发', 'thirdJobType': 'Flash开发'},
                 {'url': '101004', 'firstJobType': '技术', 'secondJobType': '通信', 'thirdJobType': '移动通信工程师'},
                 {'url': '101006', 'firstJobType': '技术', 'secondJobType': '通信', 'thirdJobType': '电信交换工程师'},
                 {'url': '101005', 'firstJobType': '技术', 'secondJobType': '通信', 'thirdJobType': '电信网络工程师'},
                 {'url': '101017', 'firstJobType': '技术', 'secondJobType': '通信', 'thirdJobType': '光传输工程师'},
                 {'url': '101016', 'firstJobType': '技术', 'secondJobType': '通信', 'thirdJobType': '光通信工程师'},
                 {'url': '101008', 'firstJobType': '技术', 'secondJobType': '通信',
                  'thirdJobType': '无线/射频通信工程师'},
                 {'url': '101002', 'firstJobType': '技术', 'secondJobType': '通信', 'thirdJobType': '通信研发工程师'},
                 {'url': '101007', 'firstJobType': '技术', 'secondJobType': '通信', 'thirdJobType': '有线传输工程师'},
                 {'url': '101018', 'firstJobType': '技术', 'secondJobType': '通信', 'thirdJobType': '光网络工程师'},
                 {'url': '101013', 'firstJobType': '技术', 'secondJobType': '通信', 'thirdJobType': '核心网工程师'},
                 {'url': '101012', 'firstJobType': '技术', 'secondJobType': '通信', 'thirdJobType': '通信项目经理'},
                 {'url': '101015', 'firstJobType': '技术', 'secondJobType': '通信', 'thirdJobType': '通信设备工程师'},
                 {'url': '101009', 'firstJobType': '技术', 'secondJobType': '通信', 'thirdJobType': '通信电源工程师'},
                 {'url': '101011', 'firstJobType': '技术', 'secondJobType': '通信', 'thirdJobType': '通信项目专员'},
                 {'url': '101003', 'firstJobType': '技术', 'secondJobType': '通信', 'thirdJobType': '数据通信工程师'},
                 {'url': '101010', 'firstJobType': '技术', 'secondJobType': '通信', 'thirdJobType': '通信标准化工程师'},
                 {'url': '101001', 'firstJobType': '技术', 'secondJobType': '通信', 'thirdJobType': '通信技术工程师'},
                 {'url': '101014', 'firstJobType': '技术', 'secondJobType': '通信', 'thirdJobType': '通信测试工程师'},
                 {'url': '101404', 'firstJobType': '技术', 'secondJobType': '电子/半导体',
                  'thirdJobType': '电气设计工程师'},
                 {'url': '101401', 'firstJobType': '技术', 'secondJobType': '电子/半导体',
                  'thirdJobType': '电子工程师'},
                 {'url': '101403', 'firstJobType': '技术', 'secondJobType': '电子/半导体', 'thirdJobType': 'FAE'},
                 {'url': '101405', 'firstJobType': '技术', 'secondJobType': '电子/半导体',
                  'thirdJobType': '集成电路IC设计'},
                 {'url': '101402', 'firstJobType': '技术', 'secondJobType': '电子/半导体',
                  'thirdJobType': '电气工程师'},
                 {'url': '101406', 'firstJobType': '技术', 'secondJobType': '电子/半导体',
                  'thirdJobType': 'IC验证工程师'},
                 {'url': '100706', 'firstJobType': '技术', 'secondJobType': '高端技术职位', 'thirdJobType': '运维总监'},
                 {'url': '100704', 'firstJobType': '技术', 'secondJobType': '高端技术职位', 'thirdJobType': '架构师'},
                 {'url': '100799', 'firstJobType': '技术', 'secondJobType': '高端技术职位',
                  'thirdJobType': '高端技术职位'},
                 {'url': '100707', 'firstJobType': '技术', 'secondJobType': '高端技术职位',
                  'thirdJobType': '技术合伙人'},
                 {'url': '100702', 'firstJobType': '技术', 'secondJobType': '高端技术职位', 'thirdJobType': '技术总监'},
                 {'url': '100701', 'firstJobType': '技术', 'secondJobType': '高端技术职位', 'thirdJobType': '技术经理'},
                 {'url': '100705', 'firstJobType': '技术', 'secondJobType': '高端技术职位', 'thirdJobType': 'CTO'},
                 {'url': '100703', 'firstJobType': '技术', 'secondJobType': '高端技术职位', 'thirdJobType': '测试经理'},
                 {'url': '100118', 'firstJobType': '技术', 'secondJobType': '人工智能', 'thirdJobType': '推荐算法'},
                 {'url': '100117', 'firstJobType': '技术', 'secondJobType': '人工智能', 'thirdJobType': '自然语言处理'},
                 {'url': '101309', 'firstJobType': '技术', 'secondJobType': '人工智能',
                  'thirdJobType': '反欺诈/风控算法'},
                 {'url': '100104', 'firstJobType': '技术', 'secondJobType': '人工智能', 'thirdJobType': '数据挖掘'},
                 {'url': '101307', 'firstJobType': '技术', 'secondJobType': '人工智能', 'thirdJobType': '算法研究员'},
                 {'url': '101306', 'firstJobType': '技术', 'secondJobType': '人工智能', 'thirdJobType': '图像识别'},
                 {'url': '101302', 'firstJobType': '技术', 'secondJobType': '人工智能', 'thirdJobType': '深度学习'},
                 {'url': '101308', 'firstJobType': '技术', 'secondJobType': '人工智能',
                  'thirdJobType': '智能驾驶系统工程师'},
                 {'url': '101399', 'firstJobType': '技术', 'secondJobType': '人工智能', 'thirdJobType': '人工智能'},
                 {'url': '100115', 'firstJobType': '技术', 'secondJobType': '人工智能', 'thirdJobType': '搜索算法'},
                 {'url': '101301', 'firstJobType': '技术', 'secondJobType': '人工智能', 'thirdJobType': '机器学习'},
                 {'url': '100120', 'firstJobType': '技术', 'secondJobType': '人工智能', 'thirdJobType': '算法工程师'},
                 {'url': '101305', 'firstJobType': '技术', 'secondJobType': '人工智能', 'thirdJobType': '语音识别'},
                 {'url': '101201', 'firstJobType': '技术', 'secondJobType': '销售技术支持',
                  'thirdJobType': '售前技术支持'},
                 {'url': '101202', 'firstJobType': '技术', 'secondJobType': '销售技术支持',
                  'thirdJobType': '售后技术支持'},
                 {'url': '101299', 'firstJobType': '技术', 'secondJobType': '销售技术支持',
                  'thirdJobType': '销售技术支持'},
                 {'url': '101101', 'firstJobType': '技术', 'secondJobType': '其他技术职位',
                  'thirdJobType': '其他技术职位'},
                 {'url': '110102', 'firstJobType': '产品', 'secondJobType': '产品经理', 'thirdJobType': '网页产品经理'},
                 {'url': '110108', 'firstJobType': '产品', 'secondJobType': '产品经理', 'thirdJobType': '产品专员'},
                 {'url': '110105', 'firstJobType': '产品', 'secondJobType': '产品经理', 'thirdJobType': '数据产品经理'},
                 {'url': '110101', 'firstJobType': '产品', 'secondJobType': '产品经理', 'thirdJobType': '产品经理'},
                 {'url': '110109', 'firstJobType': '产品', 'secondJobType': '产品经理', 'thirdJobType': '硬件产品经理'},
                 {'url': '110103', 'firstJobType': '产品', 'secondJobType': '产品经理', 'thirdJobType': '移动产品经理'},
                 {'url': '110106', 'firstJobType': '产品', 'secondJobType': '产品经理', 'thirdJobType': '电商产品经理'},
                 {'url': '110107', 'firstJobType': '产品', 'secondJobType': '产品经理', 'thirdJobType': '游戏策划'},
                 {'url': '110104', 'firstJobType': '产品', 'secondJobType': '产品经理', 'thirdJobType': '产品助理'},
                 {'url': '110303', 'firstJobType': '产品', 'secondJobType': '高端产品职位',
                  'thirdJobType': '游戏制作人'},
                 {'url': '110399', 'firstJobType': '产品', 'secondJobType': '高端产品职位',
                  'thirdJobType': '高端产品职位'},
                 {'url': '110304', 'firstJobType': '产品', 'secondJobType': '高端产品职位', 'thirdJobType': '产品VP'},
                 {'url': '110302', 'firstJobType': '产品', 'secondJobType': '高端产品职位', 'thirdJobType': '产品总监'},
                 {'url': '110401', 'firstJobType': '产品', 'secondJobType': '其他产品职位',
                  'thirdJobType': '其他产品职位'},
                 {'url': '120122', 'firstJobType': '设计', 'secondJobType': '视觉/交互设计', 'thirdJobType': '漫画师'},
                 {'url': '120120', 'firstJobType': '设计', 'secondJobType': '视觉/交互设计',
                  'thirdJobType': '动画设计'},
                 {'url': '120123', 'firstJobType': '设计', 'secondJobType': '视觉/交互设计',
                  'thirdJobType': '人像修图师'},
                 {'url': '120109', 'firstJobType': '设计', 'secondJobType': '视觉/交互设计',
                  'thirdJobType': '多媒体设计师'},
                 {'url': '120119', 'firstJobType': '设计', 'secondJobType': '视觉/交互设计',
                  'thirdJobType': '设计师助理'},
                 {'url': '120107', 'firstJobType': '设计', 'secondJobType': '视觉/交互设计',
                  'thirdJobType': '3D设计师'},
                 {'url': '120110', 'firstJobType': '设计', 'secondJobType': '视觉/交互设计', 'thirdJobType': '原画师'},
                 {'url': '120108', 'firstJobType': '设计', 'secondJobType': '视觉/交互设计',
                  'thirdJobType': '广告设计'},
                 {'url': '120118', 'firstJobType': '设计', 'secondJobType': '视觉/交互设计',
                  'thirdJobType': '包装设计'},
                 {'url': '120104', 'firstJobType': '设计', 'secondJobType': '视觉/交互设计',
                  'thirdJobType': 'APP设计师'},
                 {'url': '120101', 'firstJobType': '设计', 'secondJobType': '视觉/交互设计',
                  'thirdJobType': '视觉设计师'},
                 {'url': '120103', 'firstJobType': '设计', 'secondJobType': '视觉/交互设计',
                  'thirdJobType': 'Flash设计师'},
                 {'url': '120199', 'firstJobType': '设计', 'secondJobType': '视觉/交互设计',
                  'thirdJobType': '视觉设计'},
                 {'url': '120121', 'firstJobType': '设计', 'secondJobType': '视觉/交互设计', 'thirdJobType': '插画师'},
                 {'url': '120102', 'firstJobType': '设计', 'secondJobType': '视觉/交互设计',
                  'thirdJobType': '网页设计师'},
                 {'url': '120117', 'firstJobType': '设计', 'secondJobType': '视觉/交互设计', 'thirdJobType': '美工'},
                 {'url': '120106', 'firstJobType': '设计', 'secondJobType': '视觉/交互设计',
                  'thirdJobType': '平面设计'},
                 {'url': '120105', 'firstJobType': '设计', 'secondJobType': '视觉/交互设计',
                  'thirdJobType': 'UI设计师'},
                 {'url': '120116', 'firstJobType': '设计', 'secondJobType': '视觉/交互设计',
                  'thirdJobType': 'CAD设计/制图'},
                 {'url': '120201', 'firstJobType': '设计', 'secondJobType': '视觉/交互设计',
                  'thirdJobType': '交互设计师'},
                 {'url': '120111', 'firstJobType': '设计', 'secondJobType': '游戏设计', 'thirdJobType': '游戏特效'},
                 {'url': '120303', 'firstJobType': '设计', 'secondJobType': '游戏设计', 'thirdJobType': '游戏数值策划'},
                 {'url': '120115', 'firstJobType': '设计', 'secondJobType': '游戏设计', 'thirdJobType': '游戏动作'},
                 {'url': '120112', 'firstJobType': '设计', 'secondJobType': '游戏设计',
                  'thirdJobType': '游戏界面设计师'},
                 {'url': '120113', 'firstJobType': '设计', 'secondJobType': '游戏设计', 'thirdJobType': '游戏场景'},
                 {'url': '120114', 'firstJobType': '设计', 'secondJobType': '游戏设计', 'thirdJobType': '游戏角色'},
                 {'url': '120301', 'firstJobType': '设计', 'secondJobType': '用户研究', 'thirdJobType': '数据分析师'},
                 {'url': '120408', 'firstJobType': '设计', 'secondJobType': '用户研究', 'thirdJobType': '用户研究总监'},
                 {'url': '120407', 'firstJobType': '设计', 'secondJobType': '用户研究', 'thirdJobType': '用户研究经理'},
                 {'url': '120304', 'firstJobType': '设计', 'secondJobType': '用户研究', 'thirdJobType': 'UX设计师'},
                 {'url': '120302', 'firstJobType': '设计', 'secondJobType': '用户研究', 'thirdJobType': '用户研究员'},
                 {'url': '120404', 'firstJobType': '设计', 'secondJobType': '高端设计职位',
                  'thirdJobType': '视觉设计总监'},
                 {'url': '120401', 'firstJobType': '设计', 'secondJobType': '高端设计职位',
                  'thirdJobType': '设计经理/主管'},
                 {'url': '120499', 'firstJobType': '设计', 'secondJobType': '高端设计职位',
                  'thirdJobType': '高端设计职位'},
                 {'url': '120402', 'firstJobType': '设计', 'secondJobType': '高端设计职位', 'thirdJobType': '设计总监'},
                 {'url': '120603', 'firstJobType': '设计', 'secondJobType': '非视觉设计', 'thirdJobType': '橱柜设计'},
                 {'url': '120607', 'firstJobType': '设计', 'secondJobType': '非视觉设计', 'thirdJobType': '室内设计'},
                 {'url': '120612', 'firstJobType': '设计', 'secondJobType': '非视觉设计', 'thirdJobType': '照明设计'},
                 {'url': '120606', 'firstJobType': '设计', 'secondJobType': '非视觉设计', 'thirdJobType': '珠宝设计'},
                 {'url': '120601', 'firstJobType': '设计', 'secondJobType': '非视觉设计',
                  'thirdJobType': '服装/纺织设计'},
                 {'url': '120699', 'firstJobType': '设计', 'secondJobType': '非视觉设计', 'thirdJobType': '非视觉设计'},
                 {'url': '120605', 'firstJobType': '设计', 'secondJobType': '非视觉设计', 'thirdJobType': '家居设计'},
                 {'url': '120604', 'firstJobType': '设计', 'secondJobType': '非视觉设计', 'thirdJobType': '家具设计'},
                 {'url': '120611', 'firstJobType': '设计', 'secondJobType': '非视觉设计',
                  'thirdJobType': '展览/展示设计'},
                 {'url': '120602', 'firstJobType': '设计', 'secondJobType': '非视觉设计', 'thirdJobType': '工业设计'},
                 {'url': '120608', 'firstJobType': '设计', 'secondJobType': '非视觉设计', 'thirdJobType': '陈列设计'},
                 {'url': '120501', 'firstJobType': '设计', 'secondJobType': '其他设计职位',
                  'thirdJobType': '其他设计职位'},
                 {'url': '130122', 'firstJobType': '运营', 'secondJobType': '运营', 'thirdJobType': '直播运营'},
                 {'url': '130120', 'firstJobType': '运营', 'secondJobType': '运营', 'thirdJobType': '内容审核'},
                 {'url': '130121', 'firstJobType': '运营', 'secondJobType': '运营', 'thirdJobType': '数据标注'},
                 {'url': '130116', 'firstJobType': '运营', 'secondJobType': '运营', 'thirdJobType': '线下拓展运营'},
                 {'url': '130104', 'firstJobType': '运营', 'secondJobType': '运营', 'thirdJobType': '内容运营'},
                 {'url': '130112', 'firstJobType': '运营', 'secondJobType': '运营', 'thirdJobType': '社区运营'},
                 {'url': '130114', 'firstJobType': '运营', 'secondJobType': '运营', 'thirdJobType': '微博运营'},
                 {'url': '130115', 'firstJobType': '运营', 'secondJobType': '运营', 'thirdJobType': '策略运营'},
                 {'url': '130123', 'firstJobType': '运营', 'secondJobType': '运营', 'thirdJobType': '车辆运营'},
                 {'url': '130124', 'firstJobType': '运营', 'secondJobType': '运营', 'thirdJobType': '跨境电商运营'},
                 {'url': '130101', 'firstJobType': '运营', 'secondJobType': '运营', 'thirdJobType': '用户运营'},
                 {'url': '130106', 'firstJobType': '运营', 'secondJobType': '运营', 'thirdJobType': '商家运营'},
                 {'url': '130199', 'firstJobType': '运营', 'secondJobType': '运营', 'thirdJobType': '运营'},
                 {'url': '130108', 'firstJobType': '运营', 'secondJobType': '运营', 'thirdJobType': '游戏运营'},
                 {'url': '130118', 'firstJobType': '运营', 'secondJobType': '运营', 'thirdJobType': '运营助理/专员'},
                 {'url': '130105', 'firstJobType': '运营', 'secondJobType': '运营', 'thirdJobType': '活动运营'},
                 {'url': '130110', 'firstJobType': '运营', 'secondJobType': '运营', 'thirdJobType': '网站运营'},
                 {'url': '130113', 'firstJobType': '运营', 'secondJobType': '运营', 'thirdJobType': '微信运营'},
                 {'url': '130111', 'firstJobType': '运营', 'secondJobType': '运营', 'thirdJobType': '新媒体运营'},
                 {'url': '130107', 'firstJobType': '运营', 'secondJobType': '运营', 'thirdJobType': '品类运营'},
                 {'url': '130103', 'firstJobType': '运营', 'secondJobType': '运营', 'thirdJobType': '数据运营'},
                 {'url': '130125', 'firstJobType': '运营', 'secondJobType': '运营', 'thirdJobType': '网店店长'},
                 {'url': '130117', 'firstJobType': '运营', 'secondJobType': '运营', 'thirdJobType': '电商运营'},
                 {'url': '130102', 'firstJobType': '运营', 'secondJobType': '运营', 'thirdJobType': '产品运营'},
                 {'url': '130204', 'firstJobType': '运营', 'secondJobType': '编辑', 'thirdJobType': '网站编辑'},
                 {'url': '130202', 'firstJobType': '运营', 'secondJobType': '编辑', 'thirdJobType': '内容编辑'},
                 {'url': '130201', 'firstJobType': '运营', 'secondJobType': '编辑', 'thirdJobType': '副主编'},
                 {'url': '130203', 'firstJobType': '运营', 'secondJobType': '编辑', 'thirdJobType': '文案策划'},
                 {'url': '210101', 'firstJobType': '运营', 'secondJobType': '编辑', 'thirdJobType': '医学编辑'},
                 {'url': '130206', 'firstJobType': '运营', 'secondJobType': '编辑', 'thirdJobType': '采编'},
                 {'url': '130299', 'firstJobType': '运营', 'secondJobType': '编辑', 'thirdJobType': '编辑'},
                 {'url': '130302', 'firstJobType': '运营', 'secondJobType': '客服', 'thirdJobType': '售后客服'},
                 {'url': '130304', 'firstJobType': '运营', 'secondJobType': '客服', 'thirdJobType': '客服经理'},
                 {'url': '130303', 'firstJobType': '运营', 'secondJobType': '客服', 'thirdJobType': '网络客服'},
                 {'url': '130308', 'firstJobType': '运营', 'secondJobType': '客服', 'thirdJobType': '电话客服'},
                 {'url': '130309', 'firstJobType': '运营', 'secondJobType': '客服',
                  'thirdJobType': '咨询热线/呼叫中心客服'},
                 {'url': '130306', 'firstJobType': '运营', 'secondJobType': '客服', 'thirdJobType': '客服主管'},
                 {'url': '130301', 'firstJobType': '运营', 'secondJobType': '客服', 'thirdJobType': '售前客服'},
                 {'url': '130305', 'firstJobType': '运营', 'secondJobType': '客服', 'thirdJobType': '客服专员'},
                 {'url': '130402', 'firstJobType': '运营', 'secondJobType': '高端运营职位', 'thirdJobType': '运营总监'},
                 {'url': '130405', 'firstJobType': '运营', 'secondJobType': '高端运营职位',
                  'thirdJobType': '运营经理/主管'},
                 {'url': '130404', 'firstJobType': '运营', 'secondJobType': '高端运营职位', 'thirdJobType': '客服总监'},
                 {'url': '130499', 'firstJobType': '运营', 'secondJobType': '高端运营职位',
                  'thirdJobType': '高端运营职位'},
                 {'url': '130401', 'firstJobType': '运营', 'secondJobType': '高端运营职位', 'thirdJobType': '主编'},
                 {'url': '130403', 'firstJobType': '运营', 'secondJobType': '高端运营职位', 'thirdJobType': 'COO'},
                 {'url': '130501', 'firstJobType': '运营', 'secondJobType': '其他运营职位',
                  'thirdJobType': '其他运营职位'},
                 {'url': '140802', 'firstJobType': '市场', 'secondJobType': '政府事务', 'thirdJobType': '企业党建'},
                 {'url': '140801', 'firstJobType': '市场', 'secondJobType': '政府事务', 'thirdJobType': '政策研究'},
                 {'url': '140112', 'firstJobType': '市场', 'secondJobType': '政府事务', 'thirdJobType': '政府关系'},
                 {'url': '140113', 'firstJobType': '市场', 'secondJobType': '市场/营销', 'thirdJobType': 'APP推广'},
                 {'url': '140103', 'firstJobType': '市场', 'secondJobType': '市场/营销', 'thirdJobType': '市场顾问'},
                 {'url': '140114', 'firstJobType': '市场', 'secondJobType': '市场/营销', 'thirdJobType': '选址开发'},
                 {'url': '140102', 'firstJobType': '市场', 'secondJobType': '市场/营销', 'thirdJobType': '市场策划'},
                 {'url': '140315', 'firstJobType': '市场', 'secondJobType': '市场/营销', 'thirdJobType': '营销主管'},
                 {'url': '140115', 'firstJobType': '市场', 'secondJobType': '市场/营销', 'thirdJobType': '游戏推广'},
                 {'url': '140104', 'firstJobType': '市场', 'secondJobType': '市场/营销', 'thirdJobType': '市场推广'},
                 {'url': '130109', 'firstJobType': '市场', 'secondJobType': '市场/营销', 'thirdJobType': '网络推广'},
                 {'url': '140106', 'firstJobType': '市场', 'secondJobType': '市场/营销', 'thirdJobType': 'SEM'},
                 {'url': '140111', 'firstJobType': '市场', 'secondJobType': '市场/营销', 'thirdJobType': '海外市场'},
                 {'url': '140109', 'firstJobType': '市场', 'secondJobType': '市场/营销', 'thirdJobType': '活动策划'},
                 {'url': '140110', 'firstJobType': '市场', 'secondJobType': '市场/营销', 'thirdJobType': '网络营销'},
                 {'url': '140108', 'firstJobType': '市场', 'secondJobType': '市场/营销',
                  'thirdJobType': '商业数据分析'},
                 {'url': '140107', 'firstJobType': '市场', 'secondJobType': '市场/营销', 'thirdJobType': '商务渠道'},
                 {'url': '140105', 'firstJobType': '市场', 'secondJobType': '市场/营销', 'thirdJobType': 'SEO'},
                 {'url': '140101', 'firstJobType': '市场', 'secondJobType': '市场/营销', 'thirdJobType': '市场营销'},
                 {'url': '140202', 'firstJobType': '市场', 'secondJobType': '公关媒介', 'thirdJobType': '广告协调'},
                 {'url': '140203', 'firstJobType': '市场', 'secondJobType': '公关媒介', 'thirdJobType': '品牌公关'},
                 {'url': '140299', 'firstJobType': '市场', 'secondJobType': '公关媒介', 'thirdJobType': '公关媒介'},
                 {'url': '140206', 'firstJobType': '市场', 'secondJobType': '公关媒介', 'thirdJobType': '媒介策划'},
                 {'url': '140205', 'firstJobType': '市场', 'secondJobType': '公关媒介', 'thirdJobType': '活动策划执行'},
                 {'url': '140201', 'firstJobType': '市场', 'secondJobType': '公关媒介', 'thirdJobType': '媒介经理'},
                 {'url': '140204', 'firstJobType': '市场', 'secondJobType': '公关媒介', 'thirdJobType': '媒介专员'},
                 {'url': '140503', 'firstJobType': '市场', 'secondJobType': '会务会展', 'thirdJobType': '会议活动执行'},
                 {'url': '140599', 'firstJobType': '市场', 'secondJobType': '会务会展', 'thirdJobType': '会务会展'},
                 {'url': '140505', 'firstJobType': '市场', 'secondJobType': '会务会展', 'thirdJobType': '会展活动策划'},
                 {'url': '140506', 'firstJobType': '市场', 'secondJobType': '会务会展', 'thirdJobType': '会展活动执行'},
                 {'url': '140502', 'firstJobType': '市场', 'secondJobType': '会务会展', 'thirdJobType': '会议活动策划'},
                 {'url': '140611', 'firstJobType': '市场', 'secondJobType': '广告', 'thirdJobType': '广告审核'},
                 {'url': '140612', 'firstJobType': '市场', 'secondJobType': '广告',
                  'thirdJobType': '广告/会展项目经理'},
                 {'url': '140605', 'firstJobType': '市场', 'secondJobType': '广告', 'thirdJobType': '广告文案'},
                 {'url': '140602', 'firstJobType': '市场', 'secondJobType': '广告', 'thirdJobType': '美术指导'},
                 {'url': '140699', 'firstJobType': '市场', 'secondJobType': '广告', 'thirdJobType': '广告'},
                 {'url': '140601', 'firstJobType': '市场', 'secondJobType': '广告', 'thirdJobType': '广告创意设计'},
                 {'url': '140607', 'firstJobType': '市场', 'secondJobType': '广告', 'thirdJobType': '广告制作'},
                 {'url': '140609', 'firstJobType': '市场', 'secondJobType': '广告', 'thirdJobType': '媒介合作'},
                 {'url': '140608', 'firstJobType': '市场', 'secondJobType': '广告', 'thirdJobType': '媒介投放'},
                 {'url': '140603', 'firstJobType': '市场', 'secondJobType': '广告', 'thirdJobType': '广告设计'},
                 {'url': '140604', 'firstJobType': '市场', 'secondJobType': '广告', 'thirdJobType': '策划经理'},
                 {'url': '140404', 'firstJobType': '市场', 'secondJobType': '高端市场职位', 'thirdJobType': 'CMO'},
                 {'url': '140405', 'firstJobType': '市场', 'secondJobType': '高端市场职位', 'thirdJobType': '公关总监'},
                 {'url': '140407', 'firstJobType': '市场', 'secondJobType': '高端市场职位', 'thirdJobType': '创意总监'},
                 {'url': '140401', 'firstJobType': '市场', 'secondJobType': '高端市场职位', 'thirdJobType': '市场总监'},
                 {'url': '140406', 'firstJobType': '市场', 'secondJobType': '高端市场职位', 'thirdJobType': '媒介总监'},
                 {'url': '140499', 'firstJobType': '市场', 'secondJobType': '高端市场职位',
                  'thirdJobType': '高端市场职位'},
                 {'url': '140701', 'firstJobType': '市场', 'secondJobType': '其他市场职位',
                  'thirdJobType': '其他市场职位'},
                 {'url': '150110', 'firstJobType': '人事/财务/行政', 'secondJobType': '人力资源',
                  'thirdJobType': '组织发展'},
                 {'url': '150107', 'firstJobType': '人事/财务/行政', 'secondJobType': '人力资源',
                  'thirdJobType': '绩效考核'},
                 {'url': '150403', 'firstJobType': '人事/财务/行政', 'secondJobType': '人力资源',
                  'thirdJobType': '人力资源经理'},
                 {'url': '150406', 'firstJobType': '人事/财务/行政', 'secondJobType': '人力资源',
                  'thirdJobType': '人力资源VP/CHO'},
                 {'url': '150101', 'firstJobType': '人事/财务/行政', 'secondJobType': '人力资源',
                  'thirdJobType': '人力资源主管'},
                 {'url': '150105', 'firstJobType': '人事/财务/行政', 'secondJobType': '人力资源',
                  'thirdJobType': '培训'},
                 {'url': '150108', 'firstJobType': '人事/财务/行政', 'secondJobType': '人力资源',
                  'thirdJobType': '人力资源总监'},
                 {'url': '150104', 'firstJobType': '人事/财务/行政', 'secondJobType': '人力资源',
                  'thirdJobType': '人力资源专员/助理'},
                 {'url': '150102', 'firstJobType': '人事/财务/行政', 'secondJobType': '人力资源',
                  'thirdJobType': '招聘'},
                 {'url': '150106', 'firstJobType': '人事/财务/行政', 'secondJobType': '人力资源',
                  'thirdJobType': '薪资福利'},
                 {'url': '150103', 'firstJobType': '人事/财务/行政', 'secondJobType': '人力资源',
                  'thirdJobType': 'HRBP'},
                 {'url': '150109', 'firstJobType': '人事/财务/行政', 'secondJobType': '人力资源',
                  'thirdJobType': '员工关系'},
                 {'url': '150202', 'firstJobType': '人事/财务/行政', 'secondJobType': '行政', 'thirdJobType': '前台'},
                 {'url': '150207', 'firstJobType': '人事/财务/行政', 'secondJobType': '行政', 'thirdJobType': '后勤'},
                 {'url': '150209', 'firstJobType': '人事/财务/行政', 'secondJobType': '行政',
                  'thirdJobType': '行政总监'},
                 {'url': '150205', 'firstJobType': '人事/财务/行政', 'secondJobType': '行政',
                  'thirdJobType': '经理助理'},
                 {'url': '150401', 'firstJobType': '人事/财务/行政', 'secondJobType': '行政',
                  'thirdJobType': '行政经理'},
                 {'url': '150201', 'firstJobType': '人事/财务/行政', 'secondJobType': '行政',
                  'thirdJobType': '行政专员/助理'},
                 {'url': '150204', 'firstJobType': '人事/财务/行政', 'secondJobType': '行政',
                  'thirdJobType': '行政主管'},
                 {'url': '150301', 'firstJobType': '人事/财务/行政', 'secondJobType': '财务', 'thirdJobType': '会计'},
                 {'url': '150302', 'firstJobType': '人事/财务/行政', 'secondJobType': '财务', 'thirdJobType': '出纳'},
                 {'url': '150309', 'firstJobType': '人事/财务/行政', 'secondJobType': '财务',
                  'thirdJobType': '财务主管'},
                 {'url': '150308', 'firstJobType': '人事/财务/行政', 'secondJobType': '财务',
                  'thirdJobType': '财务总监'},
                 {'url': '150306', 'firstJobType': '人事/财务/行政', 'secondJobType': '财务', 'thirdJobType': '审计'},
                 {'url': '150304', 'firstJobType': '人事/财务/行政', 'secondJobType': '财务', 'thirdJobType': '结算'},
                 {'url': '150303', 'firstJobType': '人事/财务/行政', 'secondJobType': '财务',
                  'thirdJobType': '财务顾问'},
                 {'url': '150402', 'firstJobType': '人事/财务/行政', 'secondJobType': '财务',
                  'thirdJobType': '财务经理'},
                 {'url': '150307', 'firstJobType': '人事/财务/行政', 'secondJobType': '财务', 'thirdJobType': '风控'},
                 {'url': '150310', 'firstJobType': '人事/财务/行政', 'secondJobType': '财务', 'thirdJobType': '成本'},
                 {'url': '150399', 'firstJobType': '人事/财务/行政', 'secondJobType': '财务', 'thirdJobType': '财务'},
                 {'url': '150404', 'firstJobType': '人事/财务/行政', 'secondJobType': '财务', 'thirdJobType': 'CFO'},
                 {'url': '150311', 'firstJobType': '人事/财务/行政', 'secondJobType': '财务',
                  'thirdJobType': '总账会计'},
                 {'url': '150305', 'firstJobType': '人事/财务/行政', 'secondJobType': '财务', 'thirdJobType': '税务'},
                 {'url': '150502', 'firstJobType': '人事/财务/行政', 'secondJobType': '法务', 'thirdJobType': '律师'},
                 {'url': '150505', 'firstJobType': '人事/财务/行政', 'secondJobType': '法务',
                  'thirdJobType': '法务主管'},
                 {'url': '150507', 'firstJobType': '人事/财务/行政', 'secondJobType': '法务',
                  'thirdJobType': '法务总监'},
                 {'url': '150203', 'firstJobType': '人事/财务/行政', 'secondJobType': '法务',
                  'thirdJobType': '法务专员/助理'},
                 {'url': '150504', 'firstJobType': '人事/财务/行政', 'secondJobType': '法务',
                  'thirdJobType': '法律顾问'},
                 {'url': '150506', 'firstJobType': '人事/财务/行政', 'secondJobType': '法务',
                  'thirdJobType': '法务经理'},
                 {'url': '150601', 'firstJobType': '人事/财务/行政', 'secondJobType': '其他职能职位',
                  'thirdJobType': '其他职能职位'},
                 {'url': '150407', 'firstJobType': '高级管理', 'secondJobType': '高级管理职位',
                  'thirdJobType': '总裁/总经理/CEO'},
                 {'url': '150410', 'firstJobType': '高级管理', 'secondJobType': '高级管理职位',
                  'thirdJobType': '区域负责人(辖多个分公司)'},
                 {'url': '150413', 'firstJobType': '高级管理', 'secondJobType': '高级管理职位',
                  'thirdJobType': '联合创始人'},
                 {'url': '150412', 'firstJobType': '高级管理', 'secondJobType': '高级管理职位',
                  'thirdJobType': '合伙人'},
                 {'url': '150411', 'firstJobType': '高级管理', 'secondJobType': '高级管理职位',
                  'thirdJobType': '总助/CEO助理/董事长助理'},
                 {'url': '150409', 'firstJobType': '高级管理', 'secondJobType': '高级管理职位',
                  'thirdJobType': '分公司/代表处负责人'},
                 {'url': '150414', 'firstJobType': '高级管理', 'secondJobType': '高级管理职位',
                  'thirdJobType': '董事会秘书'},
                 {'url': '150499', 'firstJobType': '高级管理', 'secondJobType': '高级管理职位',
                  'thirdJobType': '高级管理职位'},
                 {'url': '150408', 'firstJobType': '高级管理', 'secondJobType': '高级管理职位',
                  'thirdJobType': '副总裁/副总经理/VP'},
                 {'url': '140309', 'firstJobType': '销售', 'secondJobType': '销售行政/商务',
                  'thirdJobType': '销售助理'},
                 {'url': '160301', 'firstJobType': '销售', 'secondJobType': '销售行政/商务',
                  'thirdJobType': '商务专员'},
                 {'url': '160302', 'firstJobType': '销售', 'secondJobType': '销售行政/商务',
                  'thirdJobType': '商务经理'},
                 {'url': '140403', 'firstJobType': '销售', 'secondJobType': '销售行政/商务',
                  'thirdJobType': '商务总监'},
                 {'url': '130119', 'firstJobType': '销售', 'secondJobType': '销售行政/商务',
                  'thirdJobType': '销售运营'},
                 {'url': '220505', 'firstJobType': '销售', 'secondJobType': '房地产销售/招商',
                  'thirdJobType': '房地产销售总监'},
                 {'url': '160401', 'firstJobType': '销售', 'secondJobType': '房地产销售/招商',
                  'thirdJobType': '置业顾问'},
                 {'url': '220399', 'firstJobType': '销售', 'secondJobType': '房地产销售/招商',
                  'thirdJobType': '房地产销售/招商'},
                 {'url': '220403', 'firstJobType': '销售', 'secondJobType': '房地产销售/招商',
                  'thirdJobType': '物业招商管理'},
                 {'url': '160403', 'firstJobType': '销售', 'secondJobType': '房地产销售/招商',
                  'thirdJobType': '地产中介'},
                 {'url': '210602', 'firstJobType': '销售', 'secondJobType': '服务业销售', 'thirdJobType': '瘦身顾问'},
                 {'url': '280103', 'firstJobType': '销售', 'secondJobType': '服务业销售', 'thirdJobType': '旅游顾问'},
                 {'url': '210610', 'firstJobType': '销售', 'secondJobType': '服务业销售', 'thirdJobType': '会籍顾问'},
                 {'url': '290312', 'firstJobType': '销售', 'secondJobType': '服务业销售', 'thirdJobType': '珠宝销售'},
                 {'url': '210406', 'firstJobType': '销售', 'secondJobType': '服务业销售', 'thirdJobType': '彩妆顾问'},
                 {'url': '210414', 'firstJobType': '销售', 'secondJobType': '服务业销售', 'thirdJobType': '美容顾问'},
                 {'url': '230201', 'firstJobType': '销售', 'secondJobType': '汽车销售', 'thirdJobType': '汽车销售'},
                 {'url': '230202', 'firstJobType': '销售', 'secondJobType': '汽车销售', 'thirdJobType': '汽车配件销售'},
                 {'url': '140610', 'firstJobType': '销售', 'secondJobType': '广告/会展销售',
                  'thirdJobType': '媒介顾问'},
                 {'url': '140501', 'firstJobType': '销售', 'secondJobType': '广告/会展销售',
                  'thirdJobType': '会议活动销售'},
                 {'url': '140313', 'firstJobType': '销售', 'secondJobType': '广告/会展销售',
                  'thirdJobType': '广告销售'},
                 {'url': '140504', 'firstJobType': '销售', 'secondJobType': '广告/会展销售',
                  'thirdJobType': '会展活动销售'},
                 {'url': '180401', 'firstJobType': '销售', 'secondJobType': '金融销售', 'thirdJobType': '信用卡销售'},
                 {'url': '180801', 'firstJobType': '销售', 'secondJobType': '金融销售', 'thirdJobType': '证券经纪人'},
                 {'url': '180701', 'firstJobType': '销售', 'secondJobType': '金融销售', 'thirdJobType': '保险顾问'},
                 {'url': '180506', 'firstJobType': '销售', 'secondJobType': '金融销售', 'thirdJobType': '理财顾问'},
                 {'url': '250203', 'firstJobType': '销售', 'secondJobType': '外贸销售', 'thirdJobType': '外贸业务员'},
                 {'url': '250201', 'firstJobType': '销售', 'secondJobType': '外贸销售', 'thirdJobType': '外贸经理'},
                 {'url': '140399', 'firstJobType': '销售', 'secondJobType': '销售', 'thirdJobType': '销售'},
                 {'url': '140308', 'firstJobType': '销售', 'secondJobType': '销售', 'thirdJobType': '代理商销售'},
                 {'url': '140316', 'firstJobType': '销售', 'secondJobType': '销售', 'thirdJobType': '销售工程师'},
                 {'url': '140311', 'firstJobType': '销售', 'secondJobType': '销售', 'thirdJobType': '销售顾问'},
                 {'url': '140305', 'firstJobType': '销售', 'secondJobType': '销售', 'thirdJobType': 'BD经理'},
                 {'url': '140314', 'firstJobType': '销售', 'secondJobType': '销售', 'thirdJobType': '网络销售'},
                 {'url': '140304', 'firstJobType': '销售', 'secondJobType': '销售', 'thirdJobType': '大客户代表'},
                 {'url': '140307', 'firstJobType': '销售', 'secondJobType': '销售', 'thirdJobType': '渠道销售'},
                 {'url': '140301', 'firstJobType': '销售', 'secondJobType': '销售', 'thirdJobType': '销售专员'},
                 {'url': '140317', 'firstJobType': '销售', 'secondJobType': '销售', 'thirdJobType': '客户经理'},
                 {'url': '140303', 'firstJobType': '销售', 'secondJobType': '销售', 'thirdJobType': '客户代表'},
                 {'url': '140310', 'firstJobType': '销售', 'secondJobType': '销售', 'thirdJobType': '电话销售'},
                 {'url': '190603', 'firstJobType': '销售', 'secondJobType': '课程销售', 'thirdJobType': '留学顾问'},
                 {'url': '190602', 'firstJobType': '销售', 'secondJobType': '课程销售', 'thirdJobType': '招生顾问'},
                 {'url': '190601', 'firstJobType': '销售', 'secondJobType': '课程销售', 'thirdJobType': '课程顾问'},
                 {'url': '210599', 'firstJobType': '销售', 'secondJobType': '医疗销售', 'thirdJobType': '医疗销售'},
                 {'url': '210502', 'firstJobType': '销售', 'secondJobType': '医疗销售', 'thirdJobType': '医药代表'},
                 {'url': '210506', 'firstJobType': '销售', 'secondJobType': '医疗销售', 'thirdJobType': '医疗器械销售'},
                 {'url': '210504', 'firstJobType': '销售', 'secondJobType': '医疗销售', 'thirdJobType': '健康顾问'},
                 {'url': '210505', 'firstJobType': '销售', 'secondJobType': '医疗销售', 'thirdJobType': '医美咨询'},
                 {'url': '160104', 'firstJobType': '销售', 'secondJobType': '销售管理', 'thirdJobType': '团队经理'},
                 {'url': '160101', 'firstJobType': '销售', 'secondJobType': '销售管理', 'thirdJobType': '区域总监'},
                 {'url': '140302', 'firstJobType': '销售', 'secondJobType': '销售管理', 'thirdJobType': '销售经理'},
                 {'url': '160199', 'firstJobType': '销售', 'secondJobType': '销售管理', 'thirdJobType': '销售管理'},
                 {'url': '160103', 'firstJobType': '销售', 'secondJobType': '销售管理', 'thirdJobType': '销售VP'},
                 {'url': '140402', 'firstJobType': '销售', 'secondJobType': '销售管理', 'thirdJobType': '销售总监'},
                 {'url': '160102', 'firstJobType': '销售', 'secondJobType': '销售管理', 'thirdJobType': '城市经理'},
                 {'url': '160201', 'firstJobType': '销售', 'secondJobType': '其他销售职位',
                  'thirdJobType': '其他销售职位'},
                 {'url': '170103', 'firstJobType': '传媒', 'secondJobType': '采编/写作/出版', 'thirdJobType': '采编'},
                 {'url': '170104', 'firstJobType': '传媒', 'secondJobType': '采编/写作/出版', 'thirdJobType': '撰稿人'},
                 {'url': '170101', 'firstJobType': '传媒', 'secondJobType': '采编/写作/出版', 'thirdJobType': '记者'},
                 {'url': '170108', 'firstJobType': '传媒', 'secondJobType': '采编/写作/出版', 'thirdJobType': '自媒体'},
                 {'url': '170199', 'firstJobType': '传媒', 'secondJobType': '采编/写作/出版',
                  'thirdJobType': '采编/写作/出版'},
                 {'url': '170109', 'firstJobType': '传媒', 'secondJobType': '采编/写作/出版',
                  'thirdJobType': '排版设计'},
                 {'url': '170107', 'firstJobType': '传媒', 'secondJobType': '采编/写作/出版', 'thirdJobType': '总编'},
                 {'url': '170102', 'firstJobType': '传媒', 'secondJobType': '采编/写作/出版', 'thirdJobType': '编辑'},
                 {'url': '170106', 'firstJobType': '传媒', 'secondJobType': '采编/写作/出版',
                  'thirdJobType': '校对录入'},
                 {'url': '170105', 'firstJobType': '传媒', 'secondJobType': '采编/写作/出版',
                  'thirdJobType': '出版发行'},
                 {'url': '170306', 'firstJobType': '传媒', 'secondJobType': '公关媒介', 'thirdJobType': '媒介策划'},
                 {'url': '170302', 'firstJobType': '传媒', 'secondJobType': '公关媒介', 'thirdJobType': '媒介专员'},
                 {'url': '170301', 'firstJobType': '传媒', 'secondJobType': '公关媒介', 'thirdJobType': '媒介经理'},
                 {'url': '170305', 'firstJobType': '传媒', 'secondJobType': '公关媒介', 'thirdJobType': '活动策划执行'},
                 {'url': '170399', 'firstJobType': '传媒', 'secondJobType': '公关媒介', 'thirdJobType': '公关媒介'},
                 {'url': '170303', 'firstJobType': '传媒', 'secondJobType': '公关媒介', 'thirdJobType': '广告协调'},
                 {'url': '170304', 'firstJobType': '传媒', 'secondJobType': '公关媒介', 'thirdJobType': '品牌公关'},
                 {'url': '170203', 'firstJobType': '传媒', 'secondJobType': '广告', 'thirdJobType': '广告设计'},
                 {'url': '170209', 'firstJobType': '传媒', 'secondJobType': '广告', 'thirdJobType': '媒介合作'},
                 {'url': '170211', 'firstJobType': '传媒', 'secondJobType': '广告', 'thirdJobType': '广告审核'},
                 {'url': '170201', 'firstJobType': '传媒', 'secondJobType': '广告', 'thirdJobType': '广告创意设计'},
                 {'url': '170202', 'firstJobType': '传媒', 'secondJobType': '广告', 'thirdJobType': '美术指导'},
                 {'url': '170208', 'firstJobType': '传媒', 'secondJobType': '广告', 'thirdJobType': '媒介投放'},
                 {'url': '170299', 'firstJobType': '传媒', 'secondJobType': '广告', 'thirdJobType': '广告'},
                 {'url': '170204', 'firstJobType': '传媒', 'secondJobType': '广告', 'thirdJobType': '策划经理'},
                 {'url': '170207', 'firstJobType': '传媒', 'secondJobType': '广告', 'thirdJobType': '广告制作'},
                 {'url': '170205', 'firstJobType': '传媒', 'secondJobType': '广告', 'thirdJobType': '广告文案'},
                 {'url': '170212', 'firstJobType': '传媒', 'secondJobType': '广告',
                  'thirdJobType': '广告/会展项目经理'},
                 {'url': '170617', 'firstJobType': '传媒', 'secondJobType': '影视媒体', 'thirdJobType': '艺人助理'},
                 {'url': '170601', 'firstJobType': '传媒', 'secondJobType': '影视媒体', 'thirdJobType': '导演/编导'},
                 {'url': '170615', 'firstJobType': '传媒', 'secondJobType': '影视媒体', 'thirdJobType': '制片人'},
                 {'url': '170624', 'firstJobType': '传媒', 'secondJobType': '影视媒体', 'thirdJobType': '影视特效'},
                 {'url': '170610', 'firstJobType': '传媒', 'secondJobType': '影视媒体', 'thirdJobType': '主播'},
                 {'url': '170606', 'firstJobType': '传媒', 'secondJobType': '影视媒体', 'thirdJobType': '后期制作'},
                 {'url': '170604', 'firstJobType': '传媒', 'secondJobType': '影视媒体', 'thirdJobType': '音频编辑'},
                 {'url': '170608', 'firstJobType': '传媒', 'secondJobType': '影视媒体', 'thirdJobType': '影视发行'},
                 {'url': '170623', 'firstJobType': '传媒', 'secondJobType': '影视媒体', 'thirdJobType': '剪辑师'},
                 {'url': '170699', 'firstJobType': '传媒', 'secondJobType': '影视媒体', 'thirdJobType': '影视媒体'},
                 {'url': '170609', 'firstJobType': '传媒', 'secondJobType': '影视媒体', 'thirdJobType': '影视策划'},
                 {'url': '170603', 'firstJobType': '传媒', 'secondJobType': '影视媒体', 'thirdJobType': '视频编辑'},
                 {'url': '170613', 'firstJobType': '传媒', 'secondJobType': '影视媒体', 'thirdJobType': '放映员'},
                 {'url': '170605', 'firstJobType': '传媒', 'secondJobType': '影视媒体', 'thirdJobType': '经纪人'},
                 {'url': '170611', 'firstJobType': '传媒', 'secondJobType': '影视媒体',
                  'thirdJobType': '演员/配音/模特'},
                 {'url': '170622', 'firstJobType': '传媒', 'secondJobType': '影视媒体', 'thirdJobType': '灯光师'},
                 {'url': '170614', 'firstJobType': '传媒', 'secondJobType': '影视媒体', 'thirdJobType': '录音/音效'},
                 {'url': '170620', 'firstJobType': '传媒', 'secondJobType': '影视媒体', 'thirdJobType': '主持人/DJ'},
                 {'url': '170616', 'firstJobType': '传媒', 'secondJobType': '影视媒体', 'thirdJobType': '编剧'},
                 {'url': '170602', 'firstJobType': '传媒', 'secondJobType': '影视媒体', 'thirdJobType': '摄影/摄像'},
                 {'url': '170621', 'firstJobType': '传媒', 'secondJobType': '影视媒体', 'thirdJobType': '主播助理'},
                 {'url': '170612', 'firstJobType': '传媒', 'secondJobType': '影视媒体',
                  'thirdJobType': '化妆/造型/服装'},
                 {'url': '170501', 'firstJobType': '传媒', 'secondJobType': '其他传媒职位',
                  'thirdJobType': '其他传媒职位'},
                 {'url': '180104', 'firstJobType': '金融', 'secondJobType': '投融资', 'thirdJobType': '资产管理'},
                 {'url': '180119', 'firstJobType': '金融', 'secondJobType': '投融资', 'thirdJobType': '投资顾问'},
                 {'url': '180112', 'firstJobType': '金融', 'secondJobType': '投融资', 'thirdJobType': '投资总监'},
                 {'url': '180103', 'firstJobType': '金融', 'secondJobType': '投融资', 'thirdJobType': '行业研究'},
                 {'url': '180117', 'firstJobType': '金融', 'secondJobType': '投融资', 'thirdJobType': '投后管理'},
                 {'url': '180113', 'firstJobType': '金融', 'secondJobType': '投融资', 'thirdJobType': '投资VP'},
                 {'url': '180116', 'firstJobType': '金融', 'secondJobType': '投融资', 'thirdJobType': '并购'},
                 {'url': '180199', 'firstJobType': '金融', 'secondJobType': '投融资', 'thirdJobType': '投融资'},
                 {'url': '180118', 'firstJobType': '金融', 'secondJobType': '投融资', 'thirdJobType': '投资助理'},
                 {'url': '180115', 'firstJobType': '金融', 'secondJobType': '投融资', 'thirdJobType': '融资'},
                 {'url': '180101', 'firstJobType': '金融', 'secondJobType': '投融资', 'thirdJobType': '投资经理'},
                 {'url': '180114', 'firstJobType': '金融', 'secondJobType': '投融资', 'thirdJobType': '投资合伙人'},
                 {'url': '180111', 'firstJobType': '金融', 'secondJobType': '投融资', 'thirdJobType': '其他投融资职位'},
                 {'url': '180202', 'firstJobType': '金融', 'secondJobType': '风控', 'thirdJobType': '律师'},
                 {'url': '180204', 'firstJobType': '金融', 'secondJobType': '风控', 'thirdJobType': '合规稽查'},
                 {'url': '180203', 'firstJobType': '金融', 'secondJobType': '风控', 'thirdJobType': '资信评估'},
                 {'url': '180201', 'firstJobType': '金融', 'secondJobType': '风控', 'thirdJobType': '风控'},
                 {'url': '180302', 'firstJobType': '金融', 'secondJobType': '税务审计', 'thirdJobType': '法务'},
                 {'url': '180304', 'firstJobType': '金融', 'secondJobType': '税务审计', 'thirdJobType': '清算'},
                 {'url': '180303', 'firstJobType': '金融', 'secondJobType': '税务审计', 'thirdJobType': '会计'},
                 {'url': '180301', 'firstJobType': '金融', 'secondJobType': '税务审计', 'thirdJobType': '审计'},
                 {'url': '180107', 'firstJobType': '金融', 'secondJobType': '银行', 'thirdJobType': '风控'},
                 {'url': '180403', 'firstJobType': '金融', 'secondJobType': '银行', 'thirdJobType': '商务渠道'},
                 {'url': '180499', 'firstJobType': '金融', 'secondJobType': '银行', 'thirdJobType': '银行'},
                 {'url': '180406', 'firstJobType': '金融', 'secondJobType': '银行', 'thirdJobType': '信贷管理'},
                 {'url': '180402', 'firstJobType': '金融', 'secondJobType': '银行', 'thirdJobType': '柜员'},
                 {'url': '180405', 'firstJobType': '金融', 'secondJobType': '银行', 'thirdJobType': '客户经理'},
                 {'url': '180102', 'firstJobType': '金融', 'secondJobType': '银行', 'thirdJobType': '分析师'},
                 {'url': '180404', 'firstJobType': '金融', 'secondJobType': '银行', 'thirdJobType': '大堂经理'},
                 {'url': '180504', 'firstJobType': '金融', 'secondJobType': '互联网金融', 'thirdJobType': '分析师'},
                 {'url': '180501', 'firstJobType': '金融', 'secondJobType': '互联网金融',
                  'thirdJobType': '金融产品经理'},
                 {'url': '180505', 'firstJobType': '金融', 'secondJobType': '互联网金融', 'thirdJobType': '投资经理'},
                 {'url': '180110', 'firstJobType': '金融', 'secondJobType': '互联网金融', 'thirdJobType': '清算'},
                 {'url': '180109', 'firstJobType': '金融', 'secondJobType': '互联网金融', 'thirdJobType': '审计'},
                 {'url': '180502', 'firstJobType': '金融', 'secondJobType': '互联网金融', 'thirdJobType': '风控'},
                 {'url': '180503', 'firstJobType': '金融', 'secondJobType': '互联网金融', 'thirdJobType': '催收员'},
                 {'url': '180599', 'firstJobType': '金融', 'secondJobType': '互联网金融', 'thirdJobType': '互联网金融'},
                 {'url': '180703', 'firstJobType': '金融', 'secondJobType': '保险', 'thirdJobType': '保险理赔'},
                 {'url': '180702', 'firstJobType': '金融', 'secondJobType': '保险', 'thirdJobType': '保险精算师'},
                 {'url': '180899', 'firstJobType': '金融', 'secondJobType': '证券', 'thirdJobType': '证券'},
                 {'url': '180802', 'firstJobType': '金融', 'secondJobType': '证券', 'thirdJobType': '证券分析师'},
                 {'url': '180106', 'firstJobType': '金融', 'secondJobType': '证券', 'thirdJobType': '交易员'},
                 {'url': '180601', 'firstJobType': '金融', 'secondJobType': '其他金融职位',
                  'thirdJobType': '其他金融职位'},
                 {'url': '190104', 'firstJobType': '教育培训', 'secondJobType': '教育产品研发',
                  'thirdJobType': '培训研究'},
                 {'url': '190102', 'firstJobType': '教育培训', 'secondJobType': '教育产品研发',
                  'thirdJobType': '课程编辑'},
                 {'url': '190107', 'firstJobType': '教育培训', 'secondJobType': '教育产品研发',
                  'thirdJobType': '培训策划'},
                 {'url': '190106', 'firstJobType': '教育培训', 'secondJobType': '教育产品研发',
                  'thirdJobType': '其他教育产品研发职位'},
                 {'url': '190199', 'firstJobType': '教育培训', 'secondJobType': '教育产品研发',
                  'thirdJobType': '教育产品研发'},
                 {'url': '190101', 'firstJobType': '教育培训', 'secondJobType': '教育产品研发',
                  'thirdJobType': '课程设计'},
                 {'url': '190105', 'firstJobType': '教育培训', 'secondJobType': '教育产品研发',
                  'thirdJobType': '培训师'},
                 {'url': '190299', 'firstJobType': '教育培训', 'secondJobType': '教育行政', 'thirdJobType': '教育行政'},
                 {'url': '190201', 'firstJobType': '教育培训', 'secondJobType': '教育行政',
                  'thirdJobType': '校长/副校长'},
                 {'url': '190204', 'firstJobType': '教育培训', 'secondJobType': '教育行政',
                  'thirdJobType': '班主任/辅导员'},
                 {'url': '190202', 'firstJobType': '教育培训', 'secondJobType': '教育行政', 'thirdJobType': '教务管理'},
                 {'url': '190205', 'firstJobType': '教育培训', 'secondJobType': '教育行政',
                  'thirdJobType': '园长/副园长'},
                 {'url': '190203', 'firstJobType': '教育培训', 'secondJobType': '教育行政', 'thirdJobType': '教学管理'},
                 {'url': '190318', 'firstJobType': '教育培训', 'secondJobType': '教师', 'thirdJobType': '物理教师'},
                 {'url': '190320', 'firstJobType': '教育培训', 'secondJobType': '教师', 'thirdJobType': '生物教师'},
                 {'url': '190304', 'firstJobType': '教育培训', 'secondJobType': '教师', 'thirdJobType': '初中教师'},
                 {'url': '190301', 'firstJobType': '教育培训', 'secondJobType': '教师', 'thirdJobType': '教师'},
                 {'url': '190305', 'firstJobType': '教育培训', 'secondJobType': '教师', 'thirdJobType': '小学教师'},
                 {'url': '190315', 'firstJobType': '教育培训', 'secondJobType': '教师', 'thirdJobType': '其他外语教师'},
                 {'url': '190307', 'firstJobType': '教育培训', 'secondJobType': '教师', 'thirdJobType': '理科教师'},
                 {'url': '190313', 'firstJobType': '教育培训', 'secondJobType': '教师', 'thirdJobType': '就业老师'},
                 {'url': '190321', 'firstJobType': '教育培训', 'secondJobType': '教师', 'thirdJobType': '家教'},
                 {'url': '190308', 'firstJobType': '教育培训', 'secondJobType': '教师', 'thirdJobType': '文科教师'},
                 {'url': '190323', 'firstJobType': '教育培训', 'secondJobType': '教师', 'thirdJobType': '早教老师'},
                 {'url': '190310', 'firstJobType': '教育培训', 'secondJobType': '教师', 'thirdJobType': '音乐教师'},
                 {'url': '190312', 'firstJobType': '教育培训', 'secondJobType': '教师', 'thirdJobType': '体育教师'},
                 {'url': '190302', 'firstJobType': '教育培训', 'secondJobType': '教师', 'thirdJobType': '助教'},
                 {'url': '190314', 'firstJobType': '教育培训', 'secondJobType': '教师', 'thirdJobType': '日语教师'},
                 {'url': '190303', 'firstJobType': '教育培训', 'secondJobType': '教师', 'thirdJobType': '高中教师'},
                 {'url': '190319', 'firstJobType': '教育培训', 'secondJobType': '教师', 'thirdJobType': '化学教师'},
                 {'url': '190322', 'firstJobType': '教育培训', 'secondJobType': '教师', 'thirdJobType': '托管老师'},
                 {'url': '190311', 'firstJobType': '教育培训', 'secondJobType': '教师', 'thirdJobType': '美术教师'},
                 {'url': '190306', 'firstJobType': '教育培训', 'secondJobType': '教师', 'thirdJobType': '幼教'},
                 {'url': '190317', 'firstJobType': '教育培训', 'secondJobType': '教师', 'thirdJobType': '数学教师'},
                 {'url': '190309', 'firstJobType': '教育培训', 'secondJobType': '教师', 'thirdJobType': '英语教师'},
                 {'url': '190316', 'firstJobType': '教育培训', 'secondJobType': '教师', 'thirdJobType': '语文教师'},
                 {'url': '190401', 'firstJobType': '教育培训', 'secondJobType': 'IT培训',
                  'thirdJobType': 'JAVA培训讲师'},
                 {'url': '190407', 'firstJobType': '教育培训', 'secondJobType': 'IT培训',
                  'thirdJobType': 'Unity 3D培训讲师'},
                 {'url': '190405', 'firstJobType': '教育培训', 'secondJobType': 'IT培训',
                  'thirdJobType': '.NET培训讲师'},
                 {'url': '190411', 'firstJobType': '教育培训', 'secondJobType': 'IT培训',
                  'thirdJobType': 'UI设计培训讲师'},
                 {'url': '190409', 'firstJobType': '教育培训', 'secondJobType': 'IT培训',
                  'thirdJobType': '软件测试培训讲师'},
                 {'url': '190406', 'firstJobType': '教育培训', 'secondJobType': 'IT培训',
                  'thirdJobType': 'C++培训讲师'},
                 {'url': '190403', 'firstJobType': '教育培训', 'secondJobType': 'IT培训',
                  'thirdJobType': 'iOS培训讲师'},
                 {'url': '190410', 'firstJobType': '教育培训', 'secondJobType': 'IT培训',
                  'thirdJobType': '动漫培训讲师'},
                 {'url': '190404', 'firstJobType': '教育培训', 'secondJobType': 'IT培训',
                  'thirdJobType': 'PHP培训讲师'},
                 {'url': '190402', 'firstJobType': '教育培训', 'secondJobType': 'IT培训',
                  'thirdJobType': 'Android培训讲师'},
                 {'url': '190408', 'firstJobType': '教育培训', 'secondJobType': 'IT培训',
                  'thirdJobType': 'Web前端培训讲师'},
                 {'url': '190499', 'firstJobType': '教育培训', 'secondJobType': 'IT培训', 'thirdJobType': 'IT培训'},
                 {'url': '190501', 'firstJobType': '教育培训', 'secondJobType': '职业培训',
                  'thirdJobType': '财会培训讲师'},
                 {'url': '190502', 'firstJobType': '教育培训', 'secondJobType': '职业培训',
                  'thirdJobType': 'HR培训讲师'},
                 {'url': '190503', 'firstJobType': '教育培训', 'secondJobType': '职业培训', 'thirdJobType': '培训师'},
                 {'url': '190504', 'firstJobType': '教育培训', 'secondJobType': '职业培训', 'thirdJobType': '拓展培训'},
                 {'url': '190715', 'firstJobType': '教育培训', 'secondJobType': '特长培训', 'thirdJobType': '古筝教师'},
                 {'url': '190714', 'firstJobType': '教育培训', 'secondJobType': '特长培训', 'thirdJobType': '吉他教师'},
                 {'url': '190709', 'firstJobType': '教育培训', 'secondJobType': '特长培训', 'thirdJobType': '轮滑教练'},
                 {'url': '190701', 'firstJobType': '教育培训', 'secondJobType': '特长培训', 'thirdJobType': '舞蹈老师'},
                 {'url': '190711', 'firstJobType': '教育培训', 'secondJobType': '特长培训',
                  'thirdJobType': '机器人教师'},
                 {'url': '190704', 'firstJobType': '教育培训', 'secondJobType': '特长培训', 'thirdJobType': '游泳教练'},
                 {'url': '190717', 'firstJobType': '教育培训', 'secondJobType': '特长培训', 'thirdJobType': '乐高教师'},
                 {'url': '190708', 'firstJobType': '教育培训', 'secondJobType': '特长培训', 'thirdJobType': '武术教练'},
                 {'url': '190707', 'firstJobType': '教育培训', 'secondJobType': '特长培训',
                  'thirdJobType': '跆拳道教练'},
                 {'url': '190713', 'firstJobType': '教育培训', 'secondJobType': '特长培训', 'thirdJobType': '钢琴教师'},
                 {'url': '190710', 'firstJobType': '教育培训', 'secondJobType': '特长培训', 'thirdJobType': '表演教师'},
                 {'url': '190799', 'firstJobType': '教育培训', 'secondJobType': '特长培训', 'thirdJobType': '教练'},
                 {'url': '190716', 'firstJobType': '教育培训', 'secondJobType': '特长培训',
                  'thirdJobType': '播音主持教师'},
                 {'url': '190706', 'firstJobType': '教育培训', 'secondJobType': '特长培训',
                  'thirdJobType': '篮球/羽毛球教练'},
                 {'url': '190702', 'firstJobType': '教育培训', 'secondJobType': '特长培训', 'thirdJobType': '瑜伽老师'},
                 {'url': '190705', 'firstJobType': '教育培训', 'secondJobType': '特长培训', 'thirdJobType': '健身教练'},
                 {'url': '190712', 'firstJobType': '教育培训', 'secondJobType': '特长培训', 'thirdJobType': '书法教师'},
                 {'url': '190801', 'firstJobType': '教育培训', 'secondJobType': '其他教育培训职位',
                  'thirdJobType': '其他教育培训职位'},
                 {'url': '210120', 'firstJobType': '医疗健康', 'secondJobType': '临床试验',
                  'thirdJobType': '临床数据分析'},
                 {'url': '210501', 'firstJobType': '医疗健康', 'secondJobType': '临床试验', 'thirdJobType': '医学总监'},
                 {'url': '210119', 'firstJobType': '医疗健康', 'secondJobType': '临床试验', 'thirdJobType': '临床协调'},
                 {'url': '211001', 'firstJobType': '医疗健康', 'secondJobType': '临床试验',
                  'thirdJobType': '临床项目经理'},
                 {'url': '210118', 'firstJobType': '医疗健康', 'secondJobType': '临床试验', 'thirdJobType': '临床研究'},
                 {'url': '210305', 'firstJobType': '医疗健康', 'secondJobType': '医生/医技',
                  'thirdJobType': '康复治疗师'},
                 {'url': '210303', 'firstJobType': '医疗健康', 'secondJobType': '医生/医技',
                  'thirdJobType': '心理医生'},
                 {'url': '210103', 'firstJobType': '医疗健康', 'secondJobType': '医生/医技', 'thirdJobType': '医生'},
                 {'url': '210109', 'firstJobType': '医疗健康', 'secondJobType': '医生/医技', 'thirdJobType': '验光师'},
                 {'url': '210306', 'firstJobType': '医疗健康', 'secondJobType': '医生/医技',
                  'thirdJobType': '内科医生'},
                 {'url': '210302', 'firstJobType': '医疗健康', 'secondJobType': '医生/医技', 'thirdJobType': '中医'},
                 {'url': '210113', 'firstJobType': '医疗健康', 'secondJobType': '医生/医技',
                  'thirdJobType': '医学影像/放射科医师'},
                 {'url': '210107', 'firstJobType': '医疗健康', 'secondJobType': '医生/医技',
                  'thirdJobType': '其他医生职位'},
                 {'url': '210112', 'firstJobType': '医疗健康', 'secondJobType': '医生/医技',
                  'thirdJobType': '医生助理'},
                 {'url': '210304', 'firstJobType': '医疗健康', 'secondJobType': '医生/医技',
                  'thirdJobType': '牙科医生'},
                 {'url': '210307', 'firstJobType': '医疗健康', 'secondJobType': '医生/医技',
                  'thirdJobType': '全科医生'},
                 {'url': '210104', 'firstJobType': '医疗健康', 'secondJobType': '医生/医技', 'thirdJobType': '药剂师'},
                 {'url': '210111', 'firstJobType': '医疗健康', 'secondJobType': '医生/医技',
                  'thirdJobType': '检验科医师'},
                 {'url': '210114', 'firstJobType': '医疗健康', 'secondJobType': '医生/医技', 'thirdJobType': 'B超医生'},
                 {'url': '210503', 'firstJobType': '医疗健康', 'secondJobType': '护士/护理', 'thirdJobType': '导医'},
                 {'url': '210202', 'firstJobType': '医疗健康', 'secondJobType': '护士/护理', 'thirdJobType': '护士长'},
                 {'url': '210201', 'firstJobType': '医疗健康', 'secondJobType': '护士/护理', 'thirdJobType': '护士'},
                 {'url': '210404', 'firstJobType': '医疗健康', 'secondJobType': '健康整形', 'thirdJobType': '针灸推拿'},
                 {'url': '210499', 'firstJobType': '医疗健康', 'secondJobType': '健康整形', 'thirdJobType': '健康整形'},
                 {'url': '210402', 'firstJobType': '医疗健康', 'secondJobType': '健康整形', 'thirdJobType': '整形师'},
                 {'url': '210403', 'firstJobType': '医疗健康', 'secondJobType': '健康整形', 'thirdJobType': '理疗师'},
                 {'url': '210401', 'firstJobType': '医疗健康', 'secondJobType': '健康整形', 'thirdJobType': '营养师'},
                 {'url': '210116', 'firstJobType': '医疗健康', 'secondJobType': '生物制药', 'thirdJobType': '药品注册'},
                 {'url': '210115', 'firstJobType': '医疗健康', 'secondJobType': '生物制药', 'thirdJobType': '生物制药'},
                 {'url': '210117', 'firstJobType': '医疗健康', 'secondJobType': '生物制药', 'thirdJobType': '药品生产'},
                 {'url': '210123', 'firstJobType': '医疗健康', 'secondJobType': '生物制药',
                  'thirdJobType': '医药项目经理'},
                 {'url': '210108', 'firstJobType': '医疗健康', 'secondJobType': '生物制药', 'thirdJobType': '医药研发'},
                 {'url': '210122', 'firstJobType': '医疗健康', 'secondJobType': '医疗器械',
                  'thirdJobType': '医疗器械生产/质量管理'},
                 {'url': '210121', 'firstJobType': '医疗健康', 'secondJobType': '医疗器械',
                  'thirdJobType': '医疗器械注册'},
                 {'url': '210105', 'firstJobType': '医疗健康', 'secondJobType': '医疗器械',
                  'thirdJobType': '医疗器械研发'},
                 {'url': '210801', 'firstJobType': '医疗健康', 'secondJobType': '药店', 'thirdJobType': '药店店长'},
                 {'url': '210802', 'firstJobType': '医疗健康', 'secondJobType': '药店',
                  'thirdJobType': '执业药师/驻店药师'},
                 {'url': '210803', 'firstJobType': '医疗健康', 'secondJobType': '药店', 'thirdJobType': '药店店员'},
                 {'url': '210701', 'firstJobType': '医疗健康', 'secondJobType': '其他医疗健康职位',
                  'thirdJobType': '其他医疗健康职位'},
                 {'url': '250101', 'firstJobType': '采购/贸易', 'secondJobType': '采购', 'thirdJobType': '采购总监'},
                 {'url': '250103', 'firstJobType': '采购/贸易', 'secondJobType': '采购', 'thirdJobType': '采购专员'},
                 {'url': '250104', 'firstJobType': '采购/贸易', 'secondJobType': '采购', 'thirdJobType': '买手'},
                 {'url': '140312', 'firstJobType': '采购/贸易', 'secondJobType': '采购', 'thirdJobType': '商品经理'},
                 {'url': '250106', 'firstJobType': '采购/贸易', 'secondJobType': '采购', 'thirdJobType': '采购主管'},
                 {'url': '250105', 'firstJobType': '采购/贸易', 'secondJobType': '采购', 'thirdJobType': '采购工程师'},
                 {'url': '250199', 'firstJobType': '采购/贸易', 'secondJobType': '采购', 'thirdJobType': '采购'},
                 {'url': '250108', 'firstJobType': '采购/贸易', 'secondJobType': '采购',
                  'thirdJobType': '供应商质量工程师'},
                 {'url': '250102', 'firstJobType': '采购/贸易', 'secondJobType': '采购', 'thirdJobType': '采购经理'},
                 {'url': '250107', 'firstJobType': '采购/贸易', 'secondJobType': '采购', 'thirdJobType': '采购助理'},
                 {'url': '240114', 'firstJobType': '采购/贸易', 'secondJobType': '进出口贸易',
                  'thirdJobType': '报关/报检员'},
                 {'url': '250204', 'firstJobType': '采购/贸易', 'secondJobType': '进出口贸易',
                  'thirdJobType': '贸易跟单'},
                 {'url': '240117', 'firstJobType': '采购/贸易', 'secondJobType': '进出口贸易',
                  'thirdJobType': '单证员'},
                 {'url': '250299', 'firstJobType': '采购/贸易', 'secondJobType': '进出口贸易',
                  'thirdJobType': '进出口贸易'},
                 {'url': '250301', 'firstJobType': '采购/贸易', 'secondJobType': '其他采购/贸易职位',
                  'thirdJobType': '其他采购/贸易类职位'},
                 {'url': '240112', 'firstJobType': '供应链/物流', 'secondJobType': '物流',
                  'thirdJobType': '货运代理经理'},
                 {'url': '240116', 'firstJobType': '供应链/物流', 'secondJobType': '物流', 'thirdJobType': '核销员'},
                 {'url': '240105', 'firstJobType': '供应链/物流', 'secondJobType': '物流', 'thirdJobType': '物流运营'},
                 {'url': '240113', 'firstJobType': '供应链/物流', 'secondJobType': '物流',
                  'thirdJobType': '水/空/陆运操作'},
                 {'url': '240101', 'firstJobType': '供应链/物流', 'secondJobType': '物流',
                  'thirdJobType': '供应链专员'},
                 {'url': '240106', 'firstJobType': '供应链/物流', 'secondJobType': '物流', 'thirdJobType': '物流跟单'},
                 {'url': '240302', 'firstJobType': '供应链/物流', 'secondJobType': '物流',
                  'thirdJobType': '集装箱管理'},
                 {'url': '240108', 'firstJobType': '供应链/物流', 'secondJobType': '物流', 'thirdJobType': '调度员'},
                 {'url': '240111', 'firstJobType': '供应链/物流', 'secondJobType': '物流',
                  'thirdJobType': '货运代理专员'},
                 {'url': '240109', 'firstJobType': '供应链/物流', 'secondJobType': '物流',
                  'thirdJobType': '物流/仓储项目经理'},
                 {'url': '240104', 'firstJobType': '供应链/物流', 'secondJobType': '物流', 'thirdJobType': '物流经理'},
                 {'url': '240103', 'firstJobType': '供应链/物流', 'secondJobType': '物流', 'thirdJobType': '物流专员'},
                 {'url': '240199', 'firstJobType': '供应链/物流', 'secondJobType': '物流', 'thirdJobType': '物流'},
                 {'url': '240102', 'firstJobType': '供应链/物流', 'secondJobType': '物流',
                  'thirdJobType': '供应链经理'},
                 {'url': '240299', 'firstJobType': '供应链/物流', 'secondJobType': '仓储', 'thirdJobType': '仓储'},
                 {'url': '240205', 'firstJobType': '供应链/物流', 'secondJobType': '仓储', 'thirdJobType': '仓库文员'},
                 {'url': '240204', 'firstJobType': '供应链/物流', 'secondJobType': '仓储',
                  'thirdJobType': '仓库管理员'},
                 {'url': '240201', 'firstJobType': '供应链/物流', 'secondJobType': '仓储', 'thirdJobType': '仓库经理'},
                 {'url': '240206', 'firstJobType': '供应链/物流', 'secondJobType': '仓储',
                  'thirdJobType': '配/理/拣/发货'},
                 {'url': '240110', 'firstJobType': '供应链/物流', 'secondJobType': '交通/运输',
                  'thirdJobType': '运输经理/主管'},
                 {'url': '240301', 'firstJobType': '供应链/物流', 'secondJobType': '交通/运输',
                  'thirdJobType': '货运司机'},
                 {'url': '150208', 'firstJobType': '供应链/物流', 'secondJobType': '交通/运输',
                  'thirdJobType': '商务司机'},
                 {'url': '240304', 'firstJobType': '供应链/物流', 'secondJobType': '交通/运输',
                  'thirdJobType': '快递员'},
                 {'url': '240307', 'firstJobType': '供应链/物流', 'secondJobType': '交通/运输',
                  'thirdJobType': '驾校教练'},
                 {'url': '240305', 'firstJobType': '供应链/物流', 'secondJobType': '交通/运输',
                  'thirdJobType': '网约车司机'},
                 {'url': '240303', 'firstJobType': '供应链/物流', 'secondJobType': '交通/运输',
                  'thirdJobType': '配送员'},
                 {'url': '240399', 'firstJobType': '供应链/物流', 'secondJobType': '交通/运输',
                  'thirdJobType': '交通/运输'},
                 {'url': '240306', 'firstJobType': '供应链/物流', 'secondJobType': '交通/运输',
                  'thirdJobType': '代驾司机'},
                 {'url': '240499', 'firstJobType': '供应链/物流', 'secondJobType': '高端供应链职位',
                  'thirdJobType': '高端供应链职位'},
                 {'url': '240402', 'firstJobType': '供应链/物流', 'secondJobType': '高端供应链职位',
                  'thirdJobType': '物流总监'},
                 {'url': '240401', 'firstJobType': '供应链/物流', 'secondJobType': '高端供应链职位',
                  'thirdJobType': '供应链总监'},
                 {'url': '240501', 'firstJobType': '供应链/物流', 'secondJobType': '其他供应链职位',
                  'thirdJobType': '其他供应链职位'},
                 {'url': '220103', 'firstJobType': '房地产/建筑', 'secondJobType': '房地产规划开发',
                  'thirdJobType': '地产招投标'},
                 {'url': '220302', 'firstJobType': '房地产/建筑', 'secondJobType': '房地产规划开发',
                  'thirdJobType': '房产评估师'},
                 {'url': '220101', 'firstJobType': '房地产/建筑', 'secondJobType': '房地产规划开发',
                  'thirdJobType': '房地产策划'},
                 {'url': '220102', 'firstJobType': '房地产/建筑', 'secondJobType': '房地产规划开发',
                  'thirdJobType': '地产项目管理'},
                 {'url': '220199', 'firstJobType': '房地产/建筑', 'secondJobType': '房地产规划开发',
                  'thirdJobType': '房地产规划开发'},
                 {'url': '220224', 'firstJobType': '房地产/建筑', 'secondJobType': '设计装修与市政建设',
                  'thirdJobType': '消防工程师'},
                 {'url': '220206', 'firstJobType': '房地产/建筑', 'secondJobType': '设计装修与市政建设',
                  'thirdJobType': '园林/景观设计'},
                 {'url': '220210', 'firstJobType': '房地产/建筑', 'secondJobType': '设计装修与市政建设',
                  'thirdJobType': '工程预算'},
                 {'url': '220204', 'firstJobType': '房地产/建筑', 'secondJobType': '设计装修与市政建设',
                  'thirdJobType': '土木/土建/结构工程师'},
                 {'url': '220208', 'firstJobType': '房地产/建筑', 'secondJobType': '设计装修与市政建设',
                  'thirdJobType': '工程监理'},
                 {'url': '220223', 'firstJobType': '房地产/建筑', 'secondJobType': '设计装修与市政建设',
                  'thirdJobType': '建筑机电工程师'},
                 {'url': '220222', 'firstJobType': '房地产/建筑', 'secondJobType': '设计装修与市政建设',
                  'thirdJobType': '装修项目经理'},
                 {'url': '220211', 'firstJobType': '房地产/建筑', 'secondJobType': '设计装修与市政建设',
                  'thirdJobType': '资料员'},
                 {'url': '220213', 'firstJobType': '房地产/建筑', 'secondJobType': '设计装修与市政建设',
                  'thirdJobType': '弱电工程师'},
                 {'url': '220207', 'firstJobType': '房地产/建筑', 'secondJobType': '设计装修与市政建设',
                  'thirdJobType': '城市规划设计'},
                 {'url': '220225', 'firstJobType': '房地产/建筑', 'secondJobType': '设计装修与市政建设',
                  'thirdJobType': '施工安全员'},
                 {'url': '220216', 'firstJobType': '房地产/建筑', 'secondJobType': '设计装修与市政建设',
                  'thirdJobType': '幕墙工程师'},
                 {'url': '220209', 'firstJobType': '房地产/建筑', 'secondJobType': '设计装修与市政建设',
                  'thirdJobType': '工程造价'},
                 {'url': '220212', 'firstJobType': '房地产/建筑', 'secondJobType': '设计装修与市政建设',
                  'thirdJobType': '建筑施工现场管理'},
                 {'url': '220221', 'firstJobType': '房地产/建筑', 'secondJobType': '设计装修与市政建设',
                  'thirdJobType': 'BIM工程师'},
                 {'url': '220217', 'firstJobType': '房地产/建筑', 'secondJobType': '设计装修与市政建设',
                  'thirdJobType': '软装设计师'},
                 {'url': '220220', 'firstJobType': '房地产/建筑', 'secondJobType': '设计装修与市政建设',
                  'thirdJobType': '材料员'},
                 {'url': '220299', 'firstJobType': '房地产/建筑', 'secondJobType': '设计装修与市政建设',
                  'thirdJobType': '设计装修与市政建设'},
                 {'url': '220202', 'firstJobType': '房地产/建筑', 'secondJobType': '设计装修与市政建设',
                  'thirdJobType': '建筑工程师'},
                 {'url': '220218', 'firstJobType': '房地产/建筑', 'secondJobType': '设计装修与市政建设',
                  'thirdJobType': '施工员'},
                 {'url': '220203', 'firstJobType': '房地产/建筑', 'secondJobType': '设计装修与市政建设',
                  'thirdJobType': '建筑设计师'},
                 {'url': '220215', 'firstJobType': '房地产/建筑', 'secondJobType': '设计装修与市政建设',
                  'thirdJobType': '暖通工程师'},
                 {'url': '220219', 'firstJobType': '房地产/建筑', 'secondJobType': '设计装修与市政建设',
                  'thirdJobType': '测绘/测量'},
                 {'url': '220205', 'firstJobType': '房地产/建筑', 'secondJobType': '设计装修与市政建设',
                  'thirdJobType': '室内设计'},
                 {'url': '220214', 'firstJobType': '房地产/建筑', 'secondJobType': '设计装修与市政建设',
                  'thirdJobType': '给排水工程师'},
                 {'url': '220405', 'firstJobType': '房地产/建筑', 'secondJobType': '物业管理',
                  'thirdJobType': '绿化工'},
                 {'url': '220404', 'firstJobType': '房地产/建筑', 'secondJobType': '物业管理',
                  'thirdJobType': '物业维修'},
                 {'url': '220401', 'firstJobType': '房地产/建筑', 'secondJobType': '物业管理',
                  'thirdJobType': '物业经理'},
                 {'url': '220406', 'firstJobType': '房地产/建筑', 'secondJobType': '物业管理',
                  'thirdJobType': '物业管理员'},
                 {'url': '220599', 'firstJobType': '房地产/建筑', 'secondJobType': '高端房地产职位',
                  'thirdJobType': '高端房地产职位'},
                 {'url': '220501', 'firstJobType': '房地产/建筑', 'secondJobType': '高端房地产职位',
                  'thirdJobType': '地产项目总监'},
                 {'url': '220502', 'firstJobType': '房地产/建筑', 'secondJobType': '高端房地产职位',
                  'thirdJobType': '地产策划总监'},
                 {'url': '220503', 'firstJobType': '房地产/建筑', 'secondJobType': '高端房地产职位',
                  'thirdJobType': '地产招投标总监'},
                 {'url': '220601', 'firstJobType': '房地产/建筑', 'secondJobType': '其他房地产职位',
                  'thirdJobType': '其他房地产职位'},
                 {'url': '260105', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '咨询/调研',
                  'thirdJobType': '人力资源咨询顾问'},
                 {'url': '260199', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '咨询/调研',
                  'thirdJobType': '咨询/调研'},
                 {'url': '260401', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '咨询/调研',
                  'thirdJobType': '咨询总监'},
                 {'url': '260402', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '咨询/调研',
                  'thirdJobType': '咨询经理'},
                 {'url': '260109', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '咨询/调研',
                  'thirdJobType': '市场调研'},
                 {'url': '260113', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '咨询/调研',
                  'thirdJobType': '婚恋咨询师'},
                 {'url': '260101', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '咨询/调研',
                  'thirdJobType': '企业管理咨询'},
                 {'url': '260106', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '咨询/调研',
                  'thirdJobType': '咨询项目管理'},
                 {'url': '260103', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '咨询/调研',
                  'thirdJobType': '财务咨询顾问'},
                 {'url': '260112', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '咨询/调研',
                  'thirdJobType': '心理咨询师'},
                 {'url': '260110', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '咨询/调研',
                  'thirdJobType': '其他咨询顾问'},
                 {'url': '260107', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '咨询/调研',
                  'thirdJobType': '战略咨询'},
                 {'url': '260102', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '咨询/调研',
                  'thirdJobType': '数据分析师'},
                 {'url': '260111', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '咨询/调研',
                  'thirdJobType': '知识产权/专利/商标代理人'},
                 {'url': '260108', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '咨询/调研',
                  'thirdJobType': '猎头顾问'},
                 {'url': '260104', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '咨询/调研',
                  'thirdJobType': 'IT咨询顾问'},
                 {'url': '260203', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '律师',
                  'thirdJobType': '知识产权律师'},
                 {'url': '150503', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '律师',
                  'thirdJobType': '专利律师'},
                 {'url': '260202', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '律师', 'thirdJobType': '法务'},
                 {'url': '260201', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '律师',
                  'thirdJobType': '事务所律师'},
                 {'url': '260204', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '律师',
                  'thirdJobType': '律师助理'},
                 {'url': '260307', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '翻译',
                  'thirdJobType': '西班牙语翻译'},
                 {'url': '260306', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '翻译',
                  'thirdJobType': '俄语翻译'},
                 {'url': '260308', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '翻译',
                  'thirdJobType': '其他语种翻译'},
                 {'url': '260305', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '翻译',
                  'thirdJobType': '德语翻译'},
                 {'url': '260303', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '翻译',
                  'thirdJobType': '韩语/朝鲜语翻译'},
                 {'url': '260302', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '翻译',
                  'thirdJobType': '日语翻译'},
                 {'url': '260301', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '翻译',
                  'thirdJobType': '英语翻译'},
                 {'url': '260304', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '翻译',
                  'thirdJobType': '法语翻译'},
                 {'url': '260501', 'firstJobType': '咨询/翻译/法律', 'secondJobType': '其他咨询类职位',
                  'thirdJobType': '其他咨询/翻译类职位'},
                 {'url': '280105', 'firstJobType': '旅游', 'secondJobType': '旅游服务', 'thirdJobType': '预定票务'},
                 {'url': '280101', 'firstJobType': '旅游', 'secondJobType': '旅游服务', 'thirdJobType': '计调'},
                 {'url': '280104', 'firstJobType': '旅游', 'secondJobType': '旅游服务', 'thirdJobType': '导游'},
                 {'url': '280102', 'firstJobType': '旅游', 'secondJobType': '旅游服务', 'thirdJobType': '签证专员'},
                 {'url': '280199', 'firstJobType': '旅游', 'secondJobType': '旅游服务', 'thirdJobType': '旅游服务'},
                 {'url': '280106', 'firstJobType': '旅游', 'secondJobType': '旅游服务', 'thirdJobType': '讲解员'},
                 {'url': '280299', 'firstJobType': '旅游', 'secondJobType': '旅游产品开发/策划',
                  'thirdJobType': '旅游产品开发/策划'},
                 {'url': '280201', 'firstJobType': '旅游', 'secondJobType': '旅游产品开发/策划',
                  'thirdJobType': '旅游产品经理'},
                 {'url': '280202', 'firstJobType': '旅游', 'secondJobType': '旅游产品开发/策划',
                  'thirdJobType': '旅游策划师'},
                 {'url': '280301', 'firstJobType': '旅游', 'secondJobType': '其他旅游职位',
                  'thirdJobType': '其他旅游职位'},
                 {'url': '290203', 'firstJobType': '服务业', 'secondJobType': '餐饮', 'thirdJobType': '厨师'},
                 {'url': '290210', 'firstJobType': '服务业', 'secondJobType': '餐饮', 'thirdJobType': '茶艺师'},
                 {'url': '290212', 'firstJobType': '服务业', 'secondJobType': '餐饮', 'thirdJobType': '餐饮学徒'},
                 {'url': '290207', 'firstJobType': '服务业', 'secondJobType': '餐饮', 'thirdJobType': '领班'},
                 {'url': '290299', 'firstJobType': '服务业', 'secondJobType': '餐饮', 'thirdJobType': '餐饮'},
                 {'url': '290222', 'firstJobType': '服务业', 'secondJobType': '餐饮', 'thirdJobType': '烧烤师傅'},
                 {'url': '290202', 'firstJobType': '服务业', 'secondJobType': '餐饮', 'thirdJobType': '服务员'},
                 {'url': '290220', 'firstJobType': '服务业', 'secondJobType': '餐饮', 'thirdJobType': '西餐厨师'},
                 {'url': '290204', 'firstJobType': '服务业', 'secondJobType': '餐饮', 'thirdJobType': '咖啡师'},
                 {'url': '290218', 'firstJobType': '服务业', 'secondJobType': '餐饮', 'thirdJobType': '凉菜厨师'},
                 {'url': '290216', 'firstJobType': '服务业', 'secondJobType': '餐饮', 'thirdJobType': '传菜员'},
                 {'url': '290215', 'firstJobType': '服务业', 'secondJobType': '餐饮', 'thirdJobType': '厨师长'},
                 {'url': '290217', 'firstJobType': '服务业', 'secondJobType': '餐饮', 'thirdJobType': '洗碗工'},
                 {'url': '290205', 'firstJobType': '服务业', 'secondJobType': '餐饮', 'thirdJobType': '送餐员'},
                 {'url': '290219', 'firstJobType': '服务业', 'secondJobType': '餐饮', 'thirdJobType': '中餐厨师'},
                 {'url': '290221', 'firstJobType': '服务业', 'secondJobType': '餐饮', 'thirdJobType': '日料厨师'},
                 {'url': '290209', 'firstJobType': '服务业', 'secondJobType': '餐饮', 'thirdJobType': '配菜打荷'},
                 {'url': '290208', 'firstJobType': '服务业', 'secondJobType': '餐饮', 'thirdJobType': '后厨'},
                 {'url': '290206', 'firstJobType': '服务业', 'secondJobType': '餐饮', 'thirdJobType': '餐饮店长'},
                 {'url': '290201', 'firstJobType': '服务业', 'secondJobType': '餐饮', 'thirdJobType': '收银'},
                 {'url': '290214', 'firstJobType': '服务业', 'secondJobType': '餐饮', 'thirdJobType': '行政总厨'},
                 {'url': '290211', 'firstJobType': '服务业', 'secondJobType': '餐饮', 'thirdJobType': '西点师'},
                 {'url': '290213', 'firstJobType': '服务业', 'secondJobType': '餐饮', 'thirdJobType': '面点师'},
                 {'url': '290115', 'firstJobType': '服务业', 'secondJobType': '酒店', 'thirdJobType': '前厅经理'},
                 {'url': '290103', 'firstJobType': '服务业', 'secondJobType': '酒店', 'thirdJobType': '客房服务员'},
                 {'url': '290104', 'firstJobType': '服务业', 'secondJobType': '酒店', 'thirdJobType': '酒店经理'},
                 {'url': '290107', 'firstJobType': '服务业', 'secondJobType': '酒店', 'thirdJobType': '礼仪/迎宾/接待'},
                 {'url': '290101', 'firstJobType': '服务业', 'secondJobType': '酒店', 'thirdJobType': '收银'},
                 {'url': '290102', 'firstJobType': '服务业', 'secondJobType': '酒店', 'thirdJobType': '酒店前台'},
                 {'url': '290116', 'firstJobType': '服务业', 'secondJobType': '酒店', 'thirdJobType': '客房经理'},
                 {'url': '290304', 'firstJobType': '服务业', 'secondJobType': '零售', 'thirdJobType': '门店店长'},
                 {'url': '290311', 'firstJobType': '服务业', 'secondJobType': '零售', 'thirdJobType': '促销员'},
                 {'url': '290307', 'firstJobType': '服务业', 'secondJobType': '零售', 'thirdJobType': '理货员'},
                 {'url': '290301', 'firstJobType': '服务业', 'secondJobType': '零售', 'thirdJobType': '收银'},
                 {'url': '290306', 'firstJobType': '服务业', 'secondJobType': '零售', 'thirdJobType': '陈列员'},
                 {'url': '290309', 'firstJobType': '服务业', 'secondJobType': '零售', 'thirdJobType': '卖场经理'},
                 {'url': '290308', 'firstJobType': '服务业', 'secondJobType': '零售', 'thirdJobType': '防损员'},
                 {'url': '290302', 'firstJobType': '服务业', 'secondJobType': '零售', 'thirdJobType': '导购'},
                 {'url': '290303', 'firstJobType': '服务业', 'secondJobType': '零售', 'thirdJobType': '店员/营业员'},
                 {'url': '290305', 'firstJobType': '服务业', 'secondJobType': '零售', 'thirdJobType': '督导/巡店'},
                 {'url': '210407', 'firstJobType': '服务业', 'secondJobType': '美容保健', 'thirdJobType': '纹绣师'},
                 {'url': '210607', 'firstJobType': '服务业', 'secondJobType': '美容保健', 'thirdJobType': '发型师'},
                 {'url': '210411', 'firstJobType': '服务业', 'secondJobType': '美容保健', 'thirdJobType': '足疗师'},
                 {'url': '210412', 'firstJobType': '服务业', 'secondJobType': '美容保健', 'thirdJobType': '按摩师'},
                 {'url': '210413', 'firstJobType': '服务业', 'secondJobType': '美容保健', 'thirdJobType': '美睫师'},
                 {'url': '210409', 'firstJobType': '服务业', 'secondJobType': '美容保健', 'thirdJobType': '美发学徒'},
                 {'url': '210405', 'firstJobType': '服务业', 'secondJobType': '美容保健', 'thirdJobType': '美容师'},
                 {'url': '210609', 'firstJobType': '服务业', 'secondJobType': '美容保健', 'thirdJobType': '化妆师'},
                 {'url': '210608', 'firstJobType': '服务业', 'secondJobType': '美容保健', 'thirdJobType': '美甲师'},
                 {'url': '210410', 'firstJobType': '服务业', 'secondJobType': '美容保健', 'thirdJobType': '美容店长'},
                 {'url': '290801', 'firstJobType': '服务业', 'secondJobType': '美容保健', 'thirdJobType': '养发师'},
                 {'url': '210408', 'firstJobType': '服务业', 'secondJobType': '美容保健', 'thirdJobType': '美体师'},
                 {'url': '210601', 'firstJobType': '服务业', 'secondJobType': '运动健身', 'thirdJobType': '瑜伽老师'},
                 {'url': '210605', 'firstJobType': '服务业', 'secondJobType': '运动健身', 'thirdJobType': '舞蹈老师'},
                 {'url': '210603', 'firstJobType': '服务业', 'secondJobType': '运动健身', 'thirdJobType': '游泳教练'},
                 {'url': '210699', 'firstJobType': '服务业', 'secondJobType': '运动健身', 'thirdJobType': '健身'},
                 {'url': '210613', 'firstJobType': '服务业', 'secondJobType': '运动健身', 'thirdJobType': '救生员'},
                 {'url': '210606', 'firstJobType': '服务业', 'secondJobType': '运动健身', 'thirdJobType': '健身教练'},
                 {'url': '210604', 'firstJobType': '服务业', 'secondJobType': '运动健身', 'thirdJobType': '美体教练'},
                 {'url': '290701', 'firstJobType': '服务业', 'secondJobType': '婚礼/花艺', 'thirdJobType': '花艺师'},
                 {'url': '290702', 'firstJobType': '服务业', 'secondJobType': '婚礼/花艺', 'thirdJobType': '婚礼策划'},
                 {'url': '290601', 'firstJobType': '服务业', 'secondJobType': '宠物服务', 'thirdJobType': '宠物美容'},
                 {'url': '290602', 'firstJobType': '服务业', 'secondJobType': '宠物服务', 'thirdJobType': '宠物医生'},
                 {'url': '290105', 'firstJobType': '服务业', 'secondJobType': '安保/家政/维修', 'thirdJobType': '保安'},
                 {'url': '290113', 'firstJobType': '服务业', 'secondJobType': '安保/家政/维修',
                  'thirdJobType': '手机维修'},
                 {'url': '290119', 'firstJobType': '服务业', 'secondJobType': '安保/家政/维修',
                  'thirdJobType': '钟点工'},
                 {'url': '290109', 'firstJobType': '服务业', 'secondJobType': '安保/家政/维修', 'thirdJobType': '月嫂'},
                 {'url': '290108', 'firstJobType': '服务业', 'secondJobType': '安保/家政/维修', 'thirdJobType': '保姆'},
                 {'url': '290120', 'firstJobType': '服务业', 'secondJobType': '安保/家政/维修',
                  'thirdJobType': '押运员'},
                 {'url': '290110', 'firstJobType': '服务业', 'secondJobType': '安保/家政/维修',
                  'thirdJobType': '育婴师'},
                 {'url': '290112', 'firstJobType': '服务业', 'secondJobType': '安保/家政/维修',
                  'thirdJobType': '地铁安检'},
                 {'url': '290118', 'firstJobType': '服务业', 'secondJobType': '安保/家政/维修',
                  'thirdJobType': '产后康复师'},
                 {'url': '290106', 'firstJobType': '服务业', 'secondJobType': '安保/家政/维修', 'thirdJobType': '保洁'},
                 {'url': '290111', 'firstJobType': '服务业', 'secondJobType': '安保/家政/维修', 'thirdJobType': '护工'},
                 {'url': '290114', 'firstJobType': '服务业', 'secondJobType': '安保/家政/维修',
                  'thirdJobType': '家电维修'},
                 {'url': '290117', 'firstJobType': '服务业', 'secondJobType': '安保/家政/维修',
                  'thirdJobType': '保安经理'},
                 {'url': '290121', 'firstJobType': '服务业', 'secondJobType': '安保/家政/维修',
                  'thirdJobType': '消防中控员'},
                 {'url': '290122', 'firstJobType': '服务业', 'secondJobType': '安保/家政/维修',
                  'thirdJobType': '保洁经理'},
                 {'url': '290401', 'firstJobType': '服务业', 'secondJobType': '其他服务业职位',
                  'thirdJobType': '其他服务业职位'},
                 {'url': '300101', 'firstJobType': '生产制造', 'secondJobType': '生产营运', 'thirdJobType': '厂长'},
                 {'url': '300106', 'firstJobType': '生产制造', 'secondJobType': '生产营运',
                  'thirdJobType': '生产设备管理'},
                 {'url': '300103', 'firstJobType': '生产制造', 'secondJobType': '生产营运', 'thirdJobType': '车间主任'},
                 {'url': '300107', 'firstJobType': '生产制造', 'secondJobType': '生产营运',
                  'thirdJobType': '生产计划管理'},
                 {'url': '300108', 'firstJobType': '生产制造', 'secondJobType': '生产营运', 'thirdJobType': '生产跟单'},
                 {'url': '300105', 'firstJobType': '生产制造', 'secondJobType': '生产营运', 'thirdJobType': '生产员'},
                 {'url': '300102', 'firstJobType': '生产制造', 'secondJobType': '生产营运', 'thirdJobType': '生产总监'},
                 {'url': '300104', 'firstJobType': '生产制造', 'secondJobType': '生产营运',
                  'thirdJobType': '生产组长/拉长'},
                 {'url': '300199', 'firstJobType': '生产制造', 'secondJobType': '生产营运', 'thirdJobType': '生产营运'},
                 {'url': '300207', 'firstJobType': '生产制造', 'secondJobType': '质量安全',
                  'thirdJobType': '生产安全员'},
                 {'url': '300201', 'firstJobType': '生产制造', 'secondJobType': '质量安全',
                  'thirdJobType': '质量管理/测试'},
                 {'url': '300208', 'firstJobType': '生产制造', 'secondJobType': '质量安全', 'thirdJobType': '质检员'},
                 {'url': '300206', 'firstJobType': '生产制造', 'secondJobType': '质量安全', 'thirdJobType': '审核员'},
                 {'url': '300202', 'firstJobType': '生产制造', 'secondJobType': '质量安全',
                  'thirdJobType': '可靠度工程师'},
                 {'url': '300205', 'firstJobType': '生产制造', 'secondJobType': '质量安全',
                  'thirdJobType': '体系工程师'},
                 {'url': '300204', 'firstJobType': '生产制造', 'secondJobType': '质量安全',
                  'thirdJobType': '认证工程师'},
                 {'url': '230109', 'firstJobType': '生产制造', 'secondJobType': '质量安全',
                  'thirdJobType': '汽车质量工程师'},
                 {'url': '300203', 'firstJobType': '生产制造', 'secondJobType': '质量安全',
                  'thirdJobType': '故障分析师'},
                 {'url': '300801', 'firstJobType': '生产制造', 'secondJobType': '新能源', 'thirdJobType': '电池工程师'},
                 {'url': '300803', 'firstJobType': '生产制造', 'secondJobType': '新能源', 'thirdJobType': '线束设计'},
                 {'url': '300802', 'firstJobType': '生产制造', 'secondJobType': '新能源', 'thirdJobType': '电机工程师'},
                 {'url': '300804', 'firstJobType': '生产制造', 'secondJobType': '新能源', 'thirdJobType': '充电桩设计'},
                 {'url': '230210', 'firstJobType': '生产制造', 'secondJobType': '汽车制造',
                  'thirdJobType': '总装工程师'},
                 {'url': '230103', 'firstJobType': '生产制造', 'secondJobType': '汽车制造',
                  'thirdJobType': '底盘工程师'},
                 {'url': '230105', 'firstJobType': '生产制造', 'secondJobType': '汽车制造',
                  'thirdJobType': '动力系统工程师'},
                 {'url': '230106', 'firstJobType': '生产制造', 'secondJobType': '汽车制造',
                  'thirdJobType': '汽车电子工程师'},
                 {'url': '230107', 'firstJobType': '生产制造', 'secondJobType': '汽车制造',
                  'thirdJobType': '汽车零部件设计'},
                 {'url': '230108', 'firstJobType': '生产制造', 'secondJobType': '汽车制造',
                  'thirdJobType': '汽车项目管理'},
                 {'url': '230110', 'firstJobType': '生产制造', 'secondJobType': '汽车制造',
                  'thirdJobType': '内外饰设计工程师'},
                 {'url': '230102', 'firstJobType': '生产制造', 'secondJobType': '汽车制造',
                  'thirdJobType': '车身/造型设计'},
                 {'url': '230101', 'firstJobType': '生产制造', 'secondJobType': '汽车制造', 'thirdJobType': '汽车设计'},
                 {'url': '230204', 'firstJobType': '生产制造', 'secondJobType': '汽车服务', 'thirdJobType': '汽车维修'},
                 {'url': '230203', 'firstJobType': '生产制造', 'secondJobType': '汽车服务',
                  'thirdJobType': '汽车服务顾问'},
                 {'url': '230205', 'firstJobType': '生产制造', 'secondJobType': '汽车服务', 'thirdJobType': '汽车美容'},
                 {'url': '230206', 'firstJobType': '生产制造', 'secondJobType': '汽车服务',
                  'thirdJobType': '汽车定损理赔'},
                 {'url': '230208', 'firstJobType': '生产制造', 'secondJobType': '汽车服务',
                  'thirdJobType': '4S店店长/维修站长'},
                 {'url': '230207', 'firstJobType': '生产制造', 'secondJobType': '汽车服务',
                  'thirdJobType': '二手车评估师'},
                 {'url': '230209', 'firstJobType': '生产制造', 'secondJobType': '汽车服务',
                  'thirdJobType': '汽车改装工程师'},
                 {'url': '300305', 'firstJobType': '生产制造', 'secondJobType': '机械设计/制造',
                  'thirdJobType': '机械制图'},
                 {'url': '300303', 'firstJobType': '生产制造', 'secondJobType': '机械设计/制造',
                  'thirdJobType': '机械设备工程师'},
                 {'url': '300307', 'firstJobType': '生产制造', 'secondJobType': '机械设计/制造',
                  'thirdJobType': '工业工程师'},
                 {'url': '300309', 'firstJobType': '生产制造', 'secondJobType': '机械设计/制造',
                  'thirdJobType': '材料工程师'},
                 {'url': '300302', 'firstJobType': '生产制造', 'secondJobType': '机械设计/制造',
                  'thirdJobType': '机械设计师'},
                 {'url': '300317', 'firstJobType': '生产制造', 'secondJobType': '机械设计/制造',
                  'thirdJobType': '铸造/锻造工程师'},
                 {'url': '300308', 'firstJobType': '生产制造', 'secondJobType': '机械设计/制造',
                  'thirdJobType': '工艺/制程工程师'},
                 {'url': '300312', 'firstJobType': '生产制造', 'secondJobType': '机械设计/制造',
                  'thirdJobType': '冲压工程师'},
                 {'url': '300304', 'firstJobType': '生产制造', 'secondJobType': '机械设计/制造',
                  'thirdJobType': '机械维修/保养'},
                 {'url': '300315', 'firstJobType': '生产制造', 'secondJobType': '机械设计/制造',
                  'thirdJobType': '焊接工程师'},
                 {'url': '300314', 'firstJobType': '生产制造', 'secondJobType': '机械设计/制造',
                  'thirdJobType': '模具工程师'},
                 {'url': '300306', 'firstJobType': '生产制造', 'secondJobType': '机械设计/制造',
                  'thirdJobType': '机械结构工程师'},
                 {'url': '300310', 'firstJobType': '生产制造', 'secondJobType': '机械设计/制造',
                  'thirdJobType': '机电工程师'},
                 {'url': '300316', 'firstJobType': '生产制造', 'secondJobType': '机械设计/制造',
                  'thirdJobType': '注塑工程师'},
                 {'url': '300399', 'firstJobType': '生产制造', 'secondJobType': '机械设计/制造',
                  'thirdJobType': '机械设计/制造'},
                 {'url': '300311', 'firstJobType': '生产制造', 'secondJobType': '机械设计/制造',
                  'thirdJobType': 'CNC/数控'},
                 {'url': '300301', 'firstJobType': '生产制造', 'secondJobType': '机械设计/制造',
                  'thirdJobType': '机械工程师'},
                 {'url': '100815', 'firstJobType': '生产制造', 'secondJobType': '机械设计/制造',
                  'thirdJobType': '精益工程师'},
                 {'url': '100813', 'firstJobType': '生产制造', 'secondJobType': '机械设计/制造',
                  'thirdJobType': '热设计工程师'},
                 {'url': '300313', 'firstJobType': '生产制造', 'secondJobType': '机械设计/制造',
                  'thirdJobType': '夹具工程师'},
                 {'url': '300403', 'firstJobType': '生产制造', 'secondJobType': '化工', 'thirdJobType': '化学分析'},
                 {'url': '300405', 'firstJobType': '生产制造', 'secondJobType': '化工', 'thirdJobType': '化妆品研发'},
                 {'url': '300404', 'firstJobType': '生产制造', 'secondJobType': '化工', 'thirdJobType': '涂料研发'},
                 {'url': '300401', 'firstJobType': '生产制造', 'secondJobType': '化工', 'thirdJobType': '化工工程师'},
                 {'url': '300407', 'firstJobType': '生产制造', 'secondJobType': '化工', 'thirdJobType': '化工项目经理'},
                 {'url': '300406', 'firstJobType': '生产制造', 'secondJobType': '化工',
                  'thirdJobType': '食品/饮料研发'},
                 {'url': '300402', 'firstJobType': '生产制造', 'secondJobType': '化工', 'thirdJobType': '实验室技术员'},
                 {'url': '300507', 'firstJobType': '生产制造', 'secondJobType': '服装/纺织/皮革',
                  'thirdJobType': '面料辅料开发'},
                 {'url': '300509', 'firstJobType': '生产制造', 'secondJobType': '服装/纺织/皮革',
                  'thirdJobType': '打样/制版'},
                 {'url': '300501', 'firstJobType': '生产制造', 'secondJobType': '服装/纺织/皮革',
                  'thirdJobType': '服装/纺织设计'},
                 {'url': '300510', 'firstJobType': '生产制造', 'secondJobType': '服装/纺织/皮革',
                  'thirdJobType': '服装/纺织/皮革跟单'},
                 {'url': '300633', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '模具工'},
                 {'url': '300630', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '搬运工'},
                 {'url': '300603', 'firstJobType': '生产制造', 'secondJobType': '技工/普工',
                  'thirdJobType': '铲车司机'},
                 {'url': '300613', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '钳工'},
                 {'url': '300617', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '抛光工'},
                 {'url': '300628', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '学徒工'},
                 {'url': '300619', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '折弯工'},
                 {'url': '300604', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '焊工'},
                 {'url': '300602', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '叉车工'},
                 {'url': '300605', 'firstJobType': '生产制造', 'secondJobType': '技工/普工',
                  'thirdJobType': '氩弧焊工'},
                 {'url': '300627', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '锅炉工'},
                 {'url': '300614', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '钻工'},
                 {'url': '300618', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '机修工'},
                 {'url': '300624', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '包装工'},
                 {'url': '300622', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '注塑工'},
                 {'url': '300601', 'firstJobType': '生产制造', 'secondJobType': '技工/普工',
                  'thirdJobType': '普工/操作工'},
                 {'url': '300621', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '喷塑工'},
                 {'url': '300625', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '空调工'},
                 {'url': '300626', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '电梯工'},
                 {'url': '300610', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '车工'},
                 {'url': '300631', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '切割工'},
                 {'url': '300606', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '电工'},
                 {'url': '300611', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '磨工'},
                 {'url': '300616', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '钣金工'},
                 {'url': '300609', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '油漆工'},
                 {'url': '300623', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '组装工'},
                 {'url': '300629', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '缝纫工'},
                 {'url': '300615', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '铆工'},
                 {'url': '300632', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '样衣工'},
                 {'url': '300608', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '木工'},
                 {'url': '300612', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '铣工'},
                 {'url': '300620', 'firstJobType': '生产制造', 'secondJobType': '技工/普工', 'thirdJobType': '电镀工'},
                 {'url': '300701', 'firstJobType': '生产制造', 'secondJobType': '其他生产制造职位',
                  'thirdJobType': '其他生产制造职位'}]
Location_dict = [{'city': '北京', 'city_id': '101010100'}, {'city': '广州', 'city_id': '101280100'},
                 {'city': '杭州', 'city_id': '101210100'}, {'city': '上海', 'city_id': '101020100'},
                 {'city': '深圳', 'city_id': '101280600'}, {'city': '重庆', 'city_id': '101040100'},
                 {'city': '长沙', 'city_id': '101250100'}, {'city': '成都', 'city_id': '101270100'},
                 {'city': '佛山', 'city_id': '101280800'}, {'city': '合肥', 'city_id': '101220100'},
                 {'city': '济南', 'city_id': '101120100'}, {'city': '南京', 'city_id': '101190100'},
                 {'city': '宁波', 'city_id': '101210400'}, {'city': '沈阳', 'city_id': '101070100'},
                 {'city': '苏州', 'city_id': '101190400'}, {'city': '天津', 'city_id': '101030100'},
                 {'city': '武汉', 'city_id': '101200100'}, {'city': '西安', 'city_id': '101110100'},
                 {'city': '厦门', 'city_id': '101230200'}, {'city': '郑州', 'city_id': '101180100'},
                 {'city': '鞍山', 'city_id': '101070300'}, {'city': '安康', 'city_id': '101110700'},
                 {'city': '安阳', 'city_id': '101180200'}, {'city': '安庆', 'city_id': '101220600'},
                 {'city': '安顺', 'city_id': '101260300'}, {'city': '澳门', 'city_id': '101330100'},
                 {'city': '阿拉善盟', 'city_id': '101081200'}, {'city': '阿里地区', 'city_id': '101140700'},
                 {'city': '阿克苏', 'city_id': '101131000'}, {'city': '阿勒泰', 'city_id': '101131500'},
                 {'city': '阿拉尔', 'city_id': '101131700'}, {'city': '白城', 'city_id': '101060500'},
                 {'city': '白山', 'city_id': '101060800'}, {'city': '本溪', 'city_id': '101070500'},
                 {'city': '包头', 'city_id': '101080200'}, {'city': '巴彦淖尔', 'city_id': '101080800'},
                 {'city': '保定', 'city_id': '101090200'}, {'city': '宝鸡', 'city_id': '101110900'},
                 {'city': '滨州', 'city_id': '101121100'}, {'city': '白银', 'city_id': '101161000'},
                 {'city': '蚌埠', 'city_id': '101220200'}, {'city': '亳州', 'city_id': '101220900'},
                 {'city': '毕节', 'city_id': '101260500'}, {'city': '巴中', 'city_id': '101270900'},
                 {'city': '保山', 'city_id': '101290300'}, {'city': '百色', 'city_id': '101301000'},
                 {'city': '北海', 'city_id': '101301300'}, {'city': '巴音郭楞蒙古自治州', 'city_id': '101130400'},
                 {'city': '博尔塔拉蒙古自治州', 'city_id': '101130500'},
                 {'city': '白沙黎族自治县', 'city_id': '101311400'},
                 {'city': '保亭黎族苗族自治县', 'city_id': '101311800'}, {'city': '北屯市', 'city_id': '101132100'},
                 {'city': '朝阳', 'city_id': '101071200'}, {'city': '赤峰', 'city_id': '101080500'},
                 {'city': '承德', 'city_id': '101090400'}, {'city': '沧州', 'city_id': '101090700'},
                 {'city': '长治', 'city_id': '101100500'}, {'city': '滁州', 'city_id': '101221000'},
                 {'city': '池州', 'city_id': '101221500'}, {'city': '郴州', 'city_id': '101250500'},
                 {'city': '常德', 'city_id': '101250600'}, {'city': '潮州', 'city_id': '101281500'},
                 {'city': '崇左', 'city_id': '101300200'}, {'city': '楚雄彝族自治州', 'city_id': '101291700'},
                 {'city': '昌吉回族自治州', 'city_id': '101130300'}, {'city': '澄迈', 'city_id': '101311200'},
                 {'city': '昌江黎族自治县', 'city_id': '101311500'}, {'city': '昌都', 'city_id': '101140300'},
                 {'city': '大庆', 'city_id': '101050800'}, {'city': '丹东', 'city_id': '101070600'},
                 {'city': '大同', 'city_id': '101100200'}, {'city': '德州', 'city_id': '101120400'},
                 {'city': '东营', 'city_id': '101121200'}, {'city': '定西', 'city_id': '101160200'},
                 {'city': '达州', 'city_id': '101270600'}, {'city': '德阳', 'city_id': '101271700'},
                 {'city': '德宏傣族景颇族自治州', 'city_id': '101291300'},
                 {'city': '迪庆藏族自治州', 'city_id': '101291500'},
                 {'city': '大理白族自治州', 'city_id': '101291600'}, {'city': '大兴安岭', 'city_id': '101051300'},
                 {'city': '儋州', 'city_id': '101310400'}, {'city': '东方', 'city_id': '101310900'},
                 {'city': '定安', 'city_id': '101311000'}, {'city': '东沙群岛', 'city_id': '101282200'},
                 {'city': '鄂尔多斯', 'city_id': '101080600'}, {'city': '鄂州', 'city_id': '101200300'},
                 {'city': '恩施土家族苗族自治州', 'city_id': '101201300'},
                 {'city': '阿坝藏族羌族自治州', 'city_id': '101271900'},
                 {'city': '抚顺', 'city_id': '101070400'}, {'city': '阜新', 'city_id': '101070900'},
                 {'city': '阜阳', 'city_id': '101220800'}, {'city': '抚州', 'city_id': '101240400'},
                 {'city': '防城港', 'city_id': '101301400'}, {'city': '固原', 'city_id': '101170400'},
                 {'city': '赣州', 'city_id': '101240700'}, {'city': '广安', 'city_id': '101270800'},
                 {'city': '广元', 'city_id': '101271800'}, {'city': '桂林', 'city_id': '101300500'},
                 {'city': '贵港', 'city_id': '101300800'}, {'city': '甘孜藏族自治州', 'city_id': '101272100'},
                 {'city': '甘南藏族自治州', 'city_id': '101161400'}, {'city': '果洛藏族自治州', 'city_id': '101150600'},
                 {'city': '黑河', 'city_id': '101050600'}, {'city': '鹤岗', 'city_id': '101051100'},
                 {'city': '葫芦岛', 'city_id': '101071400'}, {'city': '呼和浩特', 'city_id': '101080100'},
                 {'city': '呼伦贝尔', 'city_id': '101080700'}, {'city': '衡水', 'city_id': '101090800'},
                 {'city': '邯郸', 'city_id': '101091000'}, {'city': '汉中', 'city_id': '101110800'},
                 {'city': '菏泽', 'city_id': '101121000'}, {'city': '海东', 'city_id': '101150200'},
                 {'city': '鹤壁', 'city_id': '101181200'}, {'city': '淮安', 'city_id': '101190900'},
                 {'city': '黄冈', 'city_id': '101200500'}, {'city': '黄石', 'city_id': '101200600'},
                 {'city': '湖州', 'city_id': '101210200'}, {'city': '淮南', 'city_id': '101220400'},
                 {'city': '淮北', 'city_id': '101221100'}, {'city': '黄山', 'city_id': '101221600'},
                 {'city': '衡阳', 'city_id': '101250400'}, {'city': '怀化', 'city_id': '101251200'},
                 {'city': '河源', 'city_id': '101281200'}, {'city': '贺州', 'city_id': '101300700'},
                 {'city': '河池', 'city_id': '101301200'}, {'city': '海口', 'city_id': '101310100'},
                 {'city': '红河哈尼族彝族自治州', 'city_id': '101291200'},
                 {'city': '海北藏族自治州', 'city_id': '101150300'},
                 {'city': '黄南藏族自治州', 'city_id': '101150400'}, {'city': '海南藏族自治州', 'city_id': '101150500'},
                 {'city': '海西蒙古族藏族自治州', 'city_id': '101150800'}, {'city': '哈密', 'city_id': '101130900'},
                 {'city': '和田', 'city_id': '101131300'}, {'city': '佳木斯', 'city_id': '101050400'},
                 {'city': '鸡西', 'city_id': '101051000'}, {'city': '吉林', 'city_id': '101060200'},
                 {'city': '锦州', 'city_id': '101070700'}, {'city': '晋中', 'city_id': '101100400'},
                 {'city': '晋城', 'city_id': '101100600'}, {'city': '济宁', 'city_id': '101120700'},
                 {'city': '金昌', 'city_id': '101160600'}, {'city': '酒泉', 'city_id': '101160800'},
                 {'city': '嘉峪关', 'city_id': '101161200'}, {'city': '焦作', 'city_id': '101181100'},
                 {'city': '荆州', 'city_id': '101200800'}, {'city': '荆门', 'city_id': '101201200'},
                 {'city': '九江', 'city_id': '101240200'}, {'city': '吉安', 'city_id': '101240600'},
                 {'city': '景德镇', 'city_id': '101240800'}, {'city': '江门', 'city_id': '101281100'},
                 {'city': '揭阳', 'city_id': '101281900'}, {'city': '济源', 'city_id': '101181800'},
                 {'city': '克拉玛依', 'city_id': '101130200'}, {'city': '开封', 'city_id': '101180800'},
                 {'city': '克孜勒苏柯尔克孜自治州', 'city_id': '101131100'}, {'city': '喀什', 'city_id': '101131200'},
                 {'city': '可克达拉市', 'city_id': '101132200'}, {'city': '昆玉市', 'city_id': '101132300'},
                 {'city': '辽源', 'city_id': '101060600'}, {'city': '辽阳', 'city_id': '101071000'},
                 {'city': '廊坊', 'city_id': '101090600'}, {'city': '临汾', 'city_id': '101100700'},
                 {'city': '吕梁', 'city_id': '101101100'}, {'city': '临沂', 'city_id': '101120900'},
                 {'city': '聊城', 'city_id': '101121700'}, {'city': '拉萨', 'city_id': '101140100'},
                 {'city': '兰州', 'city_id': '101160100'}, {'city': '陇南', 'city_id': '101161100'},
                 {'city': '洛阳', 'city_id': '101180900'}, {'city': '漯河', 'city_id': '101181500'},
                 {'city': '连云港', 'city_id': '101191000'}, {'city': '丽水', 'city_id': '101210800'},
                 {'city': '六安', 'city_id': '101221400'}, {'city': '龙岩', 'city_id': '101230700'},
                 {'city': '娄底', 'city_id': '101250800'}, {'city': '六盘水', 'city_id': '101260600'},
                 {'city': '泸州', 'city_id': '101271000'}, {'city': '乐山', 'city_id': '101271400'},
                 {'city': '临沧', 'city_id': '101290800'}, {'city': '丽江', 'city_id': '101290900'},
                 {'city': '柳州', 'city_id': '101300300'}, {'city': '来宾', 'city_id': '101300400'},
                 {'city': '凉山彝族自治州', 'city_id': '101272000'}, {'city': '临夏回族自治州', 'city_id': '101161300'},
                 {'city': '临高', 'city_id': '101311300'}, {'city': '乐东黎族自治县', 'city_id': '101311600'},
                 {'city': '陵水黎族自治县', 'city_id': '101311700'}, {'city': '林芝', 'city_id': '101140400'},
                 {'city': '牡丹江', 'city_id': '101050300'}, {'city': '马鞍山', 'city_id': '101220500'},
                 {'city': '绵阳', 'city_id': '101270400'}, {'city': '眉山', 'city_id': '101271500'},
                 {'city': '梅州', 'city_id': '101280400'}, {'city': '茂名', 'city_id': '101282000'},
                 {'city': '南阳', 'city_id': '101180700'}, {'city': '宁德', 'city_id': '101230300'},
                 {'city': '南平', 'city_id': '101230900'}, {'city': '南充', 'city_id': '101270500'},
                 {'city': '内江', 'city_id': '101271200'}, {'city': '怒江傈僳族自治州', 'city_id': '101291400'},
                 {'city': '那曲', 'city_id': '101140600'}, {'city': '盘锦', 'city_id': '101071300'},
                 {'city': '平凉', 'city_id': '101160300'}, {'city': '平顶山', 'city_id': '101180500'},
                 {'city': '濮阳', 'city_id': '101181300'}, {'city': '莆田', 'city_id': '101230400'},
                 {'city': '萍乡', 'city_id': '101240900'}, {'city': '攀枝花', 'city_id': '101270200'},
                 {'city': '普洱', 'city_id': '101290500'}, {'city': '齐齐哈尔', 'city_id': '101050200'},
                 {'city': '七台河', 'city_id': '101050900'}, {'city': '秦皇岛', 'city_id': '101091100'},
                 {'city': '庆阳', 'city_id': '101160400'}, {'city': '衢州', 'city_id': '101211000'},
                 {'city': '清远', 'city_id': '101281300'}, {'city': '曲靖', 'city_id': '101290200'},
                 {'city': '钦州', 'city_id': '101301100'}, {'city': '黔东南苗族侗族自治州', 'city_id': '101260700'},
                 {'city': '黔南布依族苗族自治州', 'city_id': '101260800'},
                 {'city': '黔西南布依族苗族自治州', 'city_id': '101260900'},
                 {'city': '潜江', 'city_id': '101201500'}, {'city': '琼海', 'city_id': '101310600'},
                 {'city': '琼中黎族苗族自治县', 'city_id': '101311900'}, {'city': '日照', 'city_id': '101121500'},
                 {'city': '日喀则', 'city_id': '101140200'}, {'city': '绥化', 'city_id': '101050500'},
                 {'city': '双鸭山', 'city_id': '101051200'}, {'city': '四平', 'city_id': '101060300'},
                 {'city': '松原', 'city_id': '101060700'}, {'city': '朔州', 'city_id': '101100900'},
                 {'city': '商洛', 'city_id': '101110600'}, {'city': '石嘴山', 'city_id': '101170200'},
                 {'city': '商丘', 'city_id': '101181000'}, {'city': '三门峡', 'city_id': '101181700'},
                 {'city': '宿迁', 'city_id': '101191300'}, {'city': '十堰', 'city_id': '101201000'},
                 {'city': '随州', 'city_id': '101201100'}, {'city': '宿州', 'city_id': '101220700'},
                 {'city': '三明', 'city_id': '101230800'}, {'city': '上饶', 'city_id': '101240300'},
                 {'city': '邵阳', 'city_id': '101250900'}, {'city': '遂宁', 'city_id': '101270700'},
                 {'city': '韶关', 'city_id': '101280200'}, {'city': '汕头', 'city_id': '101280500'},
                 {'city': '汕尾', 'city_id': '101282100'}, {'city': '三亚', 'city_id': '101310200'},
                 {'city': '三沙', 'city_id': '101310300'}, {'city': '神农架', 'city_id': '101201700'},
                 {'city': '山南', 'city_id': '101140500'}, {'city': '石河子', 'city_id': '101131600'},
                 {'city': '双河市', 'city_id': '101132400'}, {'city': '通化', 'city_id': '101060400'},
                 {'city': '铁岭', 'city_id': '101071100'}, {'city': '通辽', 'city_id': '101080400'},
                 {'city': '唐山', 'city_id': '101090500'}, {'city': '铜川', 'city_id': '101111000'},
                 {'city': '泰安', 'city_id': '101120800'}, {'city': '天水', 'city_id': '101160900'},
                 {'city': '泰州', 'city_id': '101191200'}, {'city': '铜陵', 'city_id': '101221200'},
                 {'city': '铜仁', 'city_id': '101260400'}, {'city': '天门', 'city_id': '101201600'},
                 {'city': '屯昌', 'city_id': '101311100'}, {'city': '吐鲁番', 'city_id': '101130800'},
                 {'city': '塔城', 'city_id': '101131400'}, {'city': '图木舒克', 'city_id': '101131800'},
                 {'city': '铁门关', 'city_id': '101132000'}, {'city': '台湾', 'city_id': '101341100'},
                 {'city': '乌海', 'city_id': '101080300'}, {'city': '乌兰察布', 'city_id': '101080900'},
                 {'city': '渭南', 'city_id': '101110500'}, {'city': '潍坊', 'city_id': '101120600'},
                 {'city': '威海', 'city_id': '101121300'}, {'city': '乌鲁木齐', 'city_id': '101130100'},
                 {'city': '武威', 'city_id': '101160500'}, {'city': '吴忠', 'city_id': '101170300'},
                 {'city': '芜湖', 'city_id': '101220300'}, {'city': '梧州', 'city_id': '101300600'},
                 {'city': '文山壮族苗族自治州', 'city_id': '101291100'}, {'city': '五指山', 'city_id': '101310500'},
                 {'city': '文昌', 'city_id': '101310700'}, {'city': '万宁', 'city_id': '101310800'},
                 {'city': '五家渠', 'city_id': '101131900'}, {'city': '邢台', 'city_id': '101090900'},
                 {'city': '忻州', 'city_id': '101101000'}, {'city': '咸阳', 'city_id': '101110200'},
                 {'city': '西宁', 'city_id': '101150100'}, {'city': '新乡', 'city_id': '101180300'},
                 {'city': '许昌', 'city_id': '101180400'}, {'city': '信阳', 'city_id': '101180600'},
                 {'city': '襄阳', 'city_id': '101200200'}, {'city': '孝感', 'city_id': '101200400'},
                 {'city': '咸宁', 'city_id': '101200700'}, {'city': '宣城', 'city_id': '101221300'},
                 {'city': '新余', 'city_id': '101241000'}, {'city': '湘潭', 'city_id': '101250200'},
                 {'city': '香港', 'city_id': '101320300'}, {'city': '湘西土家族苗族自治州', 'city_id': '101251400'},
                 {'city': '西双版纳傣族自治州', 'city_id': '101291000'}, {'city': '仙桃', 'city_id': '101201400'},
                 {'city': '锡林郭勒盟', 'city_id': '101081000'}, {'city': '兴安盟', 'city_id': '101081100'},
                 {'city': '伊春', 'city_id': '101050700'}, {'city': '营口', 'city_id': '101070800'},
                 {'city': '阳泉', 'city_id': '101100300'}, {'city': '运城', 'city_id': '101100800'},
                 {'city': '延安', 'city_id': '101110300'}, {'city': '榆林', 'city_id': '101110400'},
                 {'city': '银川', 'city_id': '101170100'}, {'city': '扬州', 'city_id': '101190600'},
                 {'city': '盐城', 'city_id': '101190700'}, {'city': '宜昌', 'city_id': '101200900'},
                 {'city': '宜春', 'city_id': '101240500'}, {'city': '鹰潭', 'city_id': '101241100'},
                 {'city': '益阳', 'city_id': '101250700'}, {'city': '岳阳', 'city_id': '101251000'},
                 {'city': '永州', 'city_id': '101251300'}, {'city': '宜宾', 'city_id': '101271100'},
                 {'city': '雅安', 'city_id': '101271600'}, {'city': '云浮', 'city_id': '101281400'},
                 {'city': '阳江', 'city_id': '101281800'}, {'city': '玉溪', 'city_id': '101290400'},
                 {'city': '玉林', 'city_id': '101300900'}, {'city': '延边朝鲜族自治州', 'city_id': '101060900'},
                 {'city': '玉树藏族自治州', 'city_id': '101150700'},
                 {'city': '伊犁哈萨克自治州', 'city_id': '101130600'},
                 {'city': '张家口', 'city_id': '101090300'}, {'city': '淄博', 'city_id': '101120300'},
                 {'city': '枣庄', 'city_id': '101121400'}, {'city': '张掖', 'city_id': '101160700'},
                 {'city': '中卫', 'city_id': '101170500'}, {'city': '周口', 'city_id': '101181400'},
                 {'city': '驻马店', 'city_id': '101181600'}, {'city': '镇江', 'city_id': '101190300'},
                 {'city': '舟山', 'city_id': '101211100'}, {'city': '漳州', 'city_id': '101230600'},
                 {'city': '株洲', 'city_id': '101250300'}, {'city': '张家界', 'city_id': '101251100'},
                 {'city': '遵义', 'city_id': '101260200'}, {'city': '自贡', 'city_id': '101270300'},
                 {'city': '资阳', 'city_id': '101271300'}, {'city': '肇庆', 'city_id': '101280900'},
                 {'city': '湛江', 'city_id': '101281000'}, {'city': '昭通', 'city_id': '101290700'},
                 {'city': '长春', 'city_id': '101060100'}, {'city': '常州', 'city_id': '101191100'},
                 {'city': '大连', 'city_id': '101070200'}, {'city': '东莞', 'city_id': '101281600'},
                 {'city': '福州', 'city_id': '101230100'}, {'city': '贵阳', 'city_id': '101260100'},
                 {'city': '哈尔滨', 'city_id': '101050100'}, {'city': '惠州', 'city_id': '101280300'},
                 {'city': '嘉兴', 'city_id': '101210300'}, {'city': '金华', 'city_id': '101210900'},
                 {'city': '昆明', 'city_id': '101290100'}, {'city': '南通', 'city_id': '101190500'},
                 {'city': '南昌', 'city_id': '101240100'}, {'city': '南宁', 'city_id': '101300100'},
                 {'city': '青岛', 'city_id': '101120200'}, {'city': '泉州', 'city_id': '101230500'},
                 {'city': '石家庄', 'city_id': '101090100'}, {'city': '绍兴', 'city_id': '101210500'},
                 {'city': '太原', 'city_id': '101100100'}, {'city': '台州', 'city_id': '101210600'},
                 {'city': '无锡', 'city_id': '101190200'}, {'city': '温州', 'city_id': '101210700'},
                 {'city': '徐州', 'city_id': '101190800'}, {'city': '烟台', 'city_id': '101120500'},
                 {'city': '珠海', 'city_id': '101280700'}, {'city': '中山', 'city_id': '101281700'}
                 ]


class SqlQueue:  # mysql长连接类
    def __init__(self, host="localhost", user="root", password="123456", database="pa1", maxsize=5):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.charset = 'utf8'
        self.q = Queue(maxsize=maxsize)
        for i in range(0, maxsize):
            db = pymysql.connect(host=host, user=user, password=password, database=database,
                                 charset='utf8')  # 打开数据库连接
            self.q.put(db)

    def test_conn(self, db):
        """
        测试是否断开链接，并重连
        """
        # noinspection PyBroadException
        try:
            db.ping()  # 运行ping函数，判断是否断开链接
            return True
        except BaseException:
            return False

    def select(self, sql, fetch_one=False):
        while True:
            db = self.q.get()
            if db:
                break
            else:
                time.sleep(1)
        if not self.test_conn(db):
            db = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                 database=self.database, charset=self.charset)  # 重连数据库
        cursor = db.cursor(pymysql.cursors.DictCursor)  # 使用cursor()方法获取操作游标
        try:
            cursor.execute(sql)  # 执行SQL语句
            if fetch_one:
                return cursor.fetchone()
            else:
                return cursor.fetchall()  # 获取所有记录列表
            # print('查询成功')
        except BaseException as e:
            print("Error: unable to fetch data", e)
        finally:
            self.q.put(db)

    def insert(self, sql, data=None):
        while True:
            db = self.q.get()
            if db:
                break
            else:
                time.sleep(1)
        if not self.test_conn(db):
            db = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                 database=self.database, charset=self.charset)  # 重连数据库
        cursor = db.cursor(pymysql.cursors.DictCursor)  # 使用cursor()方法获取操作游标
        try:
            if data:
                cursor.execute(sql, data)  # 执行SQL语句
            else:
                cursor.execute(sql)  # 执行SQL语句
            db.commit()  # 提交到数据库执行
            # print('插入成功')
            return cursor.lastrowid
        except BaseException as e:
            print('Error: ', e)
            db.rollback()  # 发生错误时回滚
        finally:
            self.q.put(db)

    def __del__(self):
        try:
            while True:
                self.q.get().close()
                if self.q.empty():
                    break
        except BaseException as e:
            print(e)


edu_dict = {0: "学历不限", 1: "初中及以下", 2: "高中", 3: "中专/中技", 4: "大专", 5: "本科", 6: "硕士", 7: "博士"}
we_dict = {0: "经验不限", 2: "1年以内", 3: "1-3年", 4: "3-5年", 5: "5-10年", 6: "10年以上"}
cpy_p_dict = {0: '不限', 1: '0-20人', 2: '20-99人', 3: '100-499人', 4: '500-999人', 5: '1000-9999人', 6: '10000人以上'}


def change_salary(salary):
    if '薪' in salary:
        salary, monthsalary = salary.split('·')
        monthsalary = monthsalary.strip('薪')
    else:
        monthsalary = '12'
    if 'K' in salary:
        minsalary, maxsalary = salary.split('-')
        minsalary = int(float(minsalary)) * 1000
        maxsalary = int(float(maxsalary.strip('K'))) * 1000
    elif '元/时' in salary:
        minsalary, maxsalary = salary.split('-')
        minsalary = int(float(minsalary)) * 180
        maxsalary = int(float(maxsalary.strip('元/时'))) * 180
    elif '元/天' in salary:
        minsalary, maxsalary = salary.split('-')
        minsalary = int(float(minsalary)) * 5 * 4
        maxsalary = int(float(maxsalary.strip('元/天'))) * 5 * 4
    else:
        minsalary = 0
        maxsalary = 0
    return minsalary, maxsalary, monthsalary

def edu_num(edu):
    for edu_num, edu_item in edu_dict.items():
        if edu_item in edu:
            return edu_num
    return 0

def we_num(we):
    for we_num, we_item in we_dict.items():
        if we_item in we:
            return we_num
    return 0

def split_company_item(company_item):
    companypersonnum = 0
    for com_num, com_item in cpy_p_dict.items():
        if com_item in company_item:
            companypersonnum = com_num
    return companypersonnum


_proxies = [{"ip": "54.254.144.154", "port": 4382}, {"ip": "3.64.130.48", "port": 17566},
            {"ip": "54.254.144.154", "port": 4380}, {"ip": "54.254.144.154", "port": 4381},
            {"ip": "54.254.144.154", "port": 4383}, {"ip": "54.169.86.11", "port": 18858},
            {"ip": "13.250.21.21", "port": 4110}, {"ip": "3.84.248.213", "port": 16981},
            {"ip": "13.212.118.69", "port": 4937}, {"ip": "3.64.130.48", "port": 14537}]


class Spider(object):
    def __init__(self, sleep_time=3):
        self.spider_name = str(__file__.split('\\')[-1])
        self.sleep_time = sleep_time
        self.client = redis.Redis('10.86.0.107', decode_responses=True)
        self.sql = SqlQueue(host="10.86.0.107", user="root", password="wit123456", database='bosshr')
        disable_warnings()
        # self.proxies = ['{ip}:{port}'.format_map(item) for item in _proxies]
        self.proxies = []
        # with open('boss_enc.js', encoding='utf8') as f:
        #     self.raw_js = f.read() + '\n!'
        # self.tail_js = """
        # function get_token(seed, ts) {
        #     return encodeURIComponent((new window.ABC).z(seed, parseInt(ts) + 60 * (480 + (new Date).getTimezoneOffset()) * 1e3))
        # }
        # """
        self.sql_company_id = "SELECT" + """ id FROM company.company_info WHERE companyUrl = "%s" OR companyName = "%s" """
        self.sql_company = "INSERT" + """ INTO company.company_info
(companyName,companyUrl,companyType,companyIndustry,companyPersonNum,address,update_time) VALUES (%s,%s,%s,%s,%s,%s,%s);"""
        threading.Thread(target=self.get_proxies).start()
        self.url_set = set()
        self.m = str(datetime.date.today().month).zfill(2)
        self.failed_proxies = set()
        self.thread_proxy_map = {}
        self.current_file_name = None
        self.today_js = ''
        self.ctx = None

    def get_proxies(self):
        while True:
            try:
                self.proxies = self.client.lrange('use_proxies', 0, -1)
                self.failed_proxies = set(self.proxies) & self.failed_proxies
                self.proxies = list(set(self.proxies) - self.failed_proxies)

            except Exception as e:
                if isinstance(e, KeyboardInterrupt):
                    raise KeyboardInterrupt(e)
                print(e)
            time.sleep(1)

    def get_proxy(self):
        while True:
            if self.proxies:
                return self.proxies.pop()
            else:
                print('未获取到代理ip,重试中...')
            time.sleep(2)

    def download(self, url, timesleep=1, timeout=30):
        thread_name = threading.currentThread().getName().replace('-', '')
        print('Downloading: %s' % url)
        for x in range(3):
            thead_map = self.thread_proxy_map.get(thread_name, {})
            proxy = thead_map.get('proxy', self.get_proxy())
            cookies = {
            "lastCity": "101020100",
            "wd_guid": "73ff5583-e5a0-469d-b8b1-7d724a114266",
            "historyState": "state",
            "_bl_uid": "Oglj2hzRhyzah6sFXzwt2kzd35q0",
            "sid": "sem_pz_bdpc_dasou_title",
            "__zp_seo_uuid__": "70092b9a-81d7-4cc0-b75f-798e426b2fe8",
            "__g": "sem_pz_bdpc_dasou_title",
            "Hm_lvt_194df3105ad7148dcf2b98a91b5e727a": "1683698772,1685604121",
            "Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a": "1685604128",
            "__zp_stoken__": "5879efGgOOAt3XjV2I0Bud149ICJbECNlLl0oHmJ2J2ECRn8nQChlDCNLEilnWQJWfmQSYBI2RBN7SDVAbysNURc9QB5bPjEpX1ZYD0luYnAwA1Y3FDYVOkUqelN%2BGkcdPF0gGxc%2FRWRtBkU%3D",
            "__c": "1685604121",
            "__l": "r=https%3A%2F%2Fwww.baidu.com%2Fother.php%3Fsc.0f00000gBrgDLroP9ds_155-Vtjxk816EVzTF62Ml4Ko99jUVETIO0nJ7fqzfU8uMdP3B95ao29hVpAyD_XTnm6n9VqFARhvn4_O1XxJ-wdDfsMR6nblFOsq-8kP6EfgDItNbA94kmC1OgGeVMmw5OqRF9ZYEOsrycoDphGr5OfgmTwABMtU5fqleMWSAnI_BH50qdu42fR8jZB210eqRbxmcc3D.7D_NR2Ar5Od663rj6t8AGSPticrtXFBPrM-kt5QxIW94UhmLmry6S9wiGyAp7BEIu80.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqmhq1TsKdTvNzgLw4TARqn0K9u7qYXgK-5Hn0IvqzujdBULP10ZFWIWYs0ZNzU7qGujYkPHfYrHRLnH6d0Addgv-b5HDdnWnvPjDz0AdxpyfqnHcknHbdP160UgwsU7qGujYknW6zP6KsI-qGujYs0A-bm1dribGH0ZKGujYz0APGujYYnj60mLFW5HRLPWT1%26dt%3D1685604107%26wd%3Dboss%26tpl%3Dtpl_12826_31784_0%26l%3D1544957185%26ai%3D0_60872259_1_1%26us%3DlinkVersion%253D1%2526compPath%253D10036.0-10032.0%2526label%253D%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkType%253D%2526linkText%253DBOSS%2525E7%25259B%2525B4%2525E8%252581%252598%2525E2%252580%252594%2525E2%252580%252594%2525E6%252589%2525BE%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258ABOSS%2525E7%25259B%2525B4%2525E8%252581%252598%2525EF%2525BC%25258C&l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3D%26city%3D101020100%26position%3D100101&s=3&g=%2Fwww.zhipin.com%2Fshanghai%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&friend_source=0&s=3&friend_source=0",
            "__a": "21924567.1683698873.1683698772.1685604121.108.2.4.4"
        }

            # proxies = {'http': 'http://%s' % proxy, 'https': 'http://%s' % proxy}
            proxies = {'http': proxy, 'https': proxy}

            url_list = url.split('&')
            city_id = url_list[1].replace('city=', '')
            industry_id = url_list[2].replace('position=', '')
            page_id = url_list[3].replace('page=', '')
            #ourl = f"https://www.zhipin.com/c{city_id}-p{industry_id}/"
            #ourl = f"https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=&city={city_id}&experience=&degree=&industry=&scale=&stage=&position={industry_id}&salary=&multiBusinessDistrict=&page={page_id}&pageSize=30"
            headers = {
                "authority": "www.zhipin.com",
                "accept": "application/json,text/plain',*/*",
                "accept-language": "zh-CN,zh;q=0.9",
                "referer": f"https://www.zhipin.com/web/geek/job?query=&city={city_id}&position={industry_id}",
                "sec-ch-ua": "\"Google Chrome\";v=\"110\", \"Chromium\";v=\"110\", \"Not-A.Brand\";v=\"24\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
                "x-requested-with": "XMLHttpRequest"
            }
            ourl = "https://www.zhipin.com/wapi/zpgeek/search/joblist.json"
            params = {
                "scene": "1",
                "query": "",
                "city": city_id,
                "experience": "",
                "payType": "",
                "partTime": "",
                "degree": "",
                "industry": "",
                "scale": "",
                "stage": "",
                "position": industry_id,
                "jobType": "",
                "salary": "",
                "multiBusinessDistrict": "",
                "multiSubway": "",
                "page": page_id,
                "pageSize": "30"
            }

            try:
                response = requests.get(ourl, headers=headers,params=params, proxies=proxies, timeout=timeout)
            except Exception as e:
                print('First Response Error'.center(100, '#'))
                print(e)
                self.failed_proxies.add(proxy)
                try:
                    if proxy in self.proxies:
                        self.proxies.remove(proxy)
                except Exception:
                    pass
                time.sleep(timesleep + random.random())
                continue
            # cookies = requests.utils.dict_from_cookiejar(response.cookies)
            zp_data = response.json()['zpData']
            enc = quote(zp_data['seed'] + ',' + str(zp_data['ts']))
            zp_token = self.zp_token(enc,city_id)
            if not zp_token:
                print('加密生成失败')
                continue
            js_url = "https://www.zhipin.com/wapi/zpgeek/search/joblist.json"
            params = {
                "scene": "1",
                "query": "",
                "city": city_id,
                "experience": "",
                "payType": "",
                "partTime": "",
                "degree": "",
                "industry": "",
                "scale": "",
                "stage": "",
                "position": industry_id,
                "jobType": "",
                "salary": "",
                "multiBusinessDistrict": "",
                "multiSubway": "",
                "page": page_id,
                "pageSize": "30"
            }
            cookies['__zp_stoken__'] = zp_token
            # headers['referer'] = ourl
            try:
                response = requests.get(url=js_url, headers=headers,params=params, proxies=proxies, timeout=timeout, cookies=cookies)
            except Exception as e:
                print('Third Response Error'.center(100, '#'))
                print(e)
                time.sleep(timesleep + random.random())
                continue

            if response.status_code == 200:
                if "禁止访问" in response.content.decode():
                    print("您的 IP 存在异常访问行为，暂时被禁止访问！")
                    self.failed_proxies.add(proxy)
                    try:
                        if proxy in self.proxies:
                            self.proxies.remove(proxy)
                    except Exception:
                        pass
                    continue
                if "您的访问行为异常" in response.content.decode():
                    print("您的访问行为异常。")
                    continue

                # cookies_map = requests.utils.dict_from_cookiejar(response.cookies)
                # if len(cookies_map):
                #     if '__zp_sseed__' in cookies_map:
                #         _seed = cookies_map.get('__zp_sseed__')
                #         _ts = cookies_map.get('__zp_sts__')
                #         enc = quote(_seed + ',' + _ts)
                #         cookies.update(cookies_map)
                #         self.thread_proxy_map[thread_name] = {'proxy': proxy, 'enc': enc, 'cookie': cookies}
                #     else:
                #         self.thread_proxy_map[thread_name] = {'proxy': proxy, 'enc': None, 'cookie': None}
                else:
                    time.sleep(timesleep + random.random())

                time.sleep(timesleep + random.random())

                return response.content.decode()

            # elif response.status_code == 406:
            #     seed_ts = response.cookies.get_dict()
            #     enc = quote(seed_ts['__zp_sseed__'] + ',' + str(seed_ts['__zp_sts__']))
            #     zp_token = self.zp_token('', enc)
            #     cookies['__zp_stoken__'] = zp_token
            #     response = requests.get(js_url, headers=headers, proxies=proxies, timeout=timeout, cookies=cookies)

            else:
                time.sleep(timesleep + random.random())
                self.thread_proxy_map[thread_name] = {'proxy': self.get_proxy(), 'enc': None, 'cookie': None}

        else:
            return ''

    def zp_token(self, enc,city_id):
        try:
            lock.acquire()
            zp_token = requests.get(
                'http://10.86.1.74:8888/getToken?enc={enc}&cityCode={city}'.format(enc=enc, city=city_id)).text
            # zp_token = requests.get('http://127.0.0.1:8888/getToken?enc={enc}&cityCode={city}'.format(enc=enc, city=city_id)).text

        except Exception as e:
            time.sleep(10)
            zp_token = ''
        finally:
            lock.release()
        return zp_token

    def get_list(self, url_items):
        origin_url = url_items['url']
        hi = 0
        while True:
            html = self.download(origin_url)
            if html:
                break
            hi += 1
            if hi == 9:
                print('下载失败：', origin_url)
                return None
        # noinspection PyBroadException
        # soup = BeautifulSoup(html, 'lxml')
        try:
            data = json.loads(html)
            data_list = data.get('zpData', {}).get('jobList', [])
            pages = math.ceil(data.get('zpData', {}).get('totalCount', 0) / 30)
        except AttributeError:
            data_list = []
            pages = 1
        # self.get_item_to_sql(data_list, url_items)
        # #
        if len(data_list) > 0:

            if not self.get_item_to_sql(data_list, url_items):
                for i in range(2, pages):
                    next_url = origin_url.replace('page=1', 'page=%s' % i)
                    if self.get_next(next_url, url_items):
                        break

    def get_next(self, next_url, url_items):
        hi2 = 0
        while True:
            html = self.download(next_url)
            if html:
                break
            hi2 += 1
            if hi2 == 9:
                print('下载失败：', next_url)
                return 0
        try:
            data = json.loads(html)
            data_list = data.get('zpData', {}).get('jobList', [])
        except AttributeError:
            data_list = []
        if len(data_list) > 0:
            return self.get_item_to_sql(data_list, url_items)

    def get_item_to_sql(self, data_list, url_items):
        print('data_list:', len(data_list))
        not_filter = []
        for data in data_list:
            item = url_items.copy()
            item['publishTime'] = datetime.date.today()
            item['update_time'] = datetime.datetime.now()
            item['jobName'] = data.get('jobName', '')
            item['detailUrl'] = f"https://www.zhipin.com/job_detail/{data.get('encryptJobId', '')}.html"
            if self.url_qc(item['detailUrl']):
                continue
            not_filter.append(1)
            item['minSalary'], item['maxSalary'], item['monthSalary'] = change_salary(data.get('salaryDesc', ''))
            item['workExperience'] = we_num(data.get('jobExperience', ''))
            item['education'] = edu_num(data.get('jobDegree', ''))
            item['companyName'] = data.get('brandName', '')
            item['companyUrl'] = f"https://www.zhipin.com/gongsi/{data.get('encryptBrandId', '')}.html"
            item['companyIndustry'] = data.get('brandIndustry', '')
            item['companyType'] = data.get('brandStageName', '')
            item['companyPersonNum'] = split_company_item(data.get('brandScaleName', ''))
            item['city'] = item['address'] = data.get('cityName', '')+'-' +data.get('areaDistrict', '')
            welfareList = data.get('welfareList', [])
            if len(welfareList):
                item['welfare'] = ','.join(welfareList)
            item['company_id'] = self.get_company_id(item)
            # pprint(item)
            self.insert(item)
        # if len(data_list) < 30:
        if len(data_list) < 30 or len(not_filter) <= 3:
            return True

    def get_jobinfo(self, item):
        pass

    def get_company_id(self, item):
        company_id_dict = self.sql.select(self.sql_company_id % (item['companyUrl'], item['companyName']),
                                          fetch_one=True)
        if company_id_dict:
            company_id = company_id_dict.get('id', 0)
        else:
            company_id = self.sql.insert(self.sql_company, [
                item['companyName'], item['companyUrl'], item['companyType'], item['companyIndustry'],
                item['companyPersonNum'], item['address'], item['update_time']])
            print('公司数据录入成功'.center(100, '#'))
            if not company_id:
                company_id_dict = self.sql.select(self.sql_company_id % (item['companyUrl'], item['companyName']),
                                                  fetch_one=True)
                company_id = company_id_dict.get('id', 0)
        return company_id

    def insert(self, item):
        print(self.spider_name.center(100, '='))
        # pprint(item)
        ls = [item.get('jobName'), item['minSalary'], item['maxSalary'], item['city'], item['company_id'],
              datetime.date.today().month]
        item['job_id'] = hashlib.md5(''.join([str(x) for x in ls]).encode()).hexdigest()
        y = str(datetime.date.today().year)
        m = str(datetime.date.today().month).zfill(2)
        sql_job = "INSERT" + f""" INTO jobinfo_{y}{m} (jobName,minSalary,maxSalary,monthSalary,detailUrl,education,city,
    firstJobType,secondJobType,thirdJobType,publishTime,workExperience,company_id,welfare,update_time,job_id,address)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
        self.sql.insert(sql_job, [
            item['jobName'], item['minSalary'], item['maxSalary'], item['monthSalary'], item['detailUrl'],
            item['education'], item['city'], item['firstJobType'], item['secondJobType'], item['thirdJobType'],
            item['publishTime'], item['workExperience'], item['company_id'], item.get('welfare', ''),
            item['update_time'],
            item['job_id'],item['address'] ])
        print('工作数据入库成功'.center(100, '#'))

    def url_qc(self, url):
        # y = str(datetime.date.today().year)
        m = str(datetime.date.today().month).zfill(2)
        if self.m != m:
            self.url_set.clear()
            self.m = m
        url_md5 = hashlib.md5(url.encode()).hexdigest()
        if url_md5 in self.url_set:
            print(f"{self.spider_name} url重复，去重".center(50, "*"))
            return True
        else:
            self.url_set.add(url_md5)
            return False

    def spider_start(self):
        y = str(datetime.date.today().year)
        m = str(datetime.date.today().month).zfill(2)
        url_list = self.sql.select("SELECT " + f"MD5(detailUrl) as url FROM `jobinfo_{y}{m}`LIMIT 1")
        for url in url_list:
            self.url_set.add(url['url'])


def list_url():
    url_list = []
    is_start = False
    hot_city = ['上海', '北京', '杭州', '广州', '深圳', '苏州', '南京', '武汉', '成都', '合肥', '济南', '西安', '长沙',
                '天津', '厦门', '宁波', '重庆',
                '佛山', '沈阳', '郑州', '福州', '东莞', '青岛', '南昌', '大连', '无锡', '石家庄', '惠州', '昆明',
                '嘉兴', '金华', '常州', '太原', '海口',
                '哈尔滨', '珠海', '贵阳', '兰州', '长春', '临沂', '温州', '南通', '泉州', '呼和浩特', '洛阳', '南宁',
                '江门', '烟台', '潍坊', '湖州', '徐州',
                '济宁', '中山', '廊坊', '乌鲁木齐', '邯郸', '淄博', '芜湖', '绍兴', '绵阳', '台州', '保定', '赣州',
                '淮安', '南阳', '唐山', '汕头', '银川',
                '漳州', '扬州', '威海', '新乡', '德州', '阜阳', '九江', '柳州', '菏泽', '连云港', '聊城', '镇江',
                '包头', '桂林', '衡阳', '泰州', '咸阳',
                '三亚', '秦皇岛', '肇庆', '荆州', '襄阳', '株洲', '西宁', '衡水', '上饶', '邢台', '盐城', '东营',
                '日照', '揭阳', '泰安', '南充', '宁德',
                '临汾', '德阳', '宿迁', '许昌', '六安', '沧州', '安阳', '运城', '大同', '吉安', '枣庄', '湛江', '开封',
                '遵义', '安庆', '茂名', '清远',
                '吉林', '商丘', '丽水', '黄石', '鞍山', '河源', '宜昌', '晋中', '焦作', '莆田', '湘潭', ]
    for location in Location_dict[:]:
        # if location['city_id'] == '101270100':
        #     is_start = True
        # if not is_start:
        #     continue
        if location['city'] in hot_city:
            for industry in Industry_dict[::-1]:
                url_list.append({'city': location['city'], 'firstJobType': industry['firstJobType'],
                                 'secondJobType': industry['secondJobType'], 'thirdJobType': industry['thirdJobType'],
                                 # 'url': f"https://www.zhipin.com/{location['city_id']}-{industry['url']}",
                                 'url': f"https://www.zhipin.com/web/geek/job?query=&city={location['city_id']}&position={industry['url']}&page=1",
                                 })
        else:
            url_list.append({'city': location['city'], 'firstJobType': '',
                             'secondJobType': '', 'thirdJobType': '',
                             # 'url': f"https://www.zhipin.com/{location['city_id']}-{industry['url']}",
                             'url': f"https://www.zhipin.com/web/geek/job?query=&city={location['city_id']}&position=&page=1",
                             })

    return url_list


def main():
    S = Spider()
    S.spider_start()
    pool = threadpool.ThreadPool(31)
    # for url_item in url_item_list:
    #     print(url_item)
    #     S.get_list(url_item)
    url_dict = list_url()
    url_dict = url_dict
    print('列表页读取完毕，总数：', len(url_dict))
    while True:
        job_requests = threadpool.makeRequests(S.get_list, url_dict)
        [pool.putRequest(req) for req in job_requests]
        pool.wait()
        print('暂停执行'.center(50, "*"))
        time.sleep(60)
        # break


if __name__ == '__main__':
    main()
