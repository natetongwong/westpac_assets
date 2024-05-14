from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from convert_int_to_date.config.ConfigStore import *
from convert_int_to_date.udfs.UDFs import *

def date_dataframe_creation(spark: SparkSession) -> DataFrame:
    out0 = spark.createDataFrame([('31012020', ), ('02032021', ), ('3042022', )], ["TRADE_DATE"])

    return out0
