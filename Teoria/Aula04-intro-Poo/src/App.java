public class App {
    public static void main(String[] args) {
        //Declara e Instancia um objeto do tipo Caneta

        System.out.println();

        //CANETA C1
        Caneta c1 = new Caneta();
        c1.iniciarCaneta("Azul", "BIC",1.0);
        c1.escrever("Ola mundo o Batman Novo é um bom filme aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa");
        c1.mostrarCarga();
        
        System.out.println();

        //CANETA C2
        Caneta c2 = new Caneta();
        c2.iniciarCaneta("Vermelha", "Stabillo", 0.4);
        c2.escrever("Missão impossível pode mesmo ser o homem de ferro?");
        c2.mostrarCarga();

        System.out.println();

    }
}