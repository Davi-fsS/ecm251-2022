public class Atividade1 {
    public static void run(){         //o "static" deixa executar sem a necessidade de criar uma instancia
        Usuario usuario1 = new Usuario("All Might", "132456", "naotenhoemail@gmail.com");
        Usuario usuario2 = new Usuario("One For All", "gkjkfjhakhfjhnaheuehhn", "all@gmail.com");
        Usuario usuario3 = new Usuario("Bakugo", "1e14123", "tchaudeku@gmail.com");

        usuario1.getConta().depositar(1000);
        usuario2.getConta().depositar(250);
        usuario3.getConta().depositar(3000);

        String qrCode1 = Transacoes.gerarQrCode(usuario1.getConta().getIdConta(), usuario1.getNome(), 250);        //estudar isso
        
        System.out.println("Transacao 1:"+usuario2.getConta().transferir(extrairValorQrCode(qrCode1),usuario1.getConta()));
        System.out.println("Transacao 2:"+usuario3.getConta().transferir(extrairValorQrCode(qrCode1),usuario1.getConta()));
        System.out.println("Transacao 3:"+usuario2.getConta().transferir(extrairValorQrCode(qrCode1),usuario1.getConta()));

        String qrCode2 = Transacoes.gerarQrCode(usuario2.getConta().getIdConta(), usuario2.getNome(), 1000);        //estudar isso
        System.out.println("Transacao 4:"+usuario3.getConta().transferir(extrairValorQrCode(qrCode2), usuario2.getConta()));

    }

    private static double extrairValorQrCode(String qrCode){
        String valorComVirgula = qrCode.split(";")[2];
        String valorSemVirgula = valorComVirgula.replace(",",".");
        return Double.parseDouble(valorSemVirgula);
    }
}
