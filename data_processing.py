import pandas as pd 
import streamlit as st


def load_data(file_path):
    df = pd.read_excel(file_path)

    return df


def renombrar_cargos(cargo):
    # Convertimos el cargo a cadena si no es NaN, en caso contrario retornamos 'OTROS'
    if pd.isna(cargo):
        return 'INFORMACION NO DISPONIBLE'
    cargo_str = str(cargo).upper()
    # Verificamos si el cargo contiene la palabra 'DIRECTOR'
    if 'DIRECTOR' in cargo_str:
        return 'DIRECTOR'
    if 'JEFE' in cargo_str:
        return 'DIRECTOR'
    # Lista de otros cargos que queremos mantener
    otros_cargos_permitidos = ['ESTUDIANTE', 'GERENTE', 'VENTAS', 'PERSONAL OPERATIVO']
    # Verificamos si el cargo actual contiene algún otro cargo permitido
    for oc in otros_cargos_permitidos:
        if oc in cargo_str:
            return oc
    # Si el cargo no es uno de los permitidos, lo renombramos a 'OTROS'
    return 'OTROS'

def mapear_asistencia(asistencia):
    if pd.isna(asistencia):
        return 'NO'
    if asistencia == True:
        return 'SI'
    if asistencia == False:
        return 'NO'
    else:
        return str(asistencia).upper()
    

def mapear_tipo(df):
    df['Empresa'] = df['Empresa'].astype(str).str.upper()
    match_string = 'UNIVERSIDAD'
    df['Empresa'] = df['Empresa'].apply(lambda x: 'UNIVERSIDAD' if match_string in x else('OTROS' if x == 'NAN' else 'EMPRESA'))
    return df

def renombrar_influencia(influencia):
    if pd.isna(influencia) or str(influencia).strip() == '0':
        return 'INFORMACIÓN NO DISPONIBLE'

    influencia_str = str(influencia).upper().strip()

    if 'NO SOY PARTE' in influencia_str:
        return 'NO PARTICIPA EN COMPRAS'
    elif 'PARTE DEL EQUIPO' in influencia_str or 'TOMA DE DECISIÓN' in influencia_str:
        return 'APRUEBO COMPRAS'
    elif 'INVESTIGO' in influencia_str or 'RECOMIENDO' in influencia_str:
        return 'EVALUO Y/O RECOMIENDO'
    elif 'COMPRAS' in influencia_str:
        return 'RESPONSABLE DE COMPRAS'
    elif 'APRUEBO' in influencia_str:
        return 'APRUEBA COMPRAS'
    else:
        return 'OTROS'