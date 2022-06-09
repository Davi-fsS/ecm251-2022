public abstract class Integrantes implements Interface{
    private final String nome;
    private final String email;
    protected String turno;
    protected String funcao;
    //private Turno turno;
    
    public Integrantes(String nome, String email, String turno) {
        this.nome = nome;
        this.email = email;
        this.turno = turno;
        this.funcao = "";
    }

    public String getNome() {
        return nome;
    }

    public String getEmail() {
        return email;
    }

    public String getTurno() {
        return turno;
    }

    @Override
    public void MudarTurno(String turnoNovo) {
        turno = turnoNovo;
    }

    public String getFuncao() {
        return funcao;
    }

    @Override
    public String toString() {
        return "Integrantes [email=" + email + ", funcao=" + funcao + ", nome=" + nome + ", turno=" + turno + "]";
    }

}
