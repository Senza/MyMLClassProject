import os
import webbrowser
from pathlib import Path
import findspark

def start_spark(app_name: str):
    current_file_path = Path(os.getcwd())
    project_root = current_file_path.parent.resolve()

    spark_home = project_root / "content" / "spark-3.5.1-bin-hadoop3"
    java_home = project_root / "content" / "java" / "jdk-17"
    hadoop_home = project_root / "content" / "hadoop"

    print("Library location check:")
    print(f"Spark home: {spark_home}")
    print(f"Java home: {java_home}")
    print(f"hadoop home: {hadoop_home}")

    os.environ["JAVA_HOME"] = str(java_home)
    os.environ["SPARK_HOME"] = str(spark_home)
    os.environ["HADOOP_HOME"] = str(hadoop_home)

    os.environ["PATH"] = (
            str(java_home / "bin") + os.pathsep +
            str(spark_home / "bin") + os.pathsep +
            str(hadoop_home / "bin") + os.pathsep +
            os.environ.get("PATH", "")
    )

    findspark.init()
    from pyspark.sql import SparkSession

    spark = SparkSession.builder \
        .appName("NYC_Yellow_Cab_Outlier_Detection") \
        .config("spark.executor.memory", "8g") \
        .config("spark.driver.memory", "8g") \
        .config("spark.sql.adaptive.enabled", "true") \
        .getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    spark.sparkContext.setLogLevel("ERROR")
    ui_url = spark.sparkContext.uiWebUrl

    print(f"Spark Session '{app_name}' is active!")
    print(f"Spark UI available at: {ui_url}")

    try:
        webbrowser.open(ui_url)
    except Exception():
        print("Could not auto-open browser, please click the link above.")

    return spark