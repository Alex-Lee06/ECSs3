•	We don’t have official document on reading out data in S3 bucket, specifically in Scala code.
•	However, there are several examples of accessing an S3 bucket in Scala on the web.  The only difference is, you would have to configure the client to connect to ECS instead of AWS.
•	Since Scala is based on Java, the AWS SDK for Java can be used, or another 3rd Scala wrapper.  We have samples that show how to connect to ECS using the AWS SDK for Java on github as well.
•	As for s3curl, it is used in the same manner as it would for AWS.  Below is customer viewable KB which explains in detail how this is used:
	How to perform basic s3 operations on ECS 3.x using the s3curl.pl script: https://support.emc.com/kb/497076 
Action Plan:
•	Customer to advise if further assistance is needed or if this SR can be closed.




http://bigdatatech.taleia.software/2015/12/07/bash-script-to-upload-files-to-a-amazon-s3-bucket-using-curl/

https://italy.emc.com/collateral/TechnicalDocument/docu59635.pdf





Camel Router with Scala DSL Project
===================================

To build this project use

    mvn install

To run this project

    mvn exec:java
    
For more help see the Apache Camel documentation

    http://camel.apache.org/



****=============For me to remember==========****
name := "rest"

version := "1.0"

scalaVersion := "2.10.2"

libraryDependencies ++= Seq(
    "io.spray" % "spray-can" % "1.1-M8",
    "io.spray" % "spray-http" % "1.1-M8",
    "io.spray" % "spray-routing" % "1.1-M8",
    "com.typesafe.akka" %% "akka-actor" % "2.1.4",
    "com.typesafe.akka" %% "akka-slf4j" % "2.1.4",
    "com.typesafe.slick" %% "slick" % "1.0.1",
    "mysql" % "mysql-connector-java" % "5.1.25",
    "net.liftweb" %% "lift-json" % "2.5.1",
    "ch.qos.logback" % "logback-classic" % "1.0.13"
)

resolvers ++= Seq(
    "Spray repository" at "http://repo.spray.io",
    "Typesafe repository" at "http://repo.typesafe.com/typesafe/releases/"
)



======================
public class Test {
    public static String uid = "root";
    public static String secret = "KHBkaH0Xd7YKF43ZPFbWMBT9OP0vIcFAMkD/9dwj";
    public static String viprDataNode = "http://ecs.yourco.com:9020";

    public static String bucketName = "myBucket";
    public static File objectFile = new File("/photos/cat1.jpg");

    public static void main(String[] args) throws Exception {

        AmazonS3Client client = new AmazonS3Client(new BasicAWSCredentials(uid, secret));

        S3ClientOptions options = new S3ClientOptions();
        options.setPathStyleAccess(true);

        AmazonS3Client client = new AmazonS3Client(credentials);
        client.setEndpoint(viprDataNode);
        client.setS3ClientOptions(options);

        client.createBucket(bucketName, "Standard");
        listObjects(client);

        client.putObject(bucketName, objectFile.getName(), objectFile);
        listObjects(client);

        client.copyObject(bucketName,objectFile.getName(),bucketName, "copy-" + objectFile.getName());
        listObjects(client);
    }

    public static void listObjects(AmazonS3Client client) {
        ObjectListing objects = client.listObjects(bucketName);
        for (S3ObjectSummary summary : objects.getObjectSummaries()) {
            System.out.println(summary.getKey()+ "   "+summary.getOwner());
        }
    }
}
==============
https://mvnrepository.com/artifact/com.emc.ecs/spark-ecs-s3?fbclid=IwAR2l8tgXt-McagEPIxDpwZFHUMD9A-e1b5yvEokJG8yVEE2dfjsOXqz3KEs

==============






