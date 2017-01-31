SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS `counties`;

CREATE TABLE `counties` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `county_name` varchar(60) NOT NULL DEFAULT '',
  `country_id` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `country_id` (`country_id`),
  CONSTRAINT `counties_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `countries` (`country_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `counties` WRITE;

INSERT INTO `counties` (`id`, `county_name`, `country_id`)
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
	(32,'Fermanagh',2),
	(38,'London',2),
	(39,'Bedfordshire',2),
	(40,'Buckinghamshire',2),
	(41,'Cambridgeshire',2),
	(42,'Cheshire',2),
	(43,'Cornwall and Isles of Scilly',2),
	(44,'Cumbria',2),
	(45,'Derbyshire',2),
	(46,'Devon',2),
	(47,'Dorset',2),
	(48,'Durham',2),
	(49,'East Sussex',2),
	(50,'Essex',2),
	(51,'Gloucestershire',2),
	(52,'Greater London',2),
	(53,'Greater Manchester',2),
	(54,'Hampshire',2),
	(55,'Hertfordshire',2),
	(56,'Kent',2),
	(57,'Lancashire',2),
	(58,'Leicestershire',2),
	(59,'Lincolnshire',2),
	(60,'Merseyside',2),
	(61,'Norfolk',2),
	(62,'North Yorkshire',2),
	(63,'Northamptonshire',2),
	(64,'Northumberland',2),
	(65,'Nottinghamshire',2),
	(66,'Oxfordshire',2),
	(67,'Shropshire',2),
	(68,'Somerset',2),
	(69,'South Yorkshire',2),
	(70,'Staffordshire',2),
	(71,'Suffolk',2),
	(72,'Surrey',2),
	(73,'Tyne and Wear',2),
	(74,'Warwickshire',2),
	(75,'West Midlands',2),
	(76,'West Sussex',2),
	(77,'West Yorkshire',2),
	(78,'Wiltshire',2),
	(79,'Worcestershire',2),
	(80,'Flintshire',2),
	(81,'Glamorgan',2),
	(82,'Merionethshire',2),
	(83,'Monmouthshire',2),
	(84,'Montgomeryshire',2),
	(85,'Pembrokeshire',2),
	(86,'Radnorshire',2),
	(87,'Anglesey',2),
	(88,'Breconshire',2),
	(89,'Caernarvonshire',2),
	(90,'Cardiganshire',2),
	(91,'Carmarthenshire',2),
	(92,'Denbighshire',2),
	(93,'Kirkcudbrightshire',2),
	(94,'Lanarkshire',2),
	(95,'Midlothian',2),
	(96,'Moray',2),
	(97,'Nairnshire',2),
	(98,'Orkney',2),
	(99,'Peebleshire',2),
	(100,'Perthshire',2),
	(101,'Renfrewshire',2),
	(102,'Ross & Cromarty',2),
	(103,'Roxburghshire',2),
	(104,'Selkirkshire',2),
	(105,'Shetland',2),
	(106,'Stirlingshire',2),
	(107,'Sutherland',2),
	(108,'West Lothian',2),
	(109,'Wigtownshire',2),
	(110,'Aberdeenshire',2),
	(111,'Angus',2),
	(112,'Argyll',2),
	(113,'Ayrshire',2),
	(114,'Banffshire',2),
	(115,'Berwickshire',2),
	(116,'Bute',2),
	(117,'Caithness',2),
	(118,'Clackmannanshire',2),
	(119,'Dumfriesshire',2),
	(120,'Dumbartonshire',2),
	(121,'East Lothian',2),
	(122,'Fife',2),
	(123,'Inverness',2),
	(124,'Kincardineshire',2),
	(125,'Kinross-shire',2);

UNLOCK TABLES;

DROP TABLE IF EXISTS `countries`;

