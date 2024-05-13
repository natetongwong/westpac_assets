from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from portfoliotogltable.config.ConfigStore import *
from portfoliotogltable.udfs.UDFs import *

def L0_Portfolio_to_GL(spark: SparkSession) -> DataFrame:
    return spark.read.table("`westpac`.`raw`.`portfolio_to_gl`")
