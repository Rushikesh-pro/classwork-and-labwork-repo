CREATE TABLE employee (
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    Role VARCHAR(50) NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    city VARCHAR(50) NOT NULL
);
INSERT INTO employee (first_name, last_name, age, Role, salary, city) VALUES ('John', 'Doe', 30, 'Developer', 60000.00, 'New York');
INSERT INTO employee (first_name, last_name, age, Role, salary, city) VALUES ('Jane', 'Smith', 25, 'Designer', 50000.00, 'San Francisco');
INSERT INTO employee (first_name, last_name, age, Role, salary, city) VALUES ('Alice', 'Johnson', 28, 'Manager', 75000.00, 'Chicago');
INSERT INTO employee (first_name, last_name, age, Role, salary, city) VALUES ('Bob', 'Brown', 35, 'Analyst', 65000.00, 'Miami');
INSERT INTO employee (first_name, last_name, age, Role, salary, city) VALUES ('Charlie', 'Davis', 40, 'Director', 80000.00, 'Boston');

SELECT * FROM employee;
