/*
 *  Description: Database Structure to be stored locally onto Raspberry Pi locally to avoid connecting to external server
*/

CREATE Table Sensor(
    data_id INTEGER NOT NULL AUTO_INCREMENT,
    humidity DECIMAL(3,1),
    temperature DECIMAL(3,1),    
    moisture DECIMAL(3,1),       
    light_intensity DECIMAL(3,1),      
    rssi INTEGER,       
    time_stamp TIMESTAMP,
    PRIMARY KEY(data_id));