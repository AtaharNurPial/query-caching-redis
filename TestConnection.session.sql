
-- @block creating table
CREATE TABLE Faculty(
    id INT(10) AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50),
    email VARCHAR(50) NOT NULL UNIQUE
);

-- @BLOCK
INSERT INTO Students (Name, email, Major) 
VALUES(
    'Cersey',
    'cersey@got.com',
    'POL'
);

-- @BLOCK
INSERT INTO Students(Name, email, Major)
VALUES
    ('tacb','atvb@aph.com','AWS'),
    ('bcaa','bqgc@aph.com','AWS'),
    ('cdaf','cqdt@aplh.com','AWS'),
    ('dees','dwebzt@aplh.com','AWS'),
    ('efgc','nzef@taplh.com','AWS'),
    ('fgga','fgz@aqplh.com','AWS'),
    ('ghaa','ghr@stilaplh.com','AWS'),
    ('hiee','hir@tqsilaplh.com','AWS'),
    ('ijge','ijaq@silaplh.com','AWS'),
    ('jkkga','jrk@silaplh.com','AWS'),
    ('klgh','ktal@silaplh.com','AWS'),
    ('lmaa','lmrq@silaplh.com','PR'),
    ('mnzw','mna@atplh.com','PR'),
    ('nora','noa@qaplh.com','PR'),
    ('opag','optg@aplh.com','PR'),
    ('pqth','pqr@bqb.com','PR'),
    ('qraa','qrw@dtex.com','PR'),
    ('rsga','mra@rmr.com','PR'),
    ('stgw','tk@reqmr.com','PR'),
    ('tugr','tuzt@ian.com','PR'),
    ('uvaat','uve@qwl.com','CSE'),
    ('vwtg','cbar@fb.com','SPO'),
    ('wxqa','fgec@fb.com','SPO'),
    ('xyqz','tecf@fb.com','SPO'),
    ('yzat','tlu@fb.com','SPO');

-- @block
SELECT NAME, Major, id FROM Students
WHERE Major = 'ACE'
ORDER BY id DESC
LIMIT 10;

-- @block 
SELECT Major,count(*) FROM Students GROUP BY Major; 

-- @block 
SELECT * FROM Students;

-- @block
SELECT count(*) FROM Students