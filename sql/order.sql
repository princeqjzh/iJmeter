CREATE DATABASE  IF NOT EXISTS `jmeter_class`;
USE `jmeter_class`;

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- LOCK TABLES `user` WRITE;
-- INSERT INTO `user` VALUES (1,'user1', '123456'),(2,'user1', '123456'),(3,'user1', '123456'),(4,'user1', '123456'),(5,'user1', '123456'),(6,'user1', '123456');
-- UNLOCK TABLES;



