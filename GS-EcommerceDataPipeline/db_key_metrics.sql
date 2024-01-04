-- DROP DATABASE key_metrics_raw ;

CREATE DATABASE key_metrics_raw;

USE key_metrics_raw;

CREATE TABLE record(
    id int(255) NOT NULL AUTO_INCREMENT,
    table_name varchar(255) NOT NULL,
    label varchar(50) NOT NULL,
    date_time varchar(50)  NOT NULL,
    PRIMARY KEY (id) 
);

