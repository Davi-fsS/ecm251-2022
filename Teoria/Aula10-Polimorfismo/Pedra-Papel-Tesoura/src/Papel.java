public class Papel extends Jogada{

    public Papel() {
        super(EnumJogadas.PEDRA,EnumJogadas.SPOCK);   //pedra e spock
    }

    @Override
    public EnumJogadas getTipo() {
        return EnumJogadas.PAPEL;
    }
    
}
