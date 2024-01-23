/* 3. Cuál es la transacción con respuesta exitosa en los que cada cliente realiza al 
 menos el 70% del monto total transferido. */
WITH TotalPorCliente as (
    SELECT
        documento,
        sum(vlrtran) as suma_vlrtran
    FROM
        ITC
    WHERE
        cdgrpta = 0
    group by
        documento
)
SELECT
    t1.documento,
    t1.cdgrpta,
    t1.vlrtran,
    t2.suma_vlrtran
FROM
    ITC t1
    INNER JOIN TotalPorCliente t2 ON t1.documento = t2.documento
WHERE
    t1.vlrtran >= t2.suma_vlrtran * 0.7
    AND t1.cdgrpta = 0;