from faulthandler import disable
import streamlit as st
from streamlit_option_menu import option_menu
from controllers.carrinho_controller import CarrinhoController
from .carrinho_view import CarrinhoView
a = []
class HomeView():
    def __init__(self) -> None:
        self.carrinho = CarrinhoController()

        with st.sidebar:
            selected = option_menu(
                menu_title=None,
                options=["Home","Categorias","Carrinho"],
                icons=["house-fill","bookmark-fill","cart-fill"],
                default_index=0,
                orientation="vertical",
            )

        if selected == "Home":

            st.write("### Conheça as nossas mídias para alugar!\n\n")

            col1, col2, col3= st.columns(3, gap="medium")
            
            with col1:
                titulo = "Interestelar"
                preco = 30.00
                st.write(f"### {titulo}")
                st.image("../assets/interestelar.jpg",use_column_width=True)
                st.write(f"R$ {preco}")
                st.button("🛒", key='f1', on_click=self.carrinho.adicionando_no_carrinho(titulo,preco))
                if st.session_state.f1 == True:
                    st.info("Interestellar está no 🛒")
                    a.append(preco)
                    st.session_state.filme = a
            with col2:
                titulo = "A Origem"
                preco = 22.00
                st.write(f"### {titulo}")
                st.image("../assets/inception.jpg",use_column_width=True)
                st.write(f"R$ {preco}") 
                st.button("🛒", key='f2', on_click=self.carrinho.adicionando_no_carrinho(titulo,preco))
                if st.session_state.f2 == True:
                    st.info("A Origem está no 🛒")
                    a.append(preco)
                    st.session_state.filme = a

            with col3:
                titulo = "Bastardos Inglórios"
                preco = 24.00
                st.write(f"#### {titulo}")
                st.image("../assets/bastardos.jpg",use_column_width=True)
                st.write(f"R$ {preco}")
                st.button("🛒", key='f3', on_click=self.carrinho.adicionando_no_carrinho(titulo,preco))
                if st.session_state.f3 == True:
                    st.info("Bastardos Inglórios está no 🛒")
                    a.append(preco)
                    st.session_state.filme = a

            col4,col5,col6 = st.columns(3, gap="medium")

            with col4:
                titulo = "Tenet"
                preco = 20.00
                st.write(f"### {titulo}")
                st.image("../assets/tenet.jpg",use_column_width=True)
                st.write(f"R$ {preco}", on_click=self.carrinho.adicionando_no_carrinho(titulo,preco))
                st.button("🛒", key='f4')
                if st.session_state.f4 == True:
                    st.info("Tenet está no 🛒")
                    a.append(preco)
                    st.session_state.filme = a

            with col5:
                titulo = "Dark Knight"
                preco = 22.00
                st.write(f"### {titulo}")
                st.image("../assets/dark1.jpg",use_column_width=True)
                st.write(f"R$ {preco}")
                st.button("🛒", key='f5', on_click=self.carrinho.adicionando_no_carrinho(titulo,preco))
                if st.session_state.f5 == True:
                    st.info("Dark Knight está no 🛒")
                    a.append(preco)
                    st.session_state.filme = a

            with col6:
                titulo = "Dark Knight Rises"
                preco = 24.00
                st.write(f"### {titulo}")
                st.image("../assets/dark2.jpg",use_column_width=True)
                st.write(f"R$ {preco}")
                st.button("🛒", key='f6', on_click=self.carrinho.adicionando_no_carrinho(titulo,preco))
                if st.session_state.f6 == True:
                    st.info("Dark Knight Rises está no 🛒")
                    a.append(preco)
                    st.session_state.filme = a

        if selected == "Categorias":

            st.title("Categorias")
            st.warning("está de backlog ainda, não era requisito")

        if selected == "Carrinho":
            
            CarrinhoView()
