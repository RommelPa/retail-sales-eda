# Resumen Ejecutivo — Inteligencia de Ventas Retail

## 1. Objetivo

Este proyecto analiza datos transaccionales de ventas online para identificar patrones de ingresos, comportamiento de clientes, desempeño de productos, impacto de cancelaciones y oportunidades comerciales.

El objetivo es entender el negocio antes de construir modelos predictivos, dashboards o sistemas de segmentación de clientes.

## 2. Alcance del dataset

Después de eliminar filas duplicadas exactas, el dataset limpio contiene:

| Dataset | Filas | Uso |
|---|---:|---|
| Datos limpios | 536,641 | Dataset completo enriquecido con variables y banderas de negocio |
| Ventas válidas | 524,878 | Dataset principal para ingresos, productos, países y tendencias |
| Ventas con cliente identificado | 392,692 | Subconjunto para análisis a nivel de cliente |

El revenue de ventas válidas alcanzó **10.64M**.

El revenue con cliente identificado alcanzó **8.89M**, lo que significa que **1.75M** de revenue válido no puede asociarse a un cliente conocido.

Esto representa **16.49%** del revenue válido.

## 3. Hallazgos principales

### 3.1 Los problemas de calidad de datos tienen significado comercial

El dataset original incluía filas duplicadas, clientes sin identificador, cancelaciones, cantidades no positivas y precios unitarios no positivos.

Estos registros no deben eliminarse de forma automática. Algunos representan eventos reales del negocio, especialmente cancelaciones y ajustes operativos.

### 3.2 El revenue está fuertemente concentrado en Reino Unido

Reino Unido representa aproximadamente **85%** del revenue válido.

Esto muestra una fuerte dependencia del mercado principal. También significa que el desempeño internacional debe analizarse por separado, porque los mercados más pequeños pueden quedar ocultos por el peso de Reino Unido.

### 3.3 Diciembre de 2011 es un mes parcial

El revenue creció con fuerza entre septiembre y noviembre de 2011.

Sin embargo, diciembre de 2011 no debe compararse directamente con los meses anteriores, porque el dataset solo contiene transacciones hasta el 9 de diciembre.

### 3.4 El revenue de clientes está concentrado

Los 10 clientes identificados con mayor revenue generan **17.30%** del revenue con cliente identificado.

Los 100 clientes identificados con mayor revenue generan **40.61%** del revenue con cliente identificado y aproximadamente **33.91%** del revenue válido total.

Esto sugiere que un grupo relativamente pequeño de clientes tiene un impacto importante en el desempeño comercial.

### 3.5 Las cancelaciones tienen impacto material

Las cancelaciones representan un impacto negativo aproximado de **894K**, equivalente al **8.40%** del revenue de ventas válidas.

Esto debe analizarse como un problema comercial y operativo, no descartarse como simple ruido.

### 3.6 El ranking de productos requiere interpretación de negocio

Algunos registros con alto revenue no son productos regulares. Algunos ejemplos son cargos de envío, ajustes manuales o códigos operativos.

Por esta razón, el desempeño de productos fue analizado con y sin códigos operativos especiales.

El ítem `PAPER CRAFT , LITTLE BIRDIE` muestra un revenue inusualmente alto con muy pocas facturas, por lo que debe tratarse como un posible outlier que requiere validación de negocio.

### 3.7 Los valores por orden están sesgados

El ticket promedio es **533.17**, mientras que el ticket mediano es **303.30**.

Esto indica que pocas órdenes grandes pueden distorsionar las interpretaciones basadas solo en promedios. Las métricas basadas en mediana y percentiles son más confiables para entender el comportamiento típico de las órdenes.

## 4. Recomendaciones de negocio

1. Monitorear por separado a los clientes de alto valor, porque representan una proporción importante del revenue con cliente identificado.
2. Analizar los mercados internacionales excluyendo Reino Unido para identificar oportunidades de crecimiento ocultas por el mercado dominante.
3. Investigar patrones de cancelación por producto, país y cliente para detectar fricciones operativas.
4. Separar códigos operativos del ranking de productos para no confundir cargos o ajustes con desempeño real de mercadería.
5. Usar métricas como mediana y percentiles para analizar ticket promedio, en lugar de depender solo de promedios.
6. Tratar los clientes sin identificador como una limitación de calidad de datos antes de realizar segmentación o análisis de retención.

## 5. Limitaciones

- El dataset cubre transacciones desde diciembre de 2010 hasta diciembre de 2011.
- Diciembre de 2011 está incompleto y no debe compararse directamente con meses completos.
- Aproximadamente 16.49% del revenue válido no tiene identificador de cliente asociado.
- El dataset no incluye costo de producto, margen de ganancia, inversión en marketing, inventario ni datos demográficos de clientes.
- Algunos registros con alto revenue pueden representar ajustes operativos y no ventas regulares de productos.

## 6. Próximos pasos

- Crear un proyecto de segmentación de clientes usando el subconjunto con cliente identificado.
- Construir un dashboard de ventas para reporting ejecutivo.
- Analizar con mayor detalle las causas de cancelaciones.
- Aplicar técnicas de forecasting a ingresos mensuales o volumen de ventas.