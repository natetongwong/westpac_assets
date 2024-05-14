from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from convert_int_to_date.udfs.UDFs import *

def trade_date_projection(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(col("deal_id"), col("TRADE_DATE").cast(StringType()).alias("STRING_TRADE_DATE"))
