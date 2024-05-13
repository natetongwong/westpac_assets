from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from exchangeratetable.config.ConfigStore import *
from exchangeratetable.udfs.UDFs import *

def create_exchange_rate_lookup(spark: SparkSession, in0: DataFrame):
    keyColumns = ['''Currency_1''']
    valueColumns = ['''Conversion_Rate''', '''Currency_2''', '''Conversion_Rule''']
    createLookup("exchange_rate_table", in0, spark, keyColumns, valueColumns)
