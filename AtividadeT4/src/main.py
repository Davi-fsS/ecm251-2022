# Davi Fernandes Simões Soares (20.01099-0)

#Importando streamlit
import streamlit as st

#Importanto Controller necessario
from src.controllers.carrinho_controller import CarrinhoController

#Importando todos os Views
from src.views.login_view import LoginView
from src.views.sidebar_home_view import SideBarHomeView
from src.views.home_view import HomeView
from src.views.cadastro_usuario import CadastroUsuario
from src.views.perfil_view import PerfilView
from src.views.carrinho_view import CarrinhoView
from src.views.cadastro_view import CadastroView

if "Login" not in st.session_state:

    st.session_state["Profile"] = "dados"

    st.session_state["Login"] = "negado"

    st.session_state["Usuario"] = ""

    st.session_state["email"] = ""

    st.session_state["falta"] = ""

    st.session_state["Cart"] = CarrinhoController()

    st.session_state["carrinho"] = ""

with st.sidebar:

    if st.session_state["Login"] == "negado" or st.session_state["Login"] == "errado":
        LoginView()
    
    if st.session_state['Login'] == 'errado':
        st.markdown("***")
        st.markdown("# Email ou senha incorreto!")
        
    if st.session_state["Login"] == "registro":
        CadastroUsuario()

    if st.session_state["Login"] == "aprovado":
        SideBarHomeView()

if "Login" in st.session_state:

    if st.session_state["Login"] == "negado" or st.session_state["Login"] == "errado":
        st.title('Seja Bem Vindo à sua Loja de Filmes favorita!')
        st.markdown('Utilize o login auto-preenchido ou crie um cadastro')
        st.markdown('Importante! Além de anotar suas credenciais criadas, **APENAS fãs de Cristopher Nolan** podem entrar nesse site!')
        st.write("")
        st.write("")
        st.write("")
        st.image('https://images7.memedroid.com/images/UPLOADED695/5fc58c468abb5.jpeg')

    if st.session_state["Login"] == "aprovado":
        
        tab1, tab2, tab3 = st.tabs(["Home", "Carrinho", "Cadastrar Filme"])

        with tab1:
            HomeView()
        with tab2:
            CarrinhoView()
        with tab3:
            CadastroView()
            
        