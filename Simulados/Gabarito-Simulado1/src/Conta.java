public class Conta {
    private int idConta;
    private double saldo;
    private static int totalContas = 0;
    
    public Conta() {
        this.saldo = 0;
        this.idConta = totalContas;
        totalContas++;
    }

    public boolean depositar(double valor){
        if(valor < 0)
            return false;
        this.saldo += valor;
        return true;                      //para somente indicar que o deposito foi realizado de fato
    } 

    public boolean sacar(double valor){
        if(valor > this.saldo) 
            return false;
        this.saldo -= valor;
        return true;                  //para indicar que o saque foi realizado
    }

    public boolean transferir(double valor, Conta destino){
        if(!sacar(valor))
            return false;                //caso não consegui sacar o valor, ele já retorna 'false'
        return destino.depositar(valor);          //estudar esta linha
    }

    public int getIdConta() {
        return idConta;
    }

    public double getSaldo() {
        return saldo;
    }

    @Override
    public String toString() {
        return "Conta [idConta=" + idConta + ", saldo=" + saldo + "]";
    }
}
