import pandas as pd

def obtener_clientes_masculinos_con_dispositivos(master_df, itc_df, dispositivos=2):
    """
    Obtiene un listado de clientes masculinos con transacciones en al menos la 
    cantidad de dispositivos especificada.
    """
    clientes_masculinos = master_df[master_df['genero_cli'] == 'M']

    master_itc = pd.merge(clientes_masculinos, itc_df, left_on='num_doc', right_on='documento', how='left')

    resultado = master_itc.groupby(['num_doc', 'genero_cli']).disposit.nunique().reset_index()

    resultado = resultado[resultado['disposit'] >= dispositivos]

    resultado.to_csv('./outputs/sol_ej_1.csv', index=False)

    return resultado

def obtener_canal_con_mayor_suma(itc_df):
    """
    Obtiene el canal con la mayor sumatoria de valor de transacciones de cada cliente.
    """
    total_canales_cliente = itc_df.groupby(['documento', 'canal'])['vlrtran'].sum().reset_index()

    orden_costos = total_canales_cliente.sort_values('vlrtran', ascending=False) \
                                          .groupby('documento') \
                                          .head(1) \
                                          .reset_index(drop=True)
    
    orden_costos = orden_costos[['documento', 'canal', 'vlrtran']]

    orden_costos.to_csv('./outputs/sol_ej_2.csv', index=False)
    
    return orden_costos

def obtener_transacciones_exitosas_con_porcentaje(itc_df, porcentaje=0.7):
    """
    Obtiene transacciones exitosas donde cada cliente realiza al menos el porcentaje 
    especificado del monto total transferido.
    """
    transacciones_exitosas = itc_df[itc_df['cdgrpta'] == 0]

    total_por_cliente = transacciones_exitosas.groupby('documento')['vlrtran'].sum().reset_index()

    resultado = pd.merge(transacciones_exitosas, total_por_cliente, on='documento', suffixes=('', '_total'))

    resultado = resultado[resultado['vlrtran'] >= resultado['vlrtran_total'] * porcentaje]

    resultado = resultado[['documento', 'cdgrpta', 'vlrtran', 'vlrtran_total']]

    resultado.to_csv('./outputs/sol_ej_3.csv', index=False)

    return resultado

if __name__ == "__main__":
    try:
        master = pd.read_csv("./src/master.csv", sep=",")
        itc = pd.read_csv("./src/ITC.csv", sep=",")

        # Ejercicio 1
        obtener_clientes_masculinos_con_dispositivos(master, itc)

        # Ejercicio 2
        obtener_canal_con_mayor_suma(itc)

        # Ejercicio 3
        obtener_transacciones_exitosas_con_porcentaje(itc)
        
    except Exception as e:
        print(f"Ocurrió un error: {e}")
