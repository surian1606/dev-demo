package com.myapp;

import software.amazon.awssdk.services.dynamodb-enhanced.$serviceClientPrefixClient;


public class Handler {
    private final $serviceClientPrefixClient ${serviceClientVariable}Client;

    public Handler() {
        ${serviceClientVariable}Client = DependencyFactory.${serviceClientVariable}Client();
    }

    public void sendRequest() {
        // TODO: invoking the api calls using ${serviceClientVariable}Client.
    }
}
