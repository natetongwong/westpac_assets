from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from portfoliotogltable.config.ConfigStore import *
from portfoliotogltable.udfs.UDFs import *

def create_portfolio_to_gl_lookup(spark: SparkSession, L1_Portfolio_to_GL: DataFrame):
    keyColumns = ['''portfolio_name''']
    valueColumns = ['''location''', '''GL_Level_1''', '''GL_Level_2''', '''GL_Level_3''']
    createLookup("portfolio_to_GL", L1_Portfolio_to_GL, spark, keyColumns, valueColumns)
