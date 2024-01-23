--1. Generar un listado de clientes de género masculino con transacciones en 2 o más dispositivos
WITH MasterItc AS (
    SELECT
        MT.genero_cli,
		MT.num_doc,
        ITC.disposit
    FROM
        MASTER MT
        LEFT JOIN ITC ON MT.num_doc = ITC.documento
    WHERE
        MT.genero_cli = 'M'
)
SELECT
    num_doc,
    genero_cli,
    COUNT(DISTINCT disposit) AS numero_dispositivos
FROM
    MasterItc
GROUP BY
    num_doc, genero_cli
HAVING
    COUNT(DISTINCT disposit) >= 2;
