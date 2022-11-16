import streamlit as st
from src.controllers.filme_controller import FilmeController

class HomeView():

    def __init__(self):
        self.filme_controller = FilmeController()

        st.title("Home")

        col1,col2 = st.columns(2,gap="medium")

        if st.session_state["falta"]:
            st.warning(st.session_state["falta"])

        for i in range(0, len(self.filme_controller.get_filmes()) - 1,2):
            with col1:

                filme = self.filme_controller.get_filme(index = i)
                c = st.container()
                c.markdown(f"## {filme.get_nome()}")
                try:
                    c.image(f"{filme.get_url()}")
                except:
                    c.image("assets/reload.png")
                c.markdown(f"## R${filme.get_preco()}")
                qtd1 = c.number_input(label = "", key = 100 * (i+1), format = "%i", step = 1,min_value = 1, max_value = filme.get_saldo())
                if filme.get_saldo() > 0 and filme.get_saldo() - qtd1 >= 0:
                    c.button(label = f"Adicionar {filme.get_nome()}", key = 400 * (i+13), on_click= st.session_state["Cart"].add_filme, args = (filme, qtd1))                 
                else:
                    c.markdown(f"## {filme.get_nome()} em falta")
            with col2:
                filme = self.filme_controller.get_filme(index = i + 1)
                c = st.container()
                c.markdown(f"## {filme.get_nome()}")
                try:
                    c.image(f"{filme.get_url()}")
                except:
                    c.image("assets/reload.png")
                c.markdown(f"## R${filme.get_preco()}")
                qtd2 = c.number_input(label = "",  format = "%i", key = 300 * (i+83), step = 1,min_value = 1, max_value = filme.get_saldo())
                if filme.get_saldo() > 0 and filme.get_saldo() - qtd2 >= 0:    
                    c.button(label = f"Adicionar {filme.get_nome()}", key = 400 * (i+45), on_click= st.session_state["Cart"].add_filme, args = (filme, qtd2))
                else:
                    c.markdown(f"## {filme.get_nome()} em falta")