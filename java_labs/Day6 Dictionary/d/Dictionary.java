package d;

import java.util.*;

public class Dictionary{
    Map<String,ArrayList<String>> Dictionary;
    public Dictionary()
    {
        Dictionary=new HashMap<>();

    }
   public void addElement(ArrayList<String> sentences, String key)
    {
        Dictionary.put(key,sentences);
    }
    public void sorted(){
        Dictionary.forEach((key,list)->Collections.sort(list));
    }
    public void print()
    {
        Dictionary.forEach((key,list)->System.out.println("key : "+key +" list : "+ list));
    }
    public void  printSpecfici(String  l)
    {
        Dictionary.forEach((key,value)->{
            if(key==l)
            {
                System.out.println("key : "+key+" value : "+value);
            }
        });
    }
}