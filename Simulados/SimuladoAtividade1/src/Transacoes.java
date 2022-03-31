public class Transacoes {
    //DEVE POSSUIR INFORMACOES APENAS SOBRE AS TRANSAÇÕES
    //NÃO DEVE POSSUIR NENHUM ATRIBUTO
    
    /*
        - Toda transação deve ser composta pelo id da conta;
        - A String gerada deve conter o nome do usuário que vai receber o valor;
        - A String gerada deve conter o valor da transação;
    */

    public String gerarQRCode(int idConta, String nome ,boolean valor){
        return(""+idConta+";"+nome+";"+valor+"");
    }
}
