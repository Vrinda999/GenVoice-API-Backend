-- Create Database
CREATE Database GenVoice;
--------------------------------------------------------------------------------------------------
-- Clinician
-- Table Creation
CREATE TABLE clinicians (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    Username VARCHAR(100) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL,
    Role ENUM('Senior', 'Junior') NOT NULL DEFAULT 'Junior'
);
-------------------------------------------------
-- Storing Initial Data
INSERT INTO clinicians
VALUES(
        001,
        "Dr. Joel Tan",
        "joel87",
        "$2b$12$d5BDnmCXiIEBotSpdOgQbeU29R7iIe7DpXFeHPuA6pEE/5nqCtAZO",
        "Senior"
    ),
    (
        002,
        "Dr. Huang Shimin",
        "shiminh",
        "$2b$12$9hQ5gy7GBC4oCJlfcqFYBueGlpkwAFBWRZo5f2fMliSqEREXqR.66",
        "Junior"
    ),
    (
        003,
        "Dr. Rishi Agarwal",
        "rishiaw",
        "$2b$12$iEpuK6Fh6GrZq.JYL65kvezkGJEnmmxp8lxA5M8/f5T8Ix0iiIF6O",
        "Junior"
    );
--------------------------------------------------------------------------------------------------
-- Cases
-- Table Creation
CREATE TABLE cases (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(1000) NOT NULL
);
-------------------------------------------------
-- Storing Initial Data
INSERT INTO cases
VALUES(
        001,
        "Jonathan Lim",
        "A 28-year-old software engineer who is experiencing intense anxiety during team meetings and is struggling to speak up, fearing judgment from colleagues."
    ),
    (
        002,
        "Angela Paolo",
        "A 42-year-old teacher who is coping with the recent loss of a parent and is finding it difficult to concentrate on work and daily responsibilities."
    ),
    (
        003,
        "Xu Yaoming",
        "A 16-year-old high school student who is feeling overwhelmed by academic pressure and is struggling to balance schoolwork, extracurriculars, and personal time."
    );
--------------------------------------------------------------------------------------------------