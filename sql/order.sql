CREATE DATABASE  IF NOT EXISTS `order`;
USE `order`;

DROP TABLE IF EXISTS `categories`;
CREATE TABLE `categories` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `cname` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

LOCK TABLES `categories` WRITE;
INSERT INTO `categories` VALUES (1,'北京菜'),(2,'新疆菜'),(3,'朝鲜族菜'),(4,'四川风味菜'),(10,'上海菜'),(11,'河南菜');
UNLOCK TABLES;

DROP TABLE IF EXISTS `menus`;
CREATE TABLE `menus` (
  `mid` int(11) NOT NULL AUTO_INCREMENT,
  `cid` int(11) DEFAULT NULL COMMENT 'category id',
  `mname` varchar(255) DEFAULT NULL,
  `price` float(11,2) DEFAULT NULL,
  PRIMARY KEY (`mid`),
  UNIQUE KEY `id_UNIQUE` (`mid`),
  KEY `cid_idx` (`cid`),
  CONSTRAINT `cid` FOREIGN KEY (`cid`) REFERENCES `categories` (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

LOCK TABLES `menus` WRITE;
INSERT INTO `menus` VALUES (6,3,'辣白菜',11.30),(9,1,'卤煮火烧',23.00),(10,2,'红柳大串',15.00),(11,4,'宫保鸡丁',20.00),(13,10,'红豆冰山',23.50),(14,10,'软炸里脊',31.00),(16,1,'北京烤鸭',98.00),(18,4,'麻婆豆腐',36.01),(19,1,'红烧猪手',26.29),(20,1,'豆汁儿',1.50);
UNLOCK TABLES;


