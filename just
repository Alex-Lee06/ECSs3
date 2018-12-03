import java.io._

import org.apache.commons.io.FileUtils
import org.apache.spark.{SparkConf, SparkContext}

object escunion{
  def main(args: Array[String]): Unit = {

    //check to delete the existing files or folder
    FileUtils.deleteQuietly(new File("s3a://ebia-vol-test/SparkECSCoalesce"))
    //Instantiate Spark Session
    val conf = new SparkConf().setAppName("SparkECS")
    val sc: SparkContext = new SparkContext(conf)
    //val sc = SparkSession.builder().master("local").appName("SparkTestECSS3").getOrCreate()

    val accessKeyId = "ebia-vol-test-user"
    val secretAccessKey = "qsUJepZHhevNxhyqfXeM97vJ188hkdvajjmga5/b"
      sc.hadoopConfiguration.set("fs.s3a.awsAccessKeyId", accessKeyId)
      sc.hadoopConfiguration.set("fs.s3a.awsSecretAccessKey",secretAccessKey)


    val gd_path = sc.textFile("s3a://ebia-vol-test/gd_lyrics.txt")
    val jack_path = sc.textFile("s3a://ebia-vol-test/jack_straw.txt")

    val rddunion = gd_path.union(jack_path)

    //if need to be one file output
      rddunion.coalesce(1).saveAsTextFile("s3a://ebia-vol-test/SparkECSCoalesce")

    val verify = sc.textFile("s3a://ebia-vol-test/SparkECSCoalesce/part*")
      verify.count()
      verify.collect().map(line => println(line))

  }
}
