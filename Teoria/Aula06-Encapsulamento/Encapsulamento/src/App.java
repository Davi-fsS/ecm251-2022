public class App {
    public static void main(String[] args){
        Cliente c1 = new Cliente(
            "Murilo",
            "1234568979",
            "20010990@maua.br",
            new Conta(1234)
        );

        System.out.println("Nome do cliente:" + c1.getNome());
        System.out.println("CPF do cliente:" + c1.getCpf());
        System.out.println("Email do cliente:" + c1.getEmail());
        c1.getConta().visualizarConta();
    }
}
