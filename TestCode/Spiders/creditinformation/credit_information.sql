/*
Navicat MySQL Data Transfer

Source Server         : zgcollection
Source Server Version : 50720
Source Host           : 172.16.100.23:3306
Source Database       : credit_information

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2019-01-17 15:22:05
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for credit_data
-- ----------------------------
DROP TABLE IF EXISTS `credit_data`;
CREATE TABLE `credit_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `dataform` varchar(63) DEFAULT NULL COMMENT 'dataform',
  `entname` varchar(63) DEFAULT NULL COMMENT 'entname',
  `judauth` varchar(63) DEFAULT NULL COMMENT 'judAuth',
  `judauth_cn` varchar(63) DEFAULT NULL COMMENT 'judAuth_CN',
  `juddate` varchar(255) DEFAULT NULL COMMENT 'judDate',
  `lastmodifiedtime` datetime DEFAULT NULL COMMENT 'lastModifiedTime',
  `noticecontent` varchar(600) DEFAULT NULL COMMENT 'noticeContent',
  `noticedate` varchar(20) DEFAULT NULL,
  `noticeid` varchar(100) DEFAULT NULL COMMENT 'noticeId',
  `noticeno` varchar(11) DEFAULT NULL COMMENT 'noticeNO',
  `noticetitle` varchar(255) DEFAULT NULL COMMENT 'noticeTitle',
  `noticetype` int(11) DEFAULT NULL COMMENT 'noticeType',
  `simplecancelurl` varchar(255) DEFAULT NULL COMMENT 'simpleCancelUrl',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2102 DEFAULT CHARSET=utf8 COMMENT='经营异常数据名单';
