public class Spock extends Jogada{
    
    public Spock(){
        super(EnumJogadas.TESOURA,EnumJogadas.PEDRA);   //tesoura e pedra
    }

    @Override
    public EnumJogadas getTipo() {
        return EnumJogadas.LAGARTO;
    }
}
