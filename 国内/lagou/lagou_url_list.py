# -*- coding: utf-8 -*-
city_list = {'厦门', '广州', '牡丹江', '酒泉', '山南', '嘉峪关', '宜春', '天水', '乌海', '郴州', '赣州', '巴彦淖尔', '昭通', '昆明', '梅州', '广元', '岳阳',
             '红河', '芜湖', '柳州', '云浮', '达州', '淮南', '南阳', '上海', '黄石', '忻州', '渭南', '白银', '天门', '温州', '阿拉善盟', '大理',
             '甘孜藏族自治州', '白山', '黔南', '泉州', '阳泉', '濮阳', '桂林', '北海', '随州', '安康', '吕梁', '晋中', '扬州', '赤峰', '儋州', '青岛',
             '巴音郭楞', '新乡', '六盘水', '潮州', '阜新', '喀什', '新余', '贵阳', '阜阳', '丽江', '沧州', '陇南', '普洱', '枣庄', '九江', '龙岩', '景德镇',
             '资阳', '鸡西', '吉林', '蚌埠', '珠海', '铜陵', '苏州', '贵港', '德阳', '江门', '贺州', '信阳', '廊坊', '凉山彝族自治州', '吴忠', '宜宾', '安顺',
             '连云港', '邵阳', '惠州', '黔西南', '泰州', '中卫', '吉安', '北京', '内江', '来宾', '鄂尔多斯', '武汉', '湘潭', '日喀则', '运城', '大连', '永州',
             '衡水', '益阳', '宁波', '盐城', '杭州', '咸阳', '朝阳', '榆林', '绍兴', '淮北', '张家界', '南平', '保定', '双鸭山', '海西', '广安', '锡林郭勒盟',
             '湛江', '锦州', '商洛', '兰州', '石嘴山', '安阳', '哈密', '河源', '鹤壁', '丽水', '三明', '中山', '黄冈', '盘锦', '六安', '宝鸡', '兴安盟',
             '黑河', '南通', '鹰潭', '台州', '济宁', '咸宁', '长治', '绥化', '茂名', '洛阳', '防城港', '汉中', '常州', '雅安', '西宁', '黔东南', '自贡',
             '河池', '攀枝花', '三沙', '曲靖', '阳江', '临夏', '十堰', '黄山', '海东', '通辽', '昌吉', '甘南', '聊城', '泸州', '合肥', '张家口', '佳木斯',
             '重庆', '丹东', '昌都', '文山', '德宏', '郑州', '崇左', '宿迁', '日照', '临沂', '莆田', '德州', '天津', '石河子', '铜仁', '安庆', '阿克苏',
             '萍乡', '沈阳', '百色', '福州', '伊春', '定西', '邯郸', '辽阳', '塔城', '驻马店', '揭阳', '抚州', '遂宁', '拉萨', '荆门', '烟台', '海口',
             '葫芦岛', '镇江', '潍坊', '庆阳', '淄博', '齐齐哈尔', '湘西土家族苗族自治州', '东营', '上饶', '台湾', '铁岭', '滨州', '抚顺', '博尔塔拉', '成都',
             '阿里地区', '玉溪', '延安', '晋城', '马鞍山', '孝感', '鄂州', '怀化', '遵义', '宁德', '肇庆', '宜昌', '呼伦贝尔', '迪庆', '太原', '宣城', '伊犁',
             '深圳', '绵阳', '许昌', '焦作', '银川', '漯河', '嘉兴', '哈尔滨', '济南', '铜川', '南昌', '呼和浩特', '眉山', '衢州', '淮安', '泰安', '滁州',
             '南宁', '本溪', '韶关', '钦州', '玉林', '漳州', '荆州', '长沙', '鞍山', '汕尾', '鹤岗', '阿勒泰', '乐山', '辽源', '平顶山', '营口', '大庆',
             '平凉', '七台河', '张掖', '威海', '保山', '临沧', '金昌', '无锡', '巴中', '武威', '常德', '西双版纳', '白城', '菏泽', '克孜勒苏', '济源', '楚雄',
             '三门峡', '南京', '石家庄', '秦皇岛', '阿坝藏族羌族自治州', '三亚', '南充', '东莞', '海外', '佛山', '四平', '徐州', '唐山', '长春', '开封', '固原',
             '乌兰察布', '林芝', '延边', '池州', '临汾', '乌鲁木齐', '金华', '商丘', '恩施', '克拉玛依', '襄阳', '承德', '通化', '梧州', '汕头', '松原', '株洲',
             '宿州', '清远', '香港', '朔州', '娄底', '西安', '大同', '湖州', '澳门', '亳州', '包头', '莱芜', '怒江', '毕节', '周口', '衡阳', '邢台', '舟山'}

