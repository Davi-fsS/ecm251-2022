public class Leitura extends Produto{

    public final EnumGeneros genero;
    public final String editora;
    public final String paisOrigem;
    public final int paginas;

    public Leitura(double preco, String nome, int quantidade, String descricao, EnumGeneros genero, String editora,
            String paisOrigem, int paginas) {
        super(preco, nome, quantidade, descricao);
        this.genero = genero;
        this.editora = editora;
        this.paisOrigem = paisOrigem;
        this.paginas = paginas;
    }

    @Override
    public double gerarDesconto() {
        return getPreco()*0.8;
    }
    
}
