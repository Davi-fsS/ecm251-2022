import streamlit as st

class CarrinhoView():

    def __init__(self):

        st.title("Carrinho")

        col1, col2, col3 = st.columns(3,gap="large")
        col1.markdown("### Produto")
        col2.markdown("### Preço")
        col3.markdown("### Quantidade")
        
        
        filme_qtd = []
        filme_nomes = []
        filme_preco = []
        for filme_qtds in st.session_state["Cart"].get_carrinho().get_filmes():
            filme_nomes.append(filme_qtds[0].get_nome())
            filme_preco.append(filme_qtds[0].get_preco())
            filme_qtd.append(filme_qtds[1])
                
        with col1:
            container1 = st.container()
            for i in range(len(filme_nomes)):
                container1.text(f"{filme_nomes[i]}")
        with col2:
            container2 = st.container()
            for i in range(len(filme_nomes)):
                container2.text(f"R${filme_preco[i]}")
        with col3:
            container3 = st.container()
            for i in range(len(filme_nomes)):
                container3.text(f"{filme_qtd[i]}")

        st.markdown("***")
        total = st.session_state["Cart"].get_total_preco()
        
        st.markdown(f"## Valor total: R${total:.2f} ")
        st.button(label = "Finalizar Pedido", key = 998, on_click= st.session_state["Cart"].limpar_carrinho)
    