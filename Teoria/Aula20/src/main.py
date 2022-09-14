from turtle import onclick
import streamlit as st

st.title('Ola mundo StreamLit🤠')
st.write('Obrigado')
st.markdown("## Subtitulo da **seção**")

st.code(
    '''
    def somar(a,b):
    return a+b
    
val1 = 10
val2 = 12
print(somar(val1,val2))
''',
    language="python"
)

st.code(
    '''
    python -m streamlit run arquivo.py
    ''',
    language="Bash"
)

st.metric(
    label="Total da compra (R$): ",
    value=105.92
)

def fui_apertado():
    print('Ola mundo')

def somar_dois(v1,v2):
    resultado = v1+v2
    st.session_state['kratos'] = resultado
    
numero1 = st.number_input(
    label="Valor 1:",
    min_value = 0,
    max_value = 100
)

numero2 = st.number_input(
    label="Valor 2:",
    min_value = 0,
    max_value = 100
)

st.button(
    label = "Clica ae 🥵",
    help="Herman me comeu",
    on_click=somar_dois,               #chamando o endereço da função quando executado
    kwargs={'v1':numero1,'v2':numero2},
)

if "kratos" in st.session_state:
    st.metric(
        label="Total da compra (R$): ",
        value=st.session_state['kratos']
    )
else:
    st.write('Nenhum calculo foi realizado ainda')

option = st.selectbox(
    'How would you like to be contacted?',
    ('email','home')    
)

st.image(
    image="./assets/img.jpeg",
    caption="Imagem gostosa do moto moto"
)
