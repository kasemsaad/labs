import { defineStore } from "pinia";
import books from '@/components/books';

export const usedatastore=defineStore("dataStore",{

    state:()=>({
       
       books: books,
       iscartvisible: false,
       hideButton: false,
       cart: {
           items: []
       }      
          
    }),
    actions:{
        remove(item) {
            const index = this.datastore.cart.items.findIndex(iitem => iitem.book.id === item.book.id);

            if (index !== -1) {
                this.datastore.cart.items.splice(index, 1);
                item.book.instock += item.quantity;
            }
        },
        isInCart(book) {
            return this.datastore.cart.items.some(iitem => iitem.book.id === book.id);
        },
        addToCart(book) {
            if (this.datastore.cart.items.some(iitem => iitem.book.id === book.id)) {
                this.datastore.cart.items.find(iitem => iitem.book.id === book.id).quantity++;
            } else {
                this.datastore.cart.items.push({ book: book, quantity: 1 });
            }
            book.instock--;
        }
    }

})