job_types = {'人事/HR', '市场总监', '电竞主持', '后端开发其它', '测试工程师', '专利', 'CTO', 'DBA其它', '销售VP', '网络推广', 'CFO', '自动化', '电竞讲师',
             'Python', '系统工程师', 'C', 'F5', 'SQLServer', '游戏数值策划', '客户代表', 'MongoDB', '渠道推广', '游戏原画', '销售工程师', '游戏体验',
             '游戏角色', '广告文案', '美术设计师（2D/3D）', '网页交互设计师', '灰盒测试', '广告定价', '客服总监', '产品总监', 'CEO', '语音识别', '游戏特效', 'Flash',
             '游戏编辑', '全栈工程师', '新媒体运营', '系统管理员', '.NET', '网页产品经理', '会计', '硬件', '活动策划', '绩效考核经理', 'Android', 'Go', '游戏美工',
             '测试其它', 'WEB安全', '设计经理/主管', '品牌策划', '商务专员', '精益工程师', 'web前端', '主编', '媒介顾问', '美术指导', '公关总监', '病毒分析', '法务',
             '项目经理', '单片机', '财务总监/经理', 'APP设计师', '结算', 'html5', '硬件开发其它', '多媒体设计师', '原画师', '淘宝客服', '广告创意', '产品部经理',
             '机器学习', 'Hadoop', '技术经理', 'ETL', '视觉设计总监', '内容运营', '热传导', '实施工程师', '架构师', '活动运营', '手游推广', '培训经理', 'VB',
             '视觉设计经理/主管', '性能测试', '运维工程师', 'Flash设计师', '企业软件其它', '前台', '财务', 'C#', '策划经理', '团队经理', '商务主管', '行政总监/经理',
             '广告投放', '模具设计', '人力资源', '出纳', '招聘', 'C++游戏开发', '游戏产品经理', 'PHP', '销售经理', '算法工程师', '系统集成', 'DSP开发', '售前咨询',
             'SEM', '小游戏开发', '广告制作', '员工关系', 'Perl', '市场营销', '游戏测试', '设计总监', '售后客服', 'C++', 'Node.js', 'COCOS2D-X',
             '网络安全', '产品实习生', '交互设计师', 'H5游戏开发', 'Shell', '数据仓库', '品牌合作', '律师', '图像处理', '税务', '交互设计经理/主管', '销售顾问',
             '安全专家', 'COO', '交互设计总监', '客户经理', '海外运营', '商业数据分析', '品牌公关', '网店运营', '系统安全', '游戏界面设计师', '其他销售管理职位', 'UI设计师',
             '广告协调', '项目助理', '风控', '保险销售', '城市经理', '材料工程师', '深度学习', '副主编', '游戏动作', 'Ruby', '区块链', '剧情设计', '媒介投放',
             '信用卡销售', '文案策划', 'CDN', '网络工程师', '运营经理', 'MySQL', '自动化测试', '广告设计师', '精准推荐', '客服经理', '运营专员', '区域总监',
             'ARM开发', '内容编辑', '销售总监', '移动开发其它', 'JavaScript', '嵌入式', '移动产品经理', '售前工程师', '广告专员', '游戏陪练', '用户研究总监',
             '黑盒测试', 'Oracle', '数据运营', '商务拓展', '游戏界面', '无线交互设计师', '用户运营', '前端开发其它', '游戏动效', 'Delphi', '技术总监', '其他销售',
             'Hive', '销售专员', '助理', '手机测试', '媒介合作', 'SEO', '市场推广', '品类运营', '媒介经理', '总助', '功能测试', '硬件测试', 'Java', '视觉设计师',
             '硬件交互设计师', 'FLASH', '产品助理', '无线产品设计师', '游戏项目经理', '自然语言处理', '数据挖掘', '测试经理', '品牌专员', '政府关系', '白盒测试', '搜索算法',
             '数据分析师', '媒介总监', '游戏动画', 'U3D', '售后工程师', '用户研究经理/主管', '网页设计师', '游戏制作人', 'HRD/HRM', 'WP', '测试总监', 'BI工程师',
             '用户研究员', 'IT支持', '运维其它', '产品经理', '驱动开发', '记者', '市场策划', '商务渠道', '电路设计', '商务总监', 'DB2', '平面设计师', '薪资福利经理',
             '市场顾问', 'IDC', '行政', '游戏推广', '测试开发', '运维总监', '网页产品设计师', '技术合伙人', '电商产品经理', '数据产品经理', '审计', '大客户代表', '文秘',
             '运营总监', '网络营销', '海外市场', '机器视觉', '代理商销售', '产品运营', 'iOS', '创意总监', '游戏后端开发', '渠道销售 ', 'ASP', '游戏运营', '游戏主播',
             '电话销售', 'HRBP', '页游推广', 'FPGA开发', '游戏文案', '运维经理', '游戏策划', '运维开发工程师', '商家运营', '高端技术职位其它', 'HTML5', '射频工程师',
             '图像识别', '项目总监', 'PCB工艺', '游戏场景', '广告销售'}

# 需要将三级三级城市采集完全的城市，不再列表中的城市只按照城市列表采集不搜索
full_spider_city = {"北京", "上海", "深圳", "广州", "杭州", "成都", "武汉", "南京", "西安", "重庆", "苏州", "长沙", "佛山", "郑州", "东莞", }
start_list = [{'city': city, 'thirdJobType': job} for city in full_spider_city for job in job_types] + \
             [{'city': city, 'thirdJobType': ''} for city in (city_list - full_spider_city)]
