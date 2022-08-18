import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

public class Sistema {
    
    public void run(){
        Cliente cliente = new Cliente("Davi", "123456789", "davifssoares2002@gmail.com");
        Conta conta = new Conta(1234, cliente);
        System.out.println(conta);

        Titulo Steam = new Titulo(200, LocalDate.of(2022, 03, 30) , 5);              
        
        conta.depositar(300);
        




        
    }

    public boolean pagarTitulo(Titulo titulo, Conta conta){
        double valorPagar;
        LocalDate dataTitulo = titulo.getData();              //data de compra
        LocalDate hoje = LocalDate.now();                      //data de hoje
        if(dataTitulo.compareTo(hoje) > 0){                   //se a data do titulo 
            valorPagar = titulo.getValor();
        }
        else{
            //AJUSTAR
            long diferencaDias = ChronoUnit.DAYS.between(hoje, dataTitulo);
            for(int i = 0; i<diferencaDias; i++){
                valorPagar *= (titulo.getMultaDiaria()/100);
            }
        }
        return true;
    }

}
