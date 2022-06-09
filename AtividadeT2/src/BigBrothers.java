public class BigBrothers extends Integrantes{
    
    public BigBrothers(String nome, String email, String turno) {
        super(nome, email, turno);
        this.funcao = "BigBrother";
    }

    @Override
    public void postagens() {
        if(turno.equals("regular")){
            System.out.println("Sempre ajudando as pessoas membros ou não S2!");
        }
        if(turno.equals("extra")){
            System.out.println("...");
        }
        
    }

}
