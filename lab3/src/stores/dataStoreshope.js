import { defineStore } from "pinia";
import products from '@/components/products';

export const usedatastore=defineStore("dataStore",{

    state:()=>({
       
        products: products,
        iscartvisible: false,
        cart: {
          items: []
        } 
          
    }),

})