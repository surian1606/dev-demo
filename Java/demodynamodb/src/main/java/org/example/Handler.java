package org.example;
 
 import org.slf4j.Logger;
 import org.slf4j.LoggerFactory;

 import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
 import software.amazon.awssdk.services.dynamodb.model.ListTablesResponse;
 
 
 public class Handler {
     private final DynamoDbClient dynamoDbClient;
 
     public Handler() {
         dynamoDbClient = DependencyFactory.dynamoDbClient();
     }
 
     public void sendRequest() {
         Logger logger = LoggerFactory.getLogger(Handler.class);
 
         logger.info("calling the DynamoDB API to get a list of existing tables");
         ListTablesResponse response = dynamoDbClient.listTables();
 
         if (!response.hasTableNames()) {
             logger.info("No existing tables found for the configured account & region");
         } else {
             response.tableNames().forEach(tableName -> logger.info("Table: " + tableName));
         }
     }
 }