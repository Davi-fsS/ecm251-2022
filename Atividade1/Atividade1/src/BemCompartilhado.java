import java.util.concurrent.ThreadLocalRandom;

// DAVI FERNANDES SIMÕES SOARES - 20.01099-0

public class BemCompartilhado {
    
    protected String tipo;
    private int id;

    public BemCompartilhado() {
        this.tipo = "";
        this.id = ThreadLocalRandom.current().nextInt(1000, 10000);

    }

    public String getTipo() {
        return tipo;
    }

    public void testar1(){
        int id = ThreadLocalRandom.current().nextInt(1000, 10000);
        System.out.println("ID:"+id+"\nTipo:"+tipo);
    }  //esta funcionando

    public int getId() {
        return id;
    }

}
