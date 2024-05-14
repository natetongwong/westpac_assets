from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from convert_int_to_date.udfs.UDFs import *

def formatted_trade_date(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("deal_id"), 
        when((length(col("STRING_TRADE_DATE")) == lit(7)), concat(lit("0"), col("STRING_TRADE_DATE")))\
          .otherwise(col("STRING_TRADE_DATE"))\
          .alias("ADD_LEADING_ZERO")
    )
