import plotly.express as px 
from data_processing import load_data, mapear_asistencia, mapear_tipo, renombrar_cargos

def plot_asistencia(df):

    table = df.groupby(['Empresa', 'Asistencia', 'FechaEvento']).size().reset_index(name='Cantidad')
    #table = table[table['Asistencia'].str.contains('SI')]
    table['Empresa_Asistencia'] = table['Empresa'] + " - " + table['Asistencia']
    fig = px.bar(table, x="FechaEvento", y="Cantidad", color="Empresa_Asistencia", barmode='group',
             title="Cantidad de Asistencia por Empresa y Año")
    return fig 


def plot_categoria(df):
    table = df.groupby(['Cargo', 'Asistencia', 'FechaEvento']).size().reset_index(name='Cantidad')
    table = table[table['Asistencia'].str.contains('SI')]
    fig = px.bar(table, x='FechaEvento', y='Cantidad', color='Cargo', barmode='group', 
                 title='Asistentes por Categoria para cada ITM')
    return fig

def plot_influencia(df):
    table = df.groupby(['Nivel de influencia', 'Asistencia', 'FechaEvento']).size().reset_index(name='Cantidad')
    table = table[table['Asistencia'].str.contains('SI')]
    #table['Nivel de influencia_Asistencia'] = table['Nivel de influencia'] + '-' + table['Asistencia']
    fig = px.bar(table, x='FechaEvento', y='Cantidad', color='Nivel de influencia', barmode='group', 
                 title='Asistentes por Nivel de influencia para cada ITM')
    return fig

def plot_registros_evento(df):
    value_count = df['FechaEvento'].value_counts().reset_index()
    value_count.columns = ['Evento', 'Cantidad']
    fig = px.bar(value_count, x='Evento', y='Cantidad', color='Evento', barmode='group',
                 title='Registros por Evento ITM')

    return fig

def plot_asistencia_registros(df):
    table = df.groupby(['Asistencia', 'FechaEvento']).size().reset_index(name='Cantidad')
    fig = px.bar(table, x='FechaEvento', y='Cantidad', color='Asistencia', barmode='group',
                 title='Asistentes por Evento')

    return fig 