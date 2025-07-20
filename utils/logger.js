const { createLogger, format, transports } = require('winston');

const path = require('path');
const { log } = require('console');


// Configure the logger

const logFormat = format.combine(
    format.errors({ stack: true }),
    format.timestamp({ format: 'YYYY-MM-DD HH:mm:ss' }),
    
    format.printf(( timestamp, level, message, stack) =>{
        return `${timestamp}[${level}]: ${stack || message}`;
    })
);


const logger = createLogger({
    level: 'info',
    format: logFormat,
    transports: [
        new transports.Console({
      format: format.combine(format.colorize(), logFormat),
    }),
        new transports.File({ filename: path.join(__dirname, '../logs/app.log'), level: 'info' }),
        new transports.File({ filename: path.join(__dirname, '../logs/error.log'), level: 'error' }),
    ],
    exitOnError: false,
});

module.exports = logger;