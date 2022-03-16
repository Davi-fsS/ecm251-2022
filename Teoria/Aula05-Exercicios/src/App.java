public class App {
    public static void main(String[] args) throws Exception {

        //Declara e instancia um objeto do tipo Conta
        Conta contaDavi = new Conta();
        Conta contaMurilo = new Conta();

        
        contaDavi.abrirConta(1,"Davi",200.0,"471.646.098-37");
        contaDavi.visualizarSaldo();

        if(!contaDavi.depositar(300)){
            System.out.println("Operação falhou!");
        }
        
        if(!contaDavi.sacar(600)){
            System.out.println("Operação falhou!");
        }

        contaDavi.visualizarSaldo();
        contaDavi.transferirDinheiro(-300,contaMurilo);
        
        contaMurilo.visualizarSaldo();
        contaDavi.visualizarSaldo();
    }
}
