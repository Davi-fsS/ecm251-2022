public class Jogada {
    private final EnumJogadas venco; //atribui aquele valor até o final da exec.
    private final EnumJogadas venco1;

    public Jogada(EnumJogadas venco, EnumJogadas venco1) {
        this.venco = venco;
        this.venco1 = venco1;
    }
    
    public boolean verificarVenceu(Jogada jogada){
        if(jogada.getTipo().equals(venco) || jogada.getTipo().equals(venco1))
            return true;
        return false;

    }

    public EnumJogadas getTipo(){
        return EnumJogadas.PAPEL;
    }
}
