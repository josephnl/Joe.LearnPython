

CREATE DATABASE `DOUBAN_DATA` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */;
SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;
-- ----------------------------
--  Table structure for `DOUBAN_BOOKLIST`
-- ----------------------------
DROP TABLE IF EXISTS `DOUBAN_BOOKLIST`;
CREATE TABLE `DOUBAN_BOOKLIST` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `rating` int(10) unsigned NOT NULL,
  `comment_nums` int(10) unsigned NOT NULL,
  `buy_info` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `brief_info` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `author_info` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `trans_info` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `publishing` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `pub_time` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `list_price` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`ID`),
) DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

SET FOREIGN_KEY_CHECKS = 1;
