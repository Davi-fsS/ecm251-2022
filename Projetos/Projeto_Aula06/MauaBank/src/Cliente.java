import javax.sound.midi.VoiceStatus;

public class Cliente {
    //Atributos
    private String cpf;
    private String nome;
    private String email;

    //Constructor !
    public Cliente(String nome, String cpf, String email){
        this.nome = nome;
        this.cpf = cpf;
        this.email = email;
    }

    //Métodos 
    public void visualizarCliente(){
        System.out.println("--Dados do cliente--");
        System.out.println("Nome: "+nome);
        System.out.println("CPF: "+cpf);
        System.out.println("E-mail: "+email);
    }

    //Getters

    public String getNome(){
        return nome;
    }

    public String getCpf(){
        return cpf;
    }

    public String getEmail(){
        return email;
    }

    //Setters

    public void setNome(String nome){
        this.nome = nome;
    }

    public void setEmail(String email){
        this.email = email;
    }    
}
