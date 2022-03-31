public class Conta {
    public int idConta;
    private double saldo;

    public Conta(int idConta, double saldo){
        this.idConta = idConta;
        this.saldo = saldo;
    }

    public void getIdConta(){
        System.out.println(this.idConta);
    }

    public void getSaldo(){
        System.out.println(this.saldo);
    }

    boolean depositar(double dinheiro){
        if(dinheiro < 0) return false;             //checar se o dinheiro a ser digitado é positivo
        this.saldo += dinheiro;                    //realiza o deposito 
        return true;
    }

    boolean sacar(double dinheiro){  
        if(dinheiro > this.saldo) return false;     //checar se o dinheiro a ser sacado é maior que o disponível
        if(dinheiro < 0) return false;              //checar se o dinheiro a ser sacado é positivo
        this.saldo -= dinheiro;                     
        return true;
    }

    boolean transferirDinheiro(double dinheiro,Conta destino, Transacoes transacao, Usuarios usuario){
        if(!sacar(dinheiro)) return false;                       
        if(!destino.depositar(dinheiro)){
            transacao.gerarQRCode(this.idConta,usuario.nome,destino.depositar(dinheiro));
            return false;
        } 
        
        return true;
    }
}
