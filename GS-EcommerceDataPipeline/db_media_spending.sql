
CREATE DATABASE media_spending_raw;

USE media_spending_raw;

CREATE TABLE record(
    id int(255) NOT NULL AUTO_INCREMENT,
    table_name varchar(255) NOT NULL,
    label varchar(50) NOT NULL,
    date_time varchar(50)  NOT NULL,
    PRIMARY KEY (id) 
);



