from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from convert_int_to_date.config.ConfigStore import *
from convert_int_to_date.udfs.UDFs import *

def date_dataframe_creation(spark: SparkSession) -> DataFrame:
    schema = StructType([
            StructField("DEAL_ID", IntegerType(), True),
            StructField("TRADE_DATE", IntegerType(), True),
            StructField("SETTLEMENT_DATE", IntegerType(), True),
            StructField("MATURITY_DATE", StringType(), True)

    ])
    # Create DataFrame with deal_id and DATE columns
    data = [(1, 31012020, 31012020, '31012020'), (2, 4022021, 4022021, '4022021'), (3, 31032022, 24032022, '0322')]
    out0 = spark.createDataFrame(data, schema)

    return out0
