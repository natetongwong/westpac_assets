from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from exchangeratetable.config.ConfigStore import *
from exchangeratetable.udfs.UDFs import *

def L0_raw_exchange_rate_table(spark: SparkSession) -> DataFrame:
    return spark.read.table("`westpac`.`raw`.`exchange_rate_table`")
