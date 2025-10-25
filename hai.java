import java.util.Scanner;

public class hai {
    public static void insertionsort(int [] dataku){
        int n = dataku.length;
        int v,j;
        for (int i = 1; i < n; i++){
            v = dataku[i];
            j = i-1;
            while (j >= 0 && dataku[j] > v){
                dataku[j+1] = dataku[j];
                j = j-1;
            }
            dataku[j+1] = v;
        }
    }
    public static void viewdata(int [] dataku){
        for(int i=0; i<dataku.length; i++){
            System.out.print(dataku[i] + " ");
        }
        System.out.println("");
    }
    public static int binarysearch(int [] dataku, int key){
        int bawah = 0;
        int atas = dataku.length -1;
        
        while(atas >= bawah){
            int tengah = (bawah+atas)/2;

            if(key == dataku [tengah]){
                return (tengah+1);
            }
            else if(key < dataku [tengah]){
                atas = tengah-1;
            }
            else
            bawah = tengah+1;
        }
        return 0;
    }
    public static void main(String[] args) {
        int [] dataku = {28,18,93,81,38,82,36};
        Scanner x = new Scanner(System.in);
        System.out.println("Masukkan angka yang mau dicari : ");
        int angkaCari = x.nextInt();
        System.out.println("Data yang sudah diurutkan :");
        insertionsort(dataku);
        viewdata(dataku);
        int indeks = binarysearch(dataku, angkaCari);

        if(indeks!=0){
            System.out.println("Angka "+angkaCari+" ditemukan pada urutan ke - "+indeks);
        }
        else{
            System.out.println("Angka "+angkaCari+" Tidak ditemukan");
        }
    }


}