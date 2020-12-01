/*
MySQL Backup
Source Server Version: 5.7.17
Source Database: myshop
Date: 2020/6/19 08:48:53
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
--  Table structure for `cookerlist`
-- ----------------------------
DROP TABLE IF EXISTS `cookerlist`;
CREATE TABLE `cookerlist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `imgurl` varchar(255) DEFAULT NULL,
  `cookname` varchar(255) DEFAULT NULL,
  `cookdescribe` varchar(255) DEFAULT NULL,
  `cooklable` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `lunboimg`
-- ----------------------------
DROP TABLE IF EXISTS `lunboimg`;
CREATE TABLE `lunboimg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `imgurl` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `tbdrink`
-- ----------------------------
DROP TABLE IF EXISTS `tbdrink`;
CREATE TABLE `tbdrink` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `proname` varchar(255) DEFAULT NULL,
  `price` varchar(255) DEFAULT NULL,
  `imgurl` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `tbguestbook`
-- ----------------------------
DROP TABLE IF EXISTS `tbguestbook`;
CREATE TABLE `tbguestbook` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `tel` varchar(255) DEFAULT NULL,
  `contents` varchar(255) DEFAULT NULL,
  `createtime` varchar(255) DEFAULT NULL,
  `isshow` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `tbliuyan`
-- ----------------------------
DROP TABLE IF EXISTS `tbliuyan`;
CREATE TABLE `tbliuyan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `msg1` varchar(255) DEFAULT NULL,
  `neirong` varchar(255) DEFAULT NULL,
  `ctime` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `tbmember`
-- ----------------------------
DROP TABLE IF EXISTS `tbmember`;
CREATE TABLE `tbmember` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `truename` varchar(255) DEFAULT NULL,
  `tel` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `tbnews`
-- ----------------------------
DROP TABLE IF EXISTS `tbnews`;
CREATE TABLE `tbnews` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `author` varchar(100) DEFAULT NULL,
  `contents` text,
  `createtime` varchar(100) DEFAULT NULL,
  `typeid` varchar(11) DEFAULT NULL,
  `source` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=104 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `tborderhead`
-- ----------------------------
DROP TABLE IF EXISTS `tborderhead`;
CREATE TABLE `tborderhead` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `orderid` varchar(255) DEFAULT NULL,
  `sname` varchar(255) DEFAULT NULL,
  `stel` varchar(255) DEFAULT NULL,
  `saddress` varchar(255) DEFAULT NULL,
  `sumprice` decimal(11,0) DEFAULT '0',
  `memberid` int(11) DEFAULT NULL,
  `ctime` varchar(255) DEFAULT NULL,
  `ptime` varchar(255) DEFAULT NULL,
  `memo` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `orderid` (`orderid`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `tborderitems`
-- ----------------------------
DROP TABLE IF EXISTS `tborderitems`;
CREATE TABLE `tborderitems` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `orderid` varchar(255) DEFAULT NULL,
  `proid` int(11) DEFAULT NULL,
  `proname` varchar(255) DEFAULT NULL,
  `price` decimal(10,0) DEFAULT NULL,
  `procount` int(11) DEFAULT NULL,
  `imgurl` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_order` (`orderid`),
  KEY `fk_proid` (`proid`),
  CONSTRAINT `fk_order` FOREIGN KEY (`orderid`) REFERENCES `tborderhead` (`orderid`),
  CONSTRAINT `fk_proid` FOREIGN KEY (`proid`) REFERENCES `tbproduct` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `tbproduct`
-- ----------------------------
DROP TABLE IF EXISTS `tbproduct`;
CREATE TABLE `tbproduct` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `proname` varchar(255) DEFAULT NULL,
  `price` decimal(10,0) DEFAULT NULL,
  `brief` varchar(255) DEFAULT NULL,
  `descriptions` text,
  `address` varchar(255) DEFAULT NULL,
  `istop` int(11) DEFAULT '0',
  `isstar` int(11) DEFAULT '0',
  `imgurl` varchar(255) DEFAULT NULL,
  `typeid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `tbroom`
-- ----------------------------
DROP TABLE IF EXISTS `tbroom`;
CREATE TABLE `tbroom` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `proname` varchar(255) DEFAULT NULL,
  `price` decimal(10,0) DEFAULT NULL,
  `brief` text,
  `imgurl` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `tbshoppingcar`
-- ----------------------------
DROP TABLE IF EXISTS `tbshoppingcar`;
CREATE TABLE `tbshoppingcar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sessionid` varchar(32) DEFAULT NULL,
  `proname` varchar(255) DEFAULT NULL,
  `proid` int(11) DEFAULT NULL,
  `procount` int(11) DEFAULT NULL,
  `ctime` varchar(255) DEFAULT NULL,
  `imgurl` varchar(255) DEFAULT NULL,
  `price` decimal(10,0) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `tbusers`
-- ----------------------------
DROP TABLE IF EXISTS `tbusers`;
CREATE TABLE `tbusers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `truename` varchar(20) DEFAULT NULL,
  `tel` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
--  View definition for `v_order`
-- ----------------------------
DROP VIEW IF EXISTS `v_order`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_order` AS select `tborderhead`.`sname` AS `sname`,`tborderhead`.`id` AS `id`,`tborderhead`.`orderid` AS `orderid`,`tborderhead`.`stel` AS `stel`,`tborderhead`.`saddress` AS `saddress`,`tborderhead`.`sumprice` AS `sumprice`,`tborderhead`.`memberid` AS `memberid`,`tborderhead`.`ctime` AS `ctime`,`tborderhead`.`ptime` AS `ptime`,`tborderhead`.`memo` AS `memo`,`tborderitems`.`procount` AS `procount`,`tborderitems`.`price` AS `price`,`tborderitems`.`proname` AS `proname`,`tborderitems`.`proid` AS `proid`,`tborderitems`.`imgurl` AS `imgurl` from (`tborderhead` join `tborderitems` on((`tborderhead`.`orderid` = `tborderitems`.`orderid`)));

-- ----------------------------
--  Records 
-- ----------------------------
INSERT INTO `cookerlist` VALUES ('14','20200618110326.jpg','谢霆锋','通过美食不断发现这个世界的美','精品  优选  热销'), ('15','20200618110005.jpeg','陈岚舒','她认为料理不只是美好的味道，更是一种幸福的滋味','精品  优选'), ('16','20200618105906.jpeg','松久信幸','穿着“阿玛尼”的厨师，融合料理，东西结合的第一人。','精品  优选  热销'), ('18','20200618105754.jpeg','董振祥','中国烹饪大师，中国烹饪协会副会长。','精品  优选'), ('19','20200618105459.jpeg','保罗·博古斯','当今世界西餐厨艺界的领袖。','精品');
INSERT INTO `lunboimg` VALUES ('14','20200618113306.jpg'), ('15','20200618113312.jpg'), ('16','20200618113316.jpg'), ('17','20200618113322.jpg'), ('18','20200618113328.jpg');
INSERT INTO `tbdrink` VALUES ('1','啤酒','3','20200617094452.jpg','1'), ('2','冰红茶','3','20200618083610.jpg','1'), ('3','可口可乐','5','20200618083636.jpg','1'), ('4','红牛','8','20200618083657.jpg','1'), ('5','雪菲力盐汽水','6','20200618083759.jpg','1'), ('6','茶兀','5','20200618083928.jpg','1'), ('7','椰子汁','4','20200618083953.jpg','1'), ('8','雪花啤酒','3','20200618084313.jpg','2'), ('9','麒麟啤酒','6','20200618084457.jpg','2'), ('10','百威啤酒','7','20200618084543.jpg','2'), ('11','青岛原浆啤酒','8','20200618084619.jpg','2'), ('12','科罗娜','7','20200618084655.jpg','2'), ('13','哈尔滨啤酒','12','20200618084734.jpg','2'), ('14','贵州茅台','658','20200618084924.jpg','3'), ('15','洋河天之蓝','828','20200618085017.jpg','3'), ('16','五粮液','989','20200618085055.jpg','3'), ('17','剑蓝春','438','20200618085153.jpg','3'), ('18','山西杏花村','458','20200618085301.jpg','3'), ('19','洋河大曲老天蓝','67','20200618085403.jpg','3'), ('20','水井坊臻粮','504','20200618085643.jpg','3'), ('22','拉菲','638','20200618085853.jpg','4'), ('25','醉鹅娘','188','20200618090213.jpg','4'), ('26','奔富麦克斯','1588','20200618090323.jpg','4');
INSERT INTO `tbliuyan` VALUES ('1','user','tuii','送货时间太长。','2020-06-15 09:27:44'), ('2','','e2qrrr2','味道不够鲜美。','2020-06-15 09:44:46'), ('3','管理员1','fafwawfa','食材不够新鲜。','2020-06-15 09:52:09'), ('4','管理员1','dafwafa','味道不够鲜美。','2020-06-15 09:53:45'), ('5','管理员1','dwafaf','送货时间太长。','2020-06-15 09:54:20'), ('6','伍思凯','jwkafhfaw','食材不够新鲜。','2020-06-17 19:28:18'), ('7','伍思凯','jwkafhfaw','食材不够新鲜。','2020-06-17 19:28:21'), ('8','伍思凯','','','2020-06-18 18:39:45');
INSERT INTO `tbmember` VALUES ('4','user5','123456','伍思凯','15900000001','成都市高新区XX路3-3-2'), ('6','user100','123456','徐XX','15112345678','成都市温江区海科东路'), ('7','cc','123456','cawfaf','1231241','123421'), ('8','user1','123456','王五','15686456234','重庆市'), ('9','阿嘎嘎','111111','挖方','发哇嘎','发完饭'), ('10','feature','111111','1213','21321','1231'), ('11','纷纷奥尔芬','111111','我确认去','1231','王企鹅v');
INSERT INTO `tbnews` VALUES ('102','在流量时代怎样做餐饮营销','admin','2019年3月18日，由吉食道食品、申唐产业、翠宏食品、航佳食品、红灯笼食品、智琪食品六家公司共同发起，成都市食品工业协会联合主办的第四届“发现川味”中国餐饮高峰论坛及食材展在成都隆重举行。\r\n据悉，本届食材展汇聚了全国40 家餐饮业供应链企业。活动当天，全国知名餐饮品牌CEO、餐饮加盟门店企业主等上千名代表出席了餐饮高峰论坛，会上嘉宾从餐饮运营、营销、供应链等角度全方位的剖析餐饮行业当前的发展现状和行业前景。\r\n红餐作为战略合作媒体参与了本次活动，为大家进行详细的报道。','2019-03-18','1','吃哪儿网'), ('103','“不忘初心，牢记使命”主题教育工作会议召开','admin','1212','1212','1','校内新闻');
INSERT INTO `tborderhead` VALUES ('24','20200618205159015603','陈梦','13320329113','108','312','4','2020-06-18 20:51:59','2020-06-18','快一点');
INSERT INTO `tborderitems` VALUES ('43','20200618205159015603','34','脆炸鹦哥鱼','58','2','http://localhost:8000/static/uploadimg/20200618202014.jpeg'), ('44','20200618205159015603','27','砂锅鲍鱼炆鸡','128','1','http://localhost:8000/static/uploadimg/20200618200706.jpeg'), ('45','20200618205159015603','22','蜜汁烧排骨','68','1','http://localhost:8000/static/uploadimg/20200618194922.jpeg');
INSERT INTO `tbproduct` VALUES ('22','蜜汁烧排骨','68','油而不腻，入口即化','','重庆','0','0','20200618194922.jpeg','1'), ('23','烟捞银鳕鱼','88','去除鱼刺可放心食用','','重庆','0','0','20200618195310.jpeg','1'), ('24','京都扒鸭','148','采用高质量自养鸭','做法：一、将光鸭洗净，去内脏，从背部剖开，开刀背敲松鸭背，下汤罐泡五六分钟，取起用酱油上色。 二、起热油锅，将鸭炸至金黄色，取起另放在瓦锅中烧熟，并脱去大骨。三、将海参、鲍鱼、鱿鱼、冬菇、干贝等海味洗净，切块下锅，与蚝油、味粉同焖十五分钟，取起摆成八卦形，用碗扣好，将鸭放在上面，上笼再蒸。','重庆','0','0','20200618195734.jpeg','1'), ('25','太极鸳鸯汤','48','香甜可口','蛋面200克，鸡肉50克，冬菇件少许，千层塔叶5克，胡萝卜丝适量，香茅适量。\r\n白糖少许，鱼露1汤匙，鸡汤0.5升，胡椒粉少许。','重庆','0','0','20200618200057.jpeg','1'), ('26','红烧蟹钳翅','238','采用野生蟹食材','红烧螃蟹是喜爱吃螃蟹的中国的一种著名菜肴，菜系上属于沪菜。其味道鲜香可口，色香味俱全，做法较容易。','重庆','0','0','20200618200513.jpeg','1'), ('27','砂锅鲍鱼炆鸡','128','补气养血，升阳益胃','本品具有补气养血，升阳益胃的功效。适用于劳伤虚损，身瘦体弱、食少泄泻、惊悸失眠。','重庆','0','0','20200618200706.jpeg','1'), ('28','金汤小米辽参','128','鲜味十足','海参与小米均为秋冬进补的良品，小米加入浓汤，鲜味十足，自然的黏稠度刚好包裹了海参，使之非常入味。温补的疗效也适宜秋冬食用，加入了适当的上汤调味，让高汤鲜美的味道更为凸显。','重庆','0','0','20200618200857.jpeg','1'), ('29','青芥焗龙虾','258','自养小龙虾','青芥沙拉拌匀上撒黑芝麻','重庆','0','0','20200618201143.jpeg','1'), ('30','酸辣汁焗明虾','68','采用自养小龙虾','香菜和蒜头切成细末，加入红尖椒片、鱼露、柠檬汁和糖，搅\r\n拌均匀，淋在生虾上即可。','重庆','0','0','20200618201323.jpeg','1'), ('31','松茸菌鸡汁滑豆腐','28','豫菜菜系之一','锅内加入清鸡汤烧开，加入盐、味精、鸡精、鸡汁调味，用生粉勾芡， 加入南瓜汁调色，封上鸡油，淋于装好的盘中即可。','重庆','0','0','20200618201538.jpeg','1'), ('32','碧玉炒辽参','98','玉环葱爆辽参','净锅上火，放入适量色拉油烧热，下入马耳朵葱炒香，再放入蚝油炒匀，倒入辽参，掺少许高汤，调入精盐、白糖、味精','重庆','0','0','20200618201701.jpeg','1'), ('33','高汤浸芥胆','38','提神醒脑，解除疲劳','把高汤煲开把芥菜放下去大火煲开小火煲20分钟调味即可。','重庆','0','0','20200618201837.jpeg','1'), ('34','脆炸鹦哥鱼','58','肉质鲜嫩','热菜、咸鲜、煎、十分钟、简单难度','重庆','0','0','20200618202014.jpeg','1'), ('35','青椒泡东星','88','家常菜品','','重庆','0','0','20200618202125.jpeg','1');
INSERT INTO `tbroom` VALUES ('7','翠竹居','2999','一往无前四海皆春','20200618132416.jpg'), ('8','花好月圆','4998','还作江南会bai，翻疑梦里逢。','20200618132635.jpg'), ('9','功成名就','2888','春风得意马蹄疾，一日看尽长安花。','20200618132838.jpg'), ('10','祥瑞苑','2888','天生我才必有用，千金散尽还复来','20200618133130.jpeg'), ('11','秋菊阁','3999','粗缯大bai布裹生涯，腹有诗书气自华。','20200618133257.jpg'), ('12','福寿无疆','3999','千古风流今在此，万里功名莫放休。','20200618133441.jpg'), ('13','揽月轩','5200','在天愿做比翼鸟，在地愿为连理枝。','20200618134417.jpg');
INSERT INTO `tbusers` VALUES ('1','admin','123456','管理员1','15397600032','北京复兴门外大街10086号'), ('2','user','123456','张三','15397600032','北京复兴门外大街10086号'), ('7','feifei','123456','郭靖','15397600032','北京复兴门外大街10086号'), ('8','xiangyang','123456','刘湘','15397600032','襄阳XX号'), ('9','mr','123456','蓉兔子','15397600032','北京ZXXX号');
