public class Conta {

    //Atributos de nossa classe
    private int numero;                  //privando de serem instanciados no app
    private double saldo;
    private Cliente cliente;

    //Constructor !
    public Conta(int numero,Cliente cliente){
        this.numero = numero;
        saldo = 0;
        this.cliente = cliente;
    }

    //Métodos de nossa classe
    public void visualizarConta(){
        System.out.println("Numero: "+this.numero);
        System.out.println("Saldo: "+this.saldo);
    }

    public String visualizarSaldo(){
        return "R$ "+ String.format("R$ %.2f",saldo);
    }

    public boolean depositar(double dinheiro){
        if(dinheiro < 0) return false;
        this.saldo += dinheiro;
        return true;
    }

    public boolean sacar(double dinheiro){
        if(dinheiro > this.saldo) return false;
        if(dinheiro < 0) return false;
        this.saldo -= dinheiro;
        return true;
    }

    public boolean transferirDinheiro(double dinheiro,Conta destino){
        if(!sacar(dinheiro)) return false;
        if(!destino.depositar(dinheiro)) return false;
        return true;
    }

    public String toString(){
        return "Conta Número: " + numero + 
        "\nSaldo: " + visualizarSaldo() + 
        "\nCliente: " + cliente.getNome();
    }
}
