public class MobileMembers extends Integrantes{

    public MobileMembers(String nome, String email, String turno) {
        super(nome, email,turno);
        this.funcao = "MobileMember";
    }

    @Override
    public void postagens() {
        if(turno.equals("regular")){
            System.out.println("Happy Coding!");
        }
        if(turno.equals("extra")){
            System.out.println("Happy_C0d1ng. Maskers");
        }
        
    }

}
