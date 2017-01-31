DROP TABLE IF EXISTS `dim_country`;

CREATE TABLE `dim_country` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `country_name` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `dim_country` WRITE;


INSERT INTO `dim_country` (`id`, `country_name`)
VALUES
	(1,'Ireland'),
	(2,'United Kingdom');

UNLOCK TABLES;

DROP TABLE IF EXISTS `dim_county`;

CREATE TABLE `dim_county` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `county_name` varchar(60) NOT NULL DEFAULT '',
  `country_id` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `country_id` (`country_id`),
  CONSTRAINT `dim_county_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `dim_country` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `dim_county` WRITE;

INSERT INTO `dim_county` (`id`, `county_name`, `country_id`)
VALUES
	(1,'Antrim',2),
	(2,'Armagh',2),
	(3,'Carlow',1),
	(4,'Cavan',1),
	(5,'Clare',1),
	(6,'Cork',1),
	(7,'Donegal',1),
	(8,'Down',2),
	(9,'Dublin',1),
	(10,'Galway',1),
	(11,'Kerry',1),
	(12,'Kildare',1),
	(13,'Kilkenny',1),
	(14,'Laois',1),
	(15,'Leitrim',1),
	(16,'Limerick',1),
	(17,'Derry',2),
	(18,'Longford',1),
	(19,'Louth',1),
	(20,'Mayo',1),
	(21,'Meath',1),
	(22,'Monaghan',1),
	(23,'Offaly',1),
	(24,'Roscommon',1),
	(25,'Sligo',1),
	(26,'Tipperary',1),
	(27,'Tyrone',2),
	(28,'Waterford',1),
	(29,'Westmeath',1),
	(30,'Wexford',1),
	(31,'Wicklow',1),
	(32,'Fermanagh',2);

UNLOCK TABLES;

DROP TABLE IF EXISTS `dim_date`;

CREATE TABLE `dim_date` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `day` varchar(2) NOT NULL DEFAULT '',
  `month` varchar(2) NOT NULL DEFAULT '',
  `year` varchar(4) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `dim_property`;

CREATE TABLE `dim_property` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `address` text NOT NULL,
  `county_id` int(11) unsigned NOT NULL,
  `country_id` int(11) unsigned NOT NULL,
  `description` text NOT NULL,
  PRIMARY KEY (`id`),
  KEY `county_id` (`county_id`),
  KEY `country_id` (`country_id`),
  CONSTRAINT `dim_property_ibfk_1` FOREIGN KEY (`county_id`) REFERENCES `dim_county` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `dim_property_ibfk_2` FOREIGN KEY (`country_id`) REFERENCES `dim_country` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `fact_country`;

CREATE TABLE `fact_country` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `country_id` int(11) unsigned NOT NULL,
  `total_number_of_sales` int(11) NOT NULL,
  `average_sale_price` decimal(15,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `country_id` (`country_id`),
  CONSTRAINT `fact_country_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `dim_country` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `fact_county`;

CREATE TABLE `fact_county` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `county_id` int(11) unsigned NOT NULL,
  `total_number_of_sales` int(11) NOT NULL,
  `average_sale_price` decimal(15,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `county_id` (`county_id`),
  CONSTRAINT `fact_county_ibfk_1` FOREIGN KEY (`county_id`) REFERENCES `dim_county` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `fact_rent`;

CREATE TABLE `fact_rent` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `county_id` int(11) unsigned NOT NULL,
  `total_properties_for_rent` int(11) unsigned NOT NULL,
  `average_rent_price` decimal(10,2) unsigned NOT NULL,
  `max_rent_price` decimal(10,2) NOT NULL,
  `min_rent_price` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `fact_sales`;

CREATE TABLE `fact_sales` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `date_id` int(11) unsigned NOT NULL,
  `property_id` int(11) unsigned NOT NULL,
  `price` decimal(15,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `date_id` (`date_id`),
  KEY `property_id` (`property_id`),
  CONSTRAINT `fact_sales_ibfk_1` FOREIGN KEY (`date_id`) REFERENCES `dim_date` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fact_sales_ibfk_2` FOREIGN KEY (`property_id`) REFERENCES `dim_property` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `fact_town`;

CREATE TABLE `fact_town` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `town_name` varchar(30) NOT NULL DEFAULT '',
  `total_number_of_sales` int(11) DEFAULT '0',
  `average_sale_price` decimal(10,2) DEFAULT '0.00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `fact_year`;

CREATE TABLE `fact_year` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `year` int(11) NOT NULL,
  `county_id` int(11) unsigned NOT NULL,
  `total_number_of_sales` int(11) NOT NULL,
  `average_sale_price` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
