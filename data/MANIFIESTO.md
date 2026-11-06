# Manifiesto de datos

| Campo | Valor |
|---|---|
| Archivo en `data/raw/` | `sentrybox_enaho2025.csv` |
| Fuente | INEI, Encuesta Nacional de Hogares (ENAHO) 2025, módulo 500, «Empleo e Ingresos», según el cuaderno del grupo. |
| Portal de origen | [Microdatos del INEI](https://proyectos.inei.gob.pe/microdatos/). La URL directa y la ficha de la descarga original quedan por verificar. |
| Archivo original indicado en el cuaderno | `Enaho01a-2025-500.csv`. El archivo de este repositorio es un **subconjunto derivado**, no el original del INEI. |
| Fecha de descarga original | Pendiente de confirmar con el grupo. |
| Licencia o condiciones de uso | Pendiente de verificar en la fuente oficial. |
| ¿Se permite redistribuir el subconjunto? | Pendiente de confirmar. Antes de publicar el CSV, verificar las condiciones aplicables. |
| Filas × columnas del CSV recibido | 4 765 × 18 |
| MD5 del CSV recibido (raw) | `79cb9c9fcccd760795c3a28fdc8b35e3` |
| MD5 del archivo processed | `f2a07a276a13ca7f0272aa8d8004b2df` (generado en Windows con Python 3.11.18 y pandas 2.2.3). |

## Diccionario de las variables usadas

Descripción basada en el cuaderno del proyecto; P indica el campo ENAHO de origen.

| Variable | Tipo | Descripción / unidad o categorías |
|---|---|---|
| `ganancia_neta_mes` | Objetivo | Ganancia neta de la ocupación principal el mes anterior, en soles (P530A). |
| `edad` | Numérica | Edad en años (P208A). |
| `horas_semana` | Numérica | Horas trabajadas la semana anterior en la ocupación principal (P513T). |
| `anios_en_ocupacion` | Numérica | Tiempo en la ocupación principal, en años (P513A1 + P513A2/12). |
| `personas_en_negocio` | Numérica | Personas que laboran en el negocio, incluido el encuestado (P512B). |
| `sexo_mujer` | Categórica binaria | 1 si la persona es mujer (P207). |
| `estado_civil` | Categórica | 1 conviviente, 2 casado, 3 viudo, 4 divorciado, 5 separado, 6 soltero (P209). |
| `nivel_educativo` | Categórica | Último nivel aprobado, códigos de ENAHO (P301A). |
| `es_empleador` | Categórica binaria | 1 empleador; 0 independiente (P507). |
| `ayuda_familiar_no_remunerado` | Categórica binaria | Indica ayuda de familiares sin pago fijo (P508). |
| `registro_sunat` | Categórica | 1 persona jurídica, 2 persona natural con RUC, 3 sin RUC (P510A1). |
| `lleva_libros_contables` | Categórica binaria | Indica si lleva libros o sistema de contabilidad (P510B). |
| `tiene_ocupacion_secundaria` | Categórica binaria | Indica si tuvo otro trabajo la semana pasada (P514). |
| `subsector_ciiu` | Categórica | Actividad de comercio minorista según CIIU Rev. 4 (P506R4). |
| `dominio` | Categórica | Dominio geográfico INEI (DOMINIO). |
| `estrato` | Categórica | Estrato geográfico INEI (ESTRATO). |
| `mes_encuesta` | Categórica | Mes de la encuesta (MES). |

`tiene_trabajadores_pagados` está presente en el CSV, pero no se usa como predictor: el cuaderno del grupo indica que coincide con `es_empleador` en esta muestra.

## Origen del subconjunto y preparación

El cuaderno del grupo describe el subconjunto como personas ocupadas, empleadoras o independientes, en comercio minorista (CIIU 4700–4799), con ganancia neta positiva e informada. También contiene código opcional para reconstruir las variables desde el módulo 500; esa reconstrucción no se ejecuta en este repositorio y debe contrastarse con el archivo original y la documentación de la fuente.

El pipeline de este repositorio parte del CSV recibido, lo conserva intacto y genera `data/processed/dataset.csv`. La plantilla quita espacios en nombres de columnas, elimina duplicados y filas sin objetivo. No se reemplazan códigos globales: el CSV ya contiene celdas vacías para los faltantes y un mismo código numérico podría tener significado válido en otra columna. La imputación de predictores, el escalamiento y la codificación se ajustan dentro de cada fold de entrenamiento del pipeline.
