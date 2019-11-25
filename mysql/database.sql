CREATE DATABASE test_data;
USE test_data;

-- Create user, grant access to database
CREATE USER 'test'@'localhost' IDENTIFIED BY 'password';
GRANT ALL on test_data.* to 'test'@'localhost';

CREATE TABLE departments (
       id bigint unsigned not null auto_increment,
       name varchar(255) not null,
       budget DECIMAL(20,2),
       constraint pk_example primary key (id)
);

CREATE TABLE employees (
       id bigint unsigned not null auto_increment,
       name varchar(255) not null,
       salary DECIMAL(20,2) not null,
       department_id bigint unsigned not null,
       constraint pk_example primary key (id),
       FOREIGN KEY (department_id)
        REFERENCES departments(id)
        ON DELETE CASCADE
);

INSERT INTO departments ( name, budget ) VALUES
('Executive', 1000000),
('Engineering', 1000000),
('Sales', 1000000),
('Legal', 1000000),
('Marketing', 1000000)
;

INSERT INTO employees ( name, salary, department_id ) VALUES
( 'Hilda Nguyen',  200000, 1),
( 'Rose Perez',  100000, 2),
( 'Byron Washington',  100000, 3),
( 'Dale Long',  100000, 4),
( 'Paul Gregory',  100000, 2),
( 'Kent Hansen',  100000, 3),
( 'Jean Pena',  100000, 5)
;
