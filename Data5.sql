use Department1;
CREATE TABLE company (
    company_id INT,
    company_name VARCHAR(50),
    company_city VARCHAR(50)
);

INSERT INTO company VALUES 
(18, 'Order All', 'Boston'),
(15, 'Jack Hill Ltd', 'London'),
(16, 'Akas Foods', 'Delhi'),
(17, 'Foodies.', 'London'),
(19, 'sip-n-Bite.', 'New York');

SELECT * FROM company;
