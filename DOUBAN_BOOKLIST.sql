/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50709
 Source Host           : localhost
 Source Database       : DOUBAN_DATA

 Target Server Type    : MySQL
 Target Server Version : 50709
 File Encoding         : utf-8

 Date: 05/24/2016 00:34:48 AM
*/

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
  `book_tag` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

SET FOREIGN_KEY_CHECKS = 1;
