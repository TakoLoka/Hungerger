CREATE DATABASE  IF NOT EXISTS `hungerger` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `hungerger`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: hungerger
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin_user`
--

DROP TABLE IF EXISTS `admin_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin_user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `avatar` varchar(45) DEFAULT NULL,
  `password` varchar(255) NOT NULL,
  `user_type` varchar(255) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_id_UNIQUE` (`user_id`),
  UNIQUE KEY `username_UNIQUE` (`username`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_user`
--

LOCK TABLES `admin_user` WRITE;
/*!40000 ALTER TABLE `admin_user` DISABLE KEYS */;
INSERT INTO `admin_user` VALUES (1,'TakoLoka','tako@mail.com','Tako','Loka',NULL,'TakoLoka','1'),(2,'NewMem','newmem@mail.com','New','Mem','None','NewMem','1');
/*!40000 ALTER TABLE `admin_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comments` (
  `user_id` int NOT NULL,
  `rec_id` int NOT NULL,
  `comm_date` datetime NOT NULL,
  `comm_content` varchar(100) NOT NULL,
  PRIMARY KEY (`user_id`,`rec_id`),
  UNIQUE KEY `user_id_UNIQUE` (`user_id`),
  UNIQUE KEY `rec_id_UNIQUE` (`rec_id`),
  CONSTRAINT `comm_rec_id` FOREIGN KEY (`rec_id`) REFERENCES `recipes` (`rec_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `comm_user_id` FOREIGN KEY (`user_id`) REFERENCES `reg_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dm`
--

DROP TABLE IF EXISTS `dm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dm` (
  `follower_id` int NOT NULL,
  `following_id` int NOT NULL,
  `dm_content` varchar(500) NOT NULL,
  PRIMARY KEY (`follower_id`,`following_id`),
  KEY `ing_id_idx` (`following_id`),
  CONSTRAINT `dm_ing_id` FOREIGN KEY (`following_id`) REFERENCES `reg_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `dm_wer_id` FOREIGN KEY (`follower_id`) REFERENCES `reg_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dm`
--

LOCK TABLES `dm` WRITE;
/*!40000 ALTER TABLE `dm` DISABLE KEYS */;
/*!40000 ALTER TABLE `dm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `follows`
--

DROP TABLE IF EXISTS `follows`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `follows` (
  `follower_id` int NOT NULL,
  `following_id` int NOT NULL,
  PRIMARY KEY (`follower_id`,`following_id`),
  KEY `ing_id_idx` (`following_id`),
  CONSTRAINT `ing_id` FOREIGN KEY (`following_id`) REFERENCES `reg_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `wer_id` FOREIGN KEY (`follower_id`) REFERENCES `reg_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `follows`
--

LOCK TABLES `follows` WRITE;
/*!40000 ALTER TABLE `follows` DISABLE KEYS */;
/*!40000 ALTER TABLE `follows` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ingredients`
--

DROP TABLE IF EXISTS `ingredients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingredients` (
  `ing_id` int NOT NULL AUTO_INCREMENT,
  `ing_name` varchar(45) NOT NULL,
  `price` double NOT NULL,
  `description` varchar(45) NOT NULL,
  PRIMARY KEY (`ing_id`),
  UNIQUE KEY `ing_id_UNIQUE` (`ing_id`),
  UNIQUE KEY `ing_name_UNIQUE` (`ing_name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredients`
--

LOCK TABLES `ingredients` WRITE;
/*!40000 ALTER TABLE `ingredients` DISABLE KEYS */;
INSERT INTO `ingredients` VALUES (1,'Salt',1,'Salt'),(2,'Rice',3,'Rice'),(3,'Water',2,'Water'),(4,'Oil',5.6,'Oil');
/*!40000 ALTER TABLE `ingredients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `misuse`
--

DROP TABLE IF EXISTS `misuse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `misuse` (
  `reporter_id` int NOT NULL,
  `misuse_id` int NOT NULL,
  `misuse_type` varchar(45) NOT NULL,
  `misuse_content` varchar(500) NOT NULL,
  `replier_admin_id` int DEFAULT NULL,
  `reply` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`reporter_id`,`misuse_id`),
  KEY `replier_id_idx` (`replier_admin_id`),
  CONSTRAINT `replier_id` FOREIGN KEY (`replier_admin_id`) REFERENCES `admin_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `reporter_id` FOREIGN KEY (`reporter_id`) REFERENCES `reg_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `misuse`
--

LOCK TABLES `misuse` WRITE;
/*!40000 ALTER TABLE `misuse` DISABLE KEYS */;
/*!40000 ALTER TABLE `misuse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rates`
--

DROP TABLE IF EXISTS `rates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rates` (
  `user_id` int NOT NULL,
  `rec_id` int NOT NULL,
  `rate_date` datetime DEFAULT NULL,
  `taste` varchar(45) DEFAULT NULL,
  `prep_ease` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`user_id`,`rec_id`),
  UNIQUE KEY `user_id_UNIQUE` (`user_id`),
  UNIQUE KEY `rec_id_UNIQUE` (`rec_id`),
  UNIQUE KEY `taste_UNIQUE` (`taste`),
  UNIQUE KEY `prep_ease_UNIQUE` (`prep_ease`),
  UNIQUE KEY `rate_date_UNIQUE` (`rate_date`),
  CONSTRAINT `rate_rec_id` FOREIGN KEY (`rec_id`) REFERENCES `recipes` (`rec_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `rate_user_id` FOREIGN KEY (`user_id`) REFERENCES `reg_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rates`
--

LOCK TABLES `rates` WRITE;
/*!40000 ALTER TABLE `rates` DISABLE KEYS */;
/*!40000 ALTER TABLE `rates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipes`
--

DROP TABLE IF EXISTS `recipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recipes` (
  `rec_id` int NOT NULL AUTO_INCREMENT,
  `rec_name` varchar(45) NOT NULL,
  `dietary_type` varchar(45) NOT NULL,
  `description` varchar(500) NOT NULL,
  `image` blob,
  `creation_date` datetime DEFAULT NULL,
  `creator_id` int NOT NULL,
  PRIMARY KEY (`rec_id`),
  UNIQUE KEY `rec_id_UNIQUE` (`rec_id`),
  KEY `user_id_idx` (`creator_id`),
  CONSTRAINT `user_id` FOREIGN KEY (`creator_id`) REFERENCES `reg_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes`
--

LOCK TABLES `recipes` WRITE;
/*!40000 ALTER TABLE `recipes` DISABLE KEYS */;
INSERT INTO `recipes` VALUES (3,'QA_Engineer_Tarik_Demirtas','None','asd',NULL,'2024-01-01 21:35:57',2),(4,'TakoLoka','None','TakoLoka as tako',NULL,'2024-01-02 00:19:46',1),(10,'Nefis Yemek','None','Tarif',NULL,'2024-01-02 00:31:30',1);
/*!40000 ALTER TABLE `recipes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipes_ingredients`
--

DROP TABLE IF EXISTS `recipes_ingredients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recipes_ingredients` (
  `ri_id` int NOT NULL AUTO_INCREMENT,
  `rec_id` int DEFAULT NULL,
  `ing_id` int DEFAULT NULL,
  PRIMARY KEY (`ri_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes_ingredients`
--

LOCK TABLES `recipes_ingredients` WRITE;
/*!40000 ALTER TABLE `recipes_ingredients` DISABLE KEYS */;
INSERT INTO `recipes_ingredients` VALUES (13,4,2),(14,4,3),(19,10,1),(20,10,3);
/*!40000 ALTER TABLE `recipes_ingredients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reg_user`
--

DROP TABLE IF EXISTS `reg_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reg_user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(16) NOT NULL,
  `email` varchar(255) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `avatar` blob,
  `password` varchar(32) NOT NULL,
  `user_type` varchar(45) NOT NULL,
  `bio` varchar(45) DEFAULT NULL,
  `followers` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_id_UNIQUE` (`user_id`),
  UNIQUE KEY `username_UNIQUE` (`username`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reg_user`
--

LOCK TABLES `reg_user` WRITE;
/*!40000 ALTER TABLE `reg_user` DISABLE KEYS */;
INSERT INTO `reg_user` VALUES (1,'TakoLoka','takoloka@mail.com','Tarık','Demirtaş',NULL,'TakoLoka','0',NULL,NULL),(2,'Koko','kokok@mail.com','Tako','Koko',NULL,'Koko','0','None',NULL);
/*!40000 ALTER TABLE `reg_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reply_bt`
--

DROP TABLE IF EXISTS `reply_bt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reply_bt` (
  `requester_id` int NOT NULL,
  `admin_id` int NOT NULL,
  `reply` varchar(45) NOT NULL,
  PRIMARY KEY (`requester_id`,`admin_id`),
  KEY `rep_admin_req_id_idx` (`admin_id`),
  CONSTRAINT `rep_admin_req_id` FOREIGN KEY (`admin_id`) REFERENCES `admin_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `rep_req_id` FOREIGN KEY (`requester_id`) REFERENCES `reg_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reply_bt`
--

LOCK TABLES `reply_bt` WRITE;
/*!40000 ALTER TABLE `reply_bt` DISABLE KEYS */;
/*!40000 ALTER TABLE `reply_bt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `request_bt`
--

DROP TABLE IF EXISTS `request_bt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `request_bt` (
  `requester_id` int NOT NULL,
  `admin_id` int NOT NULL,
  PRIMARY KEY (`requester_id`,`admin_id`),
  KEY `admin_req_id_idx` (`admin_id`),
  CONSTRAINT `admin_req_id` FOREIGN KEY (`admin_id`) REFERENCES `admin_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `req_id` FOREIGN KEY (`requester_id`) REFERENCES `reg_user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `request_bt`
--

LOCK TABLES `request_bt` WRITE;
/*!40000 ALTER TABLE `request_bt` DISABLE KEYS */;
/*!40000 ALTER TABLE `request_bt` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-02  1:27:26
