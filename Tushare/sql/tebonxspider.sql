/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50727
Source Host           : localhost:3306
Source Database       : tebonxspider

Target Server Type    : MYSQL
Target Server Version : 50727
File Encoding         : 65001

Date: 2019-08-21 08:32:02
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for cashflow_basic
-- ----------------------------
DROP TABLE IF EXISTS `cashflow_basic`;
CREATE TABLE `cashflow_basic` (
  `index` bigint(20) DEFAULT NULL,
  `code` text COMMENT '代码',
  `name` text COMMENT '名称',
  `cf_sales` double DEFAULT NULL COMMENT '经营现金净流量对销售收入比率',
  `rateofreturn` double DEFAULT NULL COMMENT '资产的经营现金流量回报率',
  `cf_nm` double DEFAULT NULL COMMENT '经营现金净流量与净利润的比率',
  `cf_liabilities` double DEFAULT NULL COMMENT '经营现金净流量对负债比率',
  `cashflowratio` double DEFAULT NULL COMMENT '现金流量比率',
  KEY `ix_cashflow_basic_index` (`index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT '现金流量';

-- ----------------------------
-- Table structure for deptpay_basic
-- ----------------------------
DROP TABLE IF EXISTS `deptpay_basic`;
CREATE TABLE `deptpay_basic` (
  `index` bigint(20) DEFAULT NULL,
  `code` text COMMENT '代码',
  `name` text COMMENT '名称',
  `currentratio` text COMMENT '流动比率',
  `quickratio` text COMMENT '速动比率',
  `cashratio` text COMMENT '现金比率',
  `icratio` text COMMENT '利息支付倍数',
  `sheqratio` text COMMENT '股东权益比率',
  `adratio` text COMMENT '股东权益增长率',
  KEY `ix_deptpay_basic_index` (`index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT '偿债能力';

-- ----------------------------
-- Table structure for growth_basic
-- ----------------------------
DROP TABLE IF EXISTS `growth_basic`;
CREATE TABLE `growth_basic` (
  `index` bigint(20) DEFAULT NULL,
  `code` text COMMENT '代码',
  `name` text COMMENT '名称',
  `mbrg` double DEFAULT NULL COMMENT '主营业务收入增长率(%)',
  `nprg` double DEFAULT NULL COMMENT '净利润增长率(%)',
  `nav` double DEFAULT NULL COMMENT '净资产增长率',
  `targ` double DEFAULT NULL COMMENT '总资产增长率',
  `epsg` double DEFAULT NULL COMMENT '每股收益增长率',
  `seg` double DEFAULT NULL COMMENT '股东权益增长率',
  KEY `ix_growth_basic_index` (`index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT '成长能力';

-- ----------------------------
-- Table structure for operation_basic
-- ----------------------------
DROP TABLE IF EXISTS `operation_basic`;
CREATE TABLE `operation_basic` (
  `index` bigint(20) DEFAULT NULL,
  `code` text COMMENT '代码',
  `name` text COMMENT '名称',
  `arturnover` double DEFAULT NULL COMMENT '应收账款周转率(次)',
  `arturndays` double DEFAULT NULL COMMENT '应收账款周转天数(天)',
  `inventory_turnover` double DEFAULT NULL COMMENT '存货周转率(次)',
  `inventory_days` double DEFAULT NULL COMMENT '存货周转天数(天)',
  `currentasset_turnover` double DEFAULT NULL COMMENT '流动资产周转率(次)',
  `currentasset_days` double DEFAULT NULL COMMENT '流动资产周转天数(天)',
  KEY `ix_operation_basic_index` (`index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT '营运能力';

-- ----------------------------
-- Table structure for profit_basic
-- ----------------------------
DROP TABLE IF EXISTS `profit_basic`;
CREATE TABLE `profit_basic` (
  `index` bigint(20) DEFAULT NULL,
  `code` text COMMENT '代码',
  `name` text COMMENT '名称',
  `roe` double DEFAULT NULL COMMENT '净资产收益率(%)',
  `net_profit_ratio` double DEFAULT NULL COMMENT '净利率(%)',
  `gross_profit_rate` double DEFAULT NULL COMMENT '毛利率(%)',
  `net_profits` double DEFAULT NULL COMMENT '净利润(万元)',
  `eps` double DEFAULT NULL COMMENT '每股收益',
  `business_income` double DEFAULT NULL COMMENT '营业收入(百万元)',
  `bips` double DEFAULT NULL COMMENT '每股主营业务收入(元)',
  KEY `ix_profit_basic_index` (`index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT '盈利能力';

-- ----------------------------
-- Table structure for resport_basic
-- ----------------------------
DROP TABLE IF EXISTS `resport_basic`;
CREATE TABLE `resport_basic` (
  `index` bigint(20) DEFAULT NULL,
  `code` text COMMENT '代码',
  `name` text COMMENT '名称',
  `eps` double DEFAULT NULL COMMENT '每股收益',
  `eps_yoy` double DEFAULT NULL COMMENT '每股收益同比(%)',
  `bvps` double DEFAULT NULL COMMENT '每股净资产',
  `roe` double DEFAULT NULL COMMENT '净资产收益率(%)',
  `epcf` double DEFAULT NULL COMMENT '每股现金流量(元)',
  `net_profits` double DEFAULT NULL COMMENT '净利润(万元)',
  `profits_yoy` double DEFAULT NULL COMMENT '净利润同比(%)',
  `distrib` text COMMENT '分配方案',
  `report_date` text COMMENT '发布日期',
  KEY `ix_resport_basic_index` (`index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT '业绩报告（主表）';

-- ----------------------------
-- Table structure for stock_basic
-- ----------------------------
DROP TABLE IF EXISTS `stock_basic`;
CREATE TABLE `stock_basic` (
  `code` text COMMENT '代码',
  `name` text COMMENT '名称',
  `industry` text COMMENT '所属行业',
  `area` text COMMENT '地区',
  `pe` double DEFAULT NULL COMMENT '市盈率',
  `outstanding` double DEFAULT NULL COMMENT '流通股本(亿)',
  `totals` double DEFAULT NULL COMMENT '总股本(亿)',
  `totalAssets` double DEFAULT NULL COMMENT '总资产(万)',
  `liquidAssets` double DEFAULT NULL COMMENT '流动资产',
  `fixedAssets` double DEFAULT NULL COMMENT '固定资产',
  `reserved` double DEFAULT NULL COMMENT '公积金',
  `reservedPerShare` double DEFAULT NULL COMMENT '每股公积金',
  `esp` double DEFAULT NULL COMMENT '每股收益',
  `bvps` double DEFAULT NULL COMMENT '每股净资',
  `pb` double DEFAULT NULL COMMENT '市净率',
  `timeToMarket` bigint(20) DEFAULT NULL COMMENT '上市日期',
  `undp` double DEFAULT NULL COMMENT '未分利润',
  `perundp` double DEFAULT NULL COMMENT '每股未分配',
  `rev` double DEFAULT NULL COMMENT '收入同比(%)',
  `profit` double DEFAULT NULL COMMENT '利润同比(%)',
  `gpr` double DEFAULT NULL COMMENT '毛利率(%)',
  `npr` double DEFAULT NULL COMMENT '净利润率(%)',
  `holders` double DEFAULT NULL COMMENT '股东人数'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT '股票列表';
