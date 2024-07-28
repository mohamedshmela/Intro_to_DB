CREATE DATABASE IF NOT EXISTS alx_book_store
USE alx_book_store;
CREATE TABLE Books (
book_id INT PRIMARY KEY,
title VARCHAR(130),
author_id VARCHAR(130),
price DOUBLE,
publication_date DATE
);