from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from convert_int_to_date.udfs.UDFs import *
from . import *
from .config import *

def Subgraph_1(spark: SparkSession, subgraph_config: SubgraphConfig, in0: DataFrame) -> DataFrame:
    Config.update(subgraph_config)
    df_trade_date_projection = trade_date_projection(spark, in0)
    df_formatted_trade_date = formatted_trade_date(spark, df_trade_date_projection)
    df_split_trade_date = split_trade_date(spark, df_formatted_trade_date)
    df_trade_date_to_date = trade_date_to_date(spark, df_split_trade_date)
    subgraph_config.update(Config)

    return df_trade_date_to_date
