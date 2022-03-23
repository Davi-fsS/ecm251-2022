public class Conta {

    //Atributos de nossa classe
    private int numero;                  //privando de serem instanciados no app
    private double saldo;

    //Constructor !
    public Conta(int numero){
        this.numero = numero;
        saldo = 0;
    }

    //Métodos de nossa classe
    public void visualizarConta(){
        System.out.println("Numero: "+this.numero);
        System.out.println("Saldo: "+this.saldo);
    }

    public void visualizarSaldo(){
        System.out.println("Saldo atual: "+this.saldo);
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
}
