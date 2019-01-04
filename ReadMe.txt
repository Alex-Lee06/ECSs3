https://github.com/djannot/ecs-p3/blob/master/spark/spark.md

val gd_path = sc.textFile("s3a://ebia-vol-test/gd_lyrics.txt")
val row_gd = gd_path.map(line => Row.fromSeq(line.split(",", -1)))
var df_gd = sqlContext.createDataFrame(row_gd, schema)

val jack_path = sc.textFile("s3a://ebia-vol-test/jack_straw.txt")
val row_jack = jack_path.map(line => Row.fromSeq(line.split(",", -1)))
var df_jack = sqlContext.createDataFrame(row_jack, schema)

val df3 = df_gd.join(df_jack)

val df1 = sqlContext.createDataFrame(rowRdd1, new StructType(schema.tail.toArray))


https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/examples-s3-objects.html
https://bitbucket.org/atlassian/aws-scala
https://github.com/EMCECS/ecs-samples/tree/master/aws-java-workshop/src/main/java/com/emc/ecs/s3/sample
https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-install.html

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





help for loading spark shell jars
https://stackoverflow.com/questions/45756554/how-to-use-s3-with-apache-spark-2-2-in-the-spark-shell

spark s3 tutorial
http://www.sparktutorials.net/Reading+and+Writing+S3+Data+with+Apache+Spark
