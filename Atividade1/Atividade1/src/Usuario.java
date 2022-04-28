// DAVI FERNANDES SIMÕES SOARES - 20.01099-0

public class Usuario {
    private String nome;
    protected BemCompartilhado transporte;
    
    public Usuario(String nome, BemCompartilhado transporte) {
        this.nome = nome;
        this.transporte = transporte;
    }

    public String getNome() {
        return nome;
    }

    public BemCompartilhado getTransporte() {
        return transporte;
    }

    @Override
    public String toString() {
        return "Usuario [nome=" + nome + ", transporte=" + transporte + "]";
    }

    public void TrocaVeiculos(/*BemCompartilhado transporte,*/BemCompartilhado tipo2){
        /*if(transporte.getTipo() != tipo2.getTipo()){
            this.transporte = tipo2;
        }                                                   NÃO DEU TEMPO!!
        System.out.println("Não é possível.");
        */
        this.transporte = tipo2;
    }
}
