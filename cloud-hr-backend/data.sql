CREATE DATABASE cloud_hr;
USE cloud_hr;
CREATE TABLE employees (
  id INT AUTO_INCREMENT PRIMARY KEY,
  employee_code VARCHAR(20) UNIQUE,
  full_name VARCHAR(100),
  email VARCHAR(100) UNIQUE,
  password VARCHAR(255),
  role ENUM('admin','employee') DEFAULT 'employee',
  department VARCHAR(100),
  status ENUM('active','inactive') DEFAULT 'active',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
SHOW TABLES;
INSERT INTO employees
(employee_code, full_name, email, password, role, department)
VALUES
('ADMIN001', 'Cloud HR Admin', 'admin@cloudhr.com', 'admin123', 'admin', 'HR');
SELECT * FROM employees;
CREATE TABLE attendance (
  id INT AUTO_INCREMENT PRIMARY KEY,
  employee_id INT,
  attendance_date DATE,
  check_in TIME,
  check_out TIME,
  status ENUM('present','absent','leave') DEFAULT 'present',
  FOREIGN KEY (employee_id) REFERENCES employees(id)
);
CREATE TABLE leave_requests (
  id INT AUTO_INCREMENT PRIMARY KEY,
  employee_id INT,
  leave_type ENUM('sick','casual','paid','unpaid'),
  start_date DATE,
  end_date DATE,
  reason TEXT,
  status ENUM('pending','approved','rejected') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (employee_id) REFERENCES employees(id)
);
SHOW TABLES;

