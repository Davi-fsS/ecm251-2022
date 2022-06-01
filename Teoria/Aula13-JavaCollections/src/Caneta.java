public class Caneta {
    public final String cor;
    public final Double ponta;

    public Caneta(String cor, Double ponta) {
        this.cor = cor;
        this.ponta = ponta;
    }
    
    @Override
    public String toString() {
        return "Caneta [cor=" + cor + ", ponta=" + ponta + "]";
    }
}
