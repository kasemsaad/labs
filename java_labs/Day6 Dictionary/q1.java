import java.util.ArrayList;
import d.Dictionary;
public class q1{

 public static void main(String[] args){
        Dictionary Dictionary=new Dictionary();
        ArrayList<String> arr1=new ArrayList<>();
        arr1.add("skoda");
        arr1.add("toyota");
        arr1.add("tesla");
        arr1.add("seat");
        arr1.add("nissan");
        arr1.add("mg");
        arr1.add("isuzu");

        ArrayList<String> arr2=new ArrayList<>();
        arr2.add("iveco");
        arr2.add("jeep");
        arr2.add("honda");
        arr2.add("gmc");
        arr2.add("hummer");
        arr2.add("fiat");
        arr2.add("ford");

        ArrayList<String> arr3=new ArrayList<>();
        arr3.add("gelly");
        arr3.add("haval");
        arr3.add("bmw");
        arr3.add("byd");
        arr3.add("proton");
        arr3.add("ram");
        arr3.add("porsche");

        Dictionary.addElement(arr1, "A");
        Dictionary.addElement(arr2, "B");
        Dictionary.addElement(arr3, "C");
        
        Dictionary.print();

        Dictionary.sorted();

        Dictionary.print();

        Dictionary.printSpecfici("B");
 
 
 
    }


}