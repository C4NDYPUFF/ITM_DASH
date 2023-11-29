import streamlit as st 
import pandas as pd 
import plotly.express as px
from plotting import plot_asistencia, plot_categoria, plot_influencia,plot_registros_evento, plot_asistencia_registros, plot_pie_chart
from data_processing import load_data2_and_plot,load_data, mapear_tipo, mapear_asistencia, renombrar_cargos, renombrar_influencia, renombrar_medio

ITM = load_data(st.secrets['EXCEL_FILE_PATH'])
ITM['Asistencia'] = ITM['Asistencia'].apply(mapear_asistencia)
ITM = mapear_tipo(ITM)
ITM['Cargo'] = ITM['Cargo'].apply(renombrar_cargos)
ITM['Nivel de influencia'] = ITM['Nivel de influencia'].apply(renombrar_influencia)
ITM['¿Cómo se enteró del evento?'] = ITM['¿Cómo se enteró del evento?'].apply(renombrar_medio)


def main_app(df):
    st.set_page_config(page_title='ITM DASHBOARD', page_icon=':bar_chart:', layout='wide')
    # Main page layout
    st.title(':chart_with_upwards_trend: ITM VISITANTES 2019-2023')
    st.markdown('##')

    data_to_plot = { 
            'Evento' : ['2019', '2020', '2021', '2022'],
            'Registros pasados en 2023' : [3144, 0, 1929, 2934],
            'Visitantes que regresaron 2023' : [473,0,465,1035],
            'Visitantes que no regresaron' : [2671, 0 , 1464, 1899]
            
    }

    plot_df = pd.DataFrame(data_to_plot)
    # Reshape the DataFrame
    melted_df = plot_df.melt(id_vars='Evento', var_name='Categoria', value_name='Cantidad')
    # Create a bar plot
    fig = px.bar(melted_df, x='Evento', y='Cantidad', color='Categoria', barmode='group')
    # Customize the plot
    fig.update_layout(
        title='Asistentes de eventos anteriores que estan presentes en 2023',
        xaxis_title='Evento',
        yaxis_title='Cantidad',
        legend_title='Categoria'
    )
    # Show the plot
    fig_evento = plot_registros_evento(ITM)
    st.plotly_chart(fig_evento, use_container_width=True)

    df = df.drop_duplicates(subset='Email', keep='last')

    fig_registros_asistencia = plot_asistencia_registros(ITM)
    st.plotly_chart(fig_registros_asistencia, use_container_width=True)

    st.plotly_chart(fig, use_container_width=True)

    fig_asistencia = plot_asistencia(ITM)
    st.plotly_chart(fig_asistencia, use_container_width=True)

    fig_categoria = plot_categoria(ITM)
    st.plotly_chart(fig_categoria, use_container_width= True)

    fig_influencia = plot_influencia(ITM)
    st.plotly_chart(fig_influencia, use_container_width= True)

    fig_semana = load_data2_and_plot(st.secrets['EXCEL_FILE_PATH2'])
    st.plotly_chart(fig_semana, use_container_width=True)

    ###Plot Pie Chart##3
    fig_2022_medio = plot_pie_chart(ITM, '2022')
    st.plotly_chart(fig_2022_medio, use_container_width=True)

    fig_2023_medio = plot_pie_chart(ITM, '2023')
    st.plotly_chart(fig_2023_medio, use_container_width=True)


main_app(ITM)