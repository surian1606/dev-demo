
package com.myapp;

import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.services.dynamodb-enhanced.$serviceClientPrefixClient;

/**
 * The module containing all dependencies required by the {@link Handler}.
 */
public class DependencyFactory {

    private DependencyFactory() {}

    /**
     * @return an instance of $serviceClientPrefixClient
     */
    public static $serviceClientPrefixClient ${serviceClientVariable}Client() {
        return $serviceClientPrefixClient.builder()
                       .httpClientBuilder(ApacheHttpClient.builder())
                       .build();
    }
}
