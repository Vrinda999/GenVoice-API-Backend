-- Create Database
CREATE Database GenVoice -- Clinician
-- Table Creation
CREATE TABLE clinicians (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    Username VARCHAR(100) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL,
    Role ENUM('Senior', 'Junior') NOT NULL DEFAULT 'Junior'
);
-- Storing Initial Data
INSERT INTO clinicians
VALUES(
        001,
        "Dr. Joel Tan",
        "joel87",
        "b'$2b$12$3CoiOPfrodj4uJDnZPO13egQTIoeDCCD3qFSU52AZUCPvGGyWijM.'",
        "Senior"
    ),
    (
        002,
        "Dr. Huang Shimin",
        "shiminh",
        "b'$2b$12$/wgBKDmwPT2gCDHBJLJvHODYC3bwJgbhg9Gq4DPSDbAblw6msk3gm'",
        "Junior"
    ),
    (
        003,
        "Dr. Rishi Agarwal",
        "rishiaw",
        "b'$2b$12$ec4R9zw4fC7TpzUHX5XnDevZwhKT1kg.36.o53YZR3LSxDGXbQS0S'",
        "Junior"
    );