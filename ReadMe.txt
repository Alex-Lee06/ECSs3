https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-s3-objects.html
https://bitbucket.org/atlassian/aws-scala
https://github.com/EMCECS/ecs-samples/tree/master/aws-java-workshop/src/main/java/com/emc/ecs/s3/sample

Dear team,
We are not able to access Dell ECS s3 from our Scala application. We tried multiple sulotions which I have shared with you eaalier but it wasn't successful. On Friday Nov 16 2018, Marlon Zhong from EMC team reached out to me and stated he will provide me a Scala version of s3curl script.  He also told me that he will esculate this ticket so the on shore team will call me on Monday Nov 19 2018, but we didn't get any response.  I waited for your call and also tried to call you for the last two days but didn't get connected.  Yesterday the support team told me that an EMC expert will connect with me within the next 3 hours, but didn't get any call. Please help me out to resovled this issue. 

The suggestions list provided by EMC to me doesn't make any sense for my task. Please ask any exeprts to call me and help me out. 

My comments are in line for the EMC suggestions list.  


•	We don’t have official document on reading out data in S3 bucket, specifically in Scala code.
		As mostly to people are using Scala nowadays. Therefore, there should be a proper documents for this. 

•	However, there are several examples of accessing an S3 bucket in Scala on the web.  The only difference is, you would have to configure the client to connect to ECS instead of AWS.
		Please share these links and mention what configuration I need to change. Or better, if you can quickly create a document and share it with me? 
		
		
•	Since Scala is based on Java, the AWS SDK for Java can be used, or another 3rd Scala wrapper.  We have samples that show how to connect to ECS using the AWS SDK for Java on github as well.
		We are bounded to using Scala for this use case. We are not suppose to use any other language for this use case.  Please provide us with a  sulotion with Scala. 
		

•	As for s3curl, it is used in the same manner as it would for AWS.  Below is customer viewable KB which explains in detail how this is used:
	How to perform basic s3 operations on ECS 3.x using the s3curl.pl script: https://support.emc.com/kb/497076 
		We try to use Perl verison of s3curl and it was succuessful, but the limitation is we need to use only Scala.  Lastly, I was talking to Marlon Zhong and he comment that you guys will provide us Scala version of the s3curl script this week. So please check the status on this. 



Note: This is very high poirity task. We spent three weeks on this task and from the last two week we are waiting for your support but didn't get such response from your side. Please understand and try to close this as soon as possible. 


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






