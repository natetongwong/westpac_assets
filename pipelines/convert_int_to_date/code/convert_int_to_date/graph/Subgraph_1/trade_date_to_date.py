from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from convert_int_to_date.udfs.UDFs import *

def trade_date_to_date(spark: SparkSession, reformat_trade_date: DataFrame) -> DataFrame:
    return reformat_trade_date.select(
        col("deal_id"), 
        make_date(col("TRADE_YEAR"), col("TRADE_MONTH"), col("TRADE_DAY")).alias("TRADE_DATE"), 
        make_date(col("SETTLEMENT_YEAR"), col("SETTLEMENT_MONTH"), col("SETTLEMENT_DAY")).alias("SETTLEMENT_DATE"), 
        make_date(col("MATURITY_YEAR"), col("MATURITY_MONTH"), col("MATURITY_DAY")).alias("MATURITY_DATE")
    )
