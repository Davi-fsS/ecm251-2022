/*
Davi Fernandes Simões Soares
20.01099-0
*/

public class Atividade1 {
    public static void main(String[] args) throws Exception {
        
        Conta conta1 = new Conta(1, 200);
        Usuarios Perigo = new Usuarios("Davi", "123", "davifssoares@gmail.com", conta1);
        Perigo.getNome();

        Conta conta2 = new Conta(2,300);
        Usuarios Perigo2 = new Usuarios("Betinho", "124", "davifssoares@gmail.com", conta2);
        Perigo2.getNome();


    }
}
