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
        substring(col("UPDATED_TRADE_DATE"), 3, 2).alias("TRADE_MONTH"), 
        substring(col("UPDATED_TRADE_DATE"), 1, 2).alias("TRADE_DAY"), 
        substring(col("UPDATED_TRADE_DATE"), 5, 4).alias("TRADE_YEAR"), 
        substring(col("UPDATED_SETTLEMENT_DATE"), 3, 2).alias("SETTLEMENT_MONTH"), 
        substring(col("UPDATED_SETTLEMENT_DATE"), 1, 2).alias("SETTLEMENT_DAY"), 
        substring(col("UPDATED_SETTLEMENT_DATE"), 5, 4).alias("SETTLEMENT_YEAR"), 
        substring(col("UPDATED_MATURITY_DATE"), 3, 2).alias("MATURITY_MONTH"), 
        substring(col("UPDATED_MATURITY_DATE"), 1, 2).alias("MATURITY_DAY"), 
        substring(col("UPDATED_MATURITY_DATE"), 5, 4).alias("MATURITY_YEAR")
    )
