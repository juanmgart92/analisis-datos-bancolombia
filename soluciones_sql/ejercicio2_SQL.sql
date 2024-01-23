/* 2. Defina el canal con mayor sumatoria de valor de transacciones de cada cliente, 
 la respuesta debe incluir un único canal por cliente con el monto total. */
with totalCanalesCliente as(
    select
        documento,
        canal,
        sum(vlrtran) as suma_vlrtran
    from
        itc
    group by
        documento,
        canal
),
ordenCostos as (
    select
        documento,
        canal,
        suma_vlrtran,
        ROW_NUMBER() over (
            partition by documento
            order by
                suma_vlrtran desc
        ) orden
    from
        totalCanalesCliente
)
select
    documento,
    canal,
    suma_vlrtran
from
    ordenCostos
where
    orden = 1;

