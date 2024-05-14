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
          .alias("UPDATED_TRADE_DATE"), 
        when((length(col("STRING_SETTLEMENT_DATE")) == lit(7)), concat(lit("0"), col("STRING_SETTLEMENT_DATE")))\
          .otherwise(col("STRING_SETTLEMENT_DATE"))\
          .alias("UPDATED_SETTLEMENT_DATE"), 
        when((length(col("STRING_MATURITY_DATE")) == lit(7)), concat(lit("0"), col("STRING_MATURITY_DATE")))\
          .when(
            (length(col("STRING_MATURITY_DATE")) == lit(4)), 
            concat(
              lit("01"), 
              substring(col("STRING_MATURITY_DATE"), 1, 2), 
              lit("20"), 
              substring(col("STRING_MATURITY_DATE"), 3, 2)
            )
          )\
          .otherwise(col("STRING_MATURITY_DATE"))\
          .alias("UPDATED_MATURITY_DATE")
    )
