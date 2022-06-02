public class V2 extends V1{
    int mv1(){
        int s = 0;
        for(int i=1;i<v.length;i+=2){
            s+=v[i];
        }
        System.out.println("passei aq: MV1 do V2");
        return s;
    }

    float mv2(float x){
        System.out.println("passei aq: MV2 do V2");
        return 3 + x * this.mv1();
    }
}
