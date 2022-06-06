process.env.AWS_SDK_LOAD_CONFIG = true;

var AWS = require("aws-sdk");

console.log("Region: ", AWS.config.region);