from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from convert_int_to_date.config.ConfigStore import *
from convert_int_to_date.udfs.UDFs import *

def date_dataframe_creation(spark: SparkSession) -> DataFrame:
    schema = StructType([
StructField("deal_id", IntegerType(), True), StructField("TRADE_DATE", IntegerType(), True)])
    # Create DataFrame with deal_id and TRADE_DATE columns
    data = [(1, 31012020), (2, 4022021), (3, 24032022)]
    out0 = spark.createDataFrame(data, schema)

    return out0
