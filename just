import org.apache.spark.sql.Row
import org.apache.spark.sql.types._

val accessKeyId = "ebia-vol-test-user"
val secretAccessKey = "qsUJepZHhevNxhyqfXeM97vJ188hkdvajjmga5/b"
sc.hadoopConfiguration.set("fs.s3a.awsAccessKeyId", accessKeyId)
sc.hadoopConfiguration.set("fs.s3a.awsSecretAccessKey",secretAccessKey)


val gd_path = sc.textFile("s3a://ebia-vol-test/gd_lyrics.txt")
val jack_path = sc.textFile("s3a://ebia-vol-test/jack_straw.txt")

val rddunion = gd_path.union(jack_path)
//=== Options ===

//if need to be one file output
rddunion.coalesce(1).saveAsTextFile("s3a://ebia-vol-test/SparkECSCoalesce.txt")

val verify = sc.textFile("s3a://ebia-vol-test/SparkECSCoalesce.txt/part*")
verify.count()
verify.collect().map(line => println(line))
