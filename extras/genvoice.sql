-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 12, 2025 at 02:16 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `genvoice`
--

-- --------------------------------------------------------

--
-- Table structure for table `cases`
--

CREATE TABLE `cases` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cases`
--

INSERT INTO `cases` (`id`, `name`, `description`) VALUES
(1, 'Jonathan Lim', 'A 28-year-old software engineer who is experiencing intense anxiety during team meetings and is struggling to speak up, fearing judgment from colleagues.'),
(2, 'Angela Paolo', 'A 42-year-old teacher who is coping with the recent loss of a parent and is finding it difficult to concentrate on work and daily responsibilities.'),
(3, 'Xu Yaoming', 'A 16-year-old high school student who is feeling overwhelmed by academic pressure and is struggling to balance schoolwork, extracurriculars, and personal time.');

-- --------------------------------------------------------

--
-- Table structure for table `clinicians`
--

CREATE TABLE `clinicians` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `Username` varchar(100) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `Role` enum('Senior','Junior') NOT NULL DEFAULT 'Junior'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `clinicians`
--

INSERT INTO `clinicians` (`id`, `name`, `Username`, `Password`, `Role`) VALUES
(1, 'Dr. Joel Tan', 'joel87', '$2b$12$d5BDnmCXiIEBotSpdOgQbeU29R7iIe7DpXFeHPuA6pEE/5nqCtAZO', 'Senior'),
(2, 'Dr. Huang Shimin', 'shiminh', '$2b$12$9hQ5gy7GBC4oCJlfcqFYBueGlpkwAFBWRZo5f2fMliSqEREXqR.66', 'Junior'),
(3, 'Dr. Rishi Agarwal', 'rishiaw', '$2b$12$iEpuK6Fh6GrZq.JYL65kvezkGJEnmmxp8lxA5M8/f5T8Ix0iiIF6O', 'Junior'),
(4, 'Dr. Jane Doe', 'jane99', '$2b$12$el5uIuvlwqKA59NRwC3cte47Z0USkhjnRG6yVtWQEWcIc3fbtmcye', 'Junior'),
(5, 'Dr. Jane Doe', 'jane992', '$2b$12$mp9Xupmln2aGRL1fV14Dy.6t.IROB.vUGgD7AsXThQWahGIrqqLz6', 'Junior');

-- --------------------------------------------------------

--
-- Table structure for table `valid_tokens`
--

CREATE TABLE `valid_tokens` (
  `id` int(11) NOT NULL,
  `clinician_id` int(11) NOT NULL,
  `token` text NOT NULL,
  `created_on` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `valid_tokens`
--

INSERT INTO `valid_tokens` (`id`, `clinician_id`, `token`, `created_on`) VALUES
(3, 4, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGluaWNpYW5faWQiOjQsImV4cCI6MTc0MTgwMjg1MH0.OCPOz-5bJOPkqMqTHA9JElTwJoRbit6II9TR2CMOeNU', '2025-03-12 17:07:30');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cases`
--
ALTER TABLE `cases`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `clinicians`
--
ALTER TABLE `clinicians`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Username` (`Username`);

--
-- Indexes for table `valid_tokens`
--
ALTER TABLE `valid_tokens`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cases`
--
ALTER TABLE `cases`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `clinicians`
--
ALTER TABLE `clinicians`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `valid_tokens`
--
ALTER TABLE `valid_tokens`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
