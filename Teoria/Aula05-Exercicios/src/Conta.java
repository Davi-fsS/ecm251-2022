public class Conta {

    //Atributos de nossa classe
    int numero;
    String titular;
    double saldo;
    String cpf;

    //Métodos de nossa classe
    void abrirConta(int numero,String titular,double saldo,String cpf){
        this.numero = numero;
        this.titular = titular;
        this.saldo = saldo;
        this.cpf = cpf;
    }
    
    void visualizarSaldo(){
        System.out.println("Saldo atual: "+this.saldo);
    }

    boolean depositar(double dinheiro){
        if(dinheiro < 0) return false;
        this.saldo += dinheiro;
        return true;
    }

    boolean sacar(double dinheiro){
        if(dinheiro > this.saldo) return false;
        if(dinheiro < 0) return false;
        this.saldo -= dinheiro;
        return true;
    }

    boolean transferirDinheiro(double dinheiro,Conta destino){
        if(!sacar(dinheiro)) return false;
        if(!destino.depositar(dinheiro)) return false;
        return true;
    }
}
