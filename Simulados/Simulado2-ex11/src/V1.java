public class V1 {
    int v[] = {2,3,1,4,2,5,3,8,2,3};

    int mv1(){
        int s = 0;
        for(int i=0;i<v.length;i+=2){
            s+=v[i];
        }
        System.out.println("passei aq: MV1 do V1");
        return s;
    }

    float mv2(int x){
        System.out.println("passei aq: MV2 do V1 int");
        return x + this.mv1();
        
    }

    float mv2(float x){
        System.out.println("passei aq: MV2 do V1 float");
        return 3 + x * this.mv1();
        
    }
}
