public abstract class Produto implements IGerarDesconto{
    private final double preco;              //final = torna como um "const"
    private final String nome;
    private int quantidade;
    private final String descricao;
    
    public Produto(double preco, String nome, int quantidade, String descricao) {
        this.preco = preco;
        this.nome = nome;
        this.quantidade = quantidade;
        this.descricao = descricao;
    }

    public double getPreco() {
        return preco;
    }

    public String getNome() {
        return nome;
    }

    public int getQuantidade() {
        return quantidade;
    }

    public void setQuantidade(int quantidade) {
        this.quantidade = quantidade;
    }

    public String getDescricao() {
        return descricao;
    }

    @Override
    public String toString() {
        return "Produto [descricao=" + descricao + ", nome=" + nome + ", preco=" + preco + ", quantidade=" + quantidade
                + "]";
    }

    
}
