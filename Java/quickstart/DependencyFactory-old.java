package com.mycompany;

import software.amazon.awssdk.auth.credentials.AwsCredentialsProvider;
import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;

/**
 * The module containing all dependencies required by the {@link Handler}.
 */
public class DependencyFactory {

    private DependencyFactory() {}

    /**
     * @return an instance of S3Client with default credential provider chain
     */
    public static S3Client s3Client() {
        return S3Client.builder()
                       .httpClientBuilder(ApacheHttpClient.builder())
                       .credentialsProvider(DefaultCredentialsProvider.create())
                       .region(Region.US_EAST_1) // Change to your preferred region
                       .build();
    }
    
    /**
     * @param region The AWS region to use
     * @return an instance of S3Client with default credential provider chain and specified region
     */
    public static S3Client s3Client(Region region) {
        return S3Client.builder()
                       .httpClientBuilder(ApacheHttpClient.builder())
                       .credentialsProvider(DefaultCredentialsProvider.create())
                       .region(region)
                       .build();
    }
    
    /**
     * @param profileName The AWS profile name to use from credentials file
     * @return an instance of S3Client using credentials from the specified profile
     */
    public static S3Client s3ClientWithProfile(String profileName) {
        return S3Client.builder()
                       .httpClientBuilder(ApacheHttpClient.builder())
                       .credentialsProvider(ProfileCredentialsProvider.create(profileName))
                       .build();
    }
    
    /**
     * @param credentialsProvider Custom AWS credentials provider
     * @return an instance of S3Client using the provided credentials provider
     */
    public static S3Client s3ClientWithCredentials(AwsCredentialsProvider credentialsProvider) {
        return S3Client.builder()
                       .httpClientBuilder(ApacheHttpClient.builder())
                       .credentialsProvider(credentialsProvider)
                       .build();
    }
}