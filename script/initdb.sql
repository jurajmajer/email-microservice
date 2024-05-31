-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: May 31, 2024 at 07:45 AM
-- Server version: 8.0.31
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `email-microservice`
--

-- --------------------------------------------------------

--
-- Table structure for table `email_attachment_queue`
--

DROP TABLE IF EXISTS `email_attachment_queue`;
CREATE TABLE IF NOT EXISTS `email_attachment_queue` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email_queue_id` int NOT NULL,
  `filename` varchar(1024) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `filepath` varchar(1024) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_email_attachment_queue_email_queue_id` (`email_queue_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `email_queue`
--

DROP TABLE IF EXISTS `email_queue`;
CREATE TABLE IF NOT EXISTS `email_queue` (
  `id` int NOT NULL AUTO_INCREMENT,
  `recipient_address` varchar(256) COLLATE utf8mb4_unicode_ci NOT NULL,
  `subject` varchar(256) COLLATE utf8mb4_unicode_ci NOT NULL,
  `template_id` varchar(256) COLLATE utf8mb4_unicode_ci NOT NULL,
  `template_params` json DEFAULT NULL,
  `lang` varchar(5) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `processed_at` datetime DEFAULT NULL,
  `processing_result` int DEFAULT NULL,
  `processing_error` text COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `email_attachment_queue`
--
ALTER TABLE `email_attachment_queue`
  ADD CONSTRAINT `email_attachment_queue_ibfk_1` FOREIGN KEY (`email_queue_id`) REFERENCES `email_queue` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
