from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from convert_int_to_date.udfs.UDFs import *

def split_trade_date(spark: SparkSession, reformatted_trade_date: DataFrame) -> DataFrame:
    return reformatted_trade_date.select(
        col("deal_id"), 
        substring(col("ADD_LEADING_ZERO"), 3, 2).alias("TRADE_MONTH"), 
        substring(col("ADD_LEADING_ZERO"), 1, 2).alias("TRADE_DAY"), 
        substring(col("ADD_LEADING_ZERO"), 5, 4).alias("TRADE_YEAR")
    )
