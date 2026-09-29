"""Listado 5.6. PySpark en local: la misma idea, repartida en varios núcleos.

Necesita Java instalado (JDK 17 o 21). Comprueba con: java -version
"""

import time

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# local[*] = usar todos los núcleos de este ordenador como si fueran un clúster
spark = (
    SparkSession.builder
    .appName("ventas-ud5")
    .master("local[*]")
    .config("spark.sql.shuffle.partitions", "8")
    .getOrCreate()
)
spark.sparkContext.setLogLevel("ERROR")

ventas = spark.read.parquet("datos/ventas_grandes.parquet")
print(f"{ventas.count():,} filas, {len(ventas.columns)} columnas")
ventas.printSchema()

inicio = time.perf_counter()
resumen = (
    ventas
    .withColumn("importe", F.col("unidades") * F.col("precio"))
    .groupBy("ciudad")
    .agg(F.count("*").alias("ventas"),
         F.round(F.sum("importe"), 2).alias("importe"))
    .orderBy(F.desc("importe"))
)
resumen.show()                       # nada se calcula hasta esta acción
print(f"Tiempo: {time.perf_counter() - inicio:.2f} s")

# La misma consulta, en SQL sobre una vista temporal
ventas.createOrReplaceTempView("venta")
spark.sql("""
    SELECT producto, ROUND(SUM(unidades * precio) / 1e6, 2) AS millones
    FROM venta GROUP BY producto ORDER BY millones DESC
""").show()

spark.stop()
