DROP DATABASE IF EXISTS datasci_final_project;
CREATE DATABASE datasci_final_project;
DROP USER IF EXISTS datasci_project_user;
CREATE USER datasci_project_user WITH PASSWORD 'datasci_password';
GRANT ALL PRIVILEGES ON DATABASE datasci_final_project TO datasci_project_user;