CREATE TABLE `countries` (
  `country_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `country_name` varchar(20) NOT NULL DEFAULT '',
  PRIMARY KEY (`country_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `countries` WRITE;

INSERT INTO `countries` (`country_id`, `country_name`)
VALUES
	(1,'Ireland'),
	(2,'United Kingdom');

UNLOCK TABLES;

DROP TABLE IF EXISTS `properties`;

CREATE TABLE `properties` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `date_time` datetime NOT NULL,
  `address` text NOT NULL,
  `postcode` varchar(10) DEFAULT '',
  `county_id` int(11) unsigned NOT NULL,
  `price` decimal(15,2) NOT NULL,
  `description` text NOT NULL,
  `country_id` int(11) unsigned NOT NULL,
  `sale_type` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `country_id` (`country_id`),
  KEY `sale_type` (`sale_type`),
  KEY `county_id` (`county_id`),
  CONSTRAINT `properties_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `countries` (`country_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `properties_ibfk_2` FOREIGN KEY (`sale_type`) REFERENCES `property_sale_types` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `properties_ibfk_3` FOREIGN KEY (`county_id`) REFERENCES `counties` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `property_sale_types`;

CREATE TABLE `property_sale_types` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `sale_type` varchar(11) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `property_sale_types` WRITE;

INSERT INTO `property_sale_types` (`id`, `sale_type`)
VALUES
	(1,'Sold'),
	(2,'For Sale'),
	(3,'Sale Agreed'),
	(4,'For Rent');

UNLOCK TABLES;

DROP TABLE IF EXISTS `towns`;

CREATE TABLE `towns` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `town_name` varchar(20) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `towns` WRITE;

INSERT INTO `towns` (`id`, `town_name`)
VALUES
	(1,'Abbeyfeale'),
	(2,'Achill Island'),
	(3,'Adare'),
	(4,'Antrim Town'),
	(5,'Ardmore'),
	(6,'Arklow'),
	(7,'Armagh'),
	(8,'Ashbourne'),
	(9,'Athenry'),
	(10,'Athlone'),
	(11,'Athy'),
	(12,'Balbriggan'),
	(13,'Ballina'),
	(14,'Ballincollig'),
	(15,'Ballybunion'),
	(16,'Ballyfermot'),
	(17,'Ballymena'),
	(18,'Banbridge'),
	(19,'Bandon'),
	(20,'Bangor'),
	(21,'Bantry'),
	(22,'Beara'),
	(23,'Belfast'),
	(24,'Birr'),
	(25,'Bishopstown'),
	(26,'Blackpool'),
	(27,'Blackrock'),
	(28,'Blanchardstown'),
	(29,'Blarney'),
	(30,'Bray'),
	(31,'Cabra'),
	(32,'Cahir'),
	(33,'Carlow'),
	(34,'Carrick-on-Shannon'),
	(35,'Carrick-On-Suir'),
	(36,'Carrickfergus'),
	(37,'Carrigaline'),
	(38,'Cashel'),
	(39,'Castlebar'),
	(40,'Castleisland'),
	(41,'Castlereagh'),
	(42,'Cavan'),
	(43,'Celbridge'),
	(44,'Charleville'),
	(45,'Clane'),
	(46,'Clonakilty'),
	(47,'Clondalkin'),
	(48,'Clonmel'),
	(49,'Clontarf'),
	(50,'Cobh'),
	(51,'Coleraine'),
	(52,'Cookstown'),
	(53,'Coolock'),
	(54,'Cork City'),
	(55,'Craigavon'),
	(56,'Derry'),
	(57,'Dingle'),
	(58,'Donabate'),
	(59,'Donegal'),
	(60,'Doolin'),
	(61,'Douglas'),
	(62,'Downpatrick'),
	(63,'Drogheda'),
	(64,'Drumcondra'),
	(65,'Dublin City'),
	(66,'Dun Laoghaire'),
	(67,'Dunboyne'),
	(68,'Dundalk'),
	(69,'Dungannon'),
	(70,'Dungarvan'),
	(71,'Dunmanway'),
	(72,'Edenderry'),
	(73,'Ennis'),
	(74,'Enniscorthy'),
	(75,'Enniskillen'),
	(76,'Fermoy'),
	(77,'Finglas'),
	(78,'Galway City'),
	(79,'Glanmire'),
	(80,'Glasnevin'),
	(81,'Gorey'),
	(82,'Gort'),
	(83,'Greystones'),
	(84,'Holywood'),
	(85,'Howth'),
	(86,'Inchicore'),
	(87,'Inishowen'),
	(88,'Kanturk'),
	(89,'Kenmare'),
	(90,'Kildare'),
	(91,'Kilkenny'),
	(92,'Killarney'),
	(93,'Killorglin'),
	(94,'Kinsale'),
	(95,'Knocknaheeny'),
	(96,'Larne'),
	(97,'Leixlip'),
	(98,'Letterkenny'),
	(99,'Limavady'),
	(100,'Limerick City'),
	(101,'Lisburn'),
	(102,'Lismore'),
	(103,'Listowel'),
	(104,'Longford'),
	(105,'Loughrea'),
	(106,'Lucan'),
	(107,'Lurgan'),
	(108,'Macroom'),
	(109,'Magherafelt'),
	(110,'Malahide'),
	(111,'Mallow'),
	(112,'Maynooth'),
	(113,'Midleton'),
	(114,'Millstreet'),
	(115,'Mitchelstown'),
	(116,'Monaghan'),
	(117,'Mullingar'),
	(118,'Naas'),
	(119,'Navan'),
	(120,'Nenagh'),
	(121,'New Ross'),
	(122,'Newbridge'),
	(123,'Newcastle West'),
	(124,'Newry'),
	(125,'Newtownabbey'),
	(126,'Newtownards'),
	(127,'Omagh'),
	(128,'Palmerstown'),
	(129,'Port Laoise'),
	(130,'Portadown'),
	(131,'Portarlington'),
	(132,'Portmarnock'),
	(133,'Portrush'),
	(134,'Portumna'),
	(135,'Ranelagh'),
	(136,'Rathcoole'),
	(137,'Rathfarnham'),
	(138,'Rathmines'),
	(139,'Roscommon'),
	(140,'Roscrea'),
	(141,'Rush'),
	(142,'Santry'),
	(143,'Shankill'),
	(144,'Shannon'),
	(145,'Skerries'),
	(146,'Skibbereen'),
	(147,'Slane'),
	(148,'Sligo'),
	(149,'Stillorgan'),
	(150,'Strabane'),
	(151,'Swords'),
	(152,'Tallaght'),
	(153,'Templemore'),
	(154,'Terenure'),
	(155,'Thurles'),
	(156,'Tipperary'),
	(157,'Togher'),
	(158,'Tralee'),
	(159,'Tramore'),
	(160,'Trim'),
	(161,'Tuam'),
	(162,'Tullamore'),
	(163,'Walkinstown'),
	(164,'Waterford City'),
	(165,'Westport'),
	(166,'Wexford'),
	(167,'Wicklow'),
	(168,'Youghal');

UNLOCK TABLES;

SET FOREIGN_KEY_CHECKS = 1;
