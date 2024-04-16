<template>
    <div id="myapp">
        <section class="wrapper">
            <div class="row">
                <div class="col text-center mb-5">
                    <h1 class="display-4 font-weight-bolder">Books</h1>
                    <div class="d-flex align-items-baseline justify-content-center text-light p-2 m-2">
                        <a href="#" style="color:yellow;text-decoration:none;" @click.prevent="iscartvisible=false">books</a>
                        <div class="align-items-baseline d-flex">
                            <p class="mx-1">[{{datastore.cart.items.length}}] <template v-if="datastore.cart.items.length==1">item</template></p>
                            <button class="btn btn-warning" @click="iscartvisible=true">wishlist</button>
                        </div>
                    </div>
                </div>
            </div>
            <!-- //////////////////////////////////////////books//////////////////////////////////////// -->
            <div class="row" v-if="!iscartvisible">
                <div class="col-sm-12 col-md-6 col-lg-4 mb-4" v-for="book in datastore.books" :key="book.id">
                    <div class="card text-dark card-has-bg click-col" style="height: 35vw;">
                        <img class="card-img d-none" :src="book.image" alt="Creative Manner Design Lorem Ipsum Sit Amet Consectetur dipisi?">
                        <div class="card-img-overlay d-flex flex-column">
                            <div class="card-body">
                                <div style="width: 100%; height: 15vw;">
                                    <img class="card-img w-100 h-100" :src="book.image" alt="Create">
                                </div>
                                <small class="card-meta mb-2">{{book.isbn}}</small>
                                <h4 class="card-title mt-0 "><a class="text-dark" href="https://creativemanner.com">{{book.name}}</a></h4>
                                <small><i class="far fa-clock"></i> price : {{book.price}}</small>
                                <div class="card-footer">
                                    <div class="media">
                                        <img class="mr-3 rounded-circle" src="https://assets.codepen.io/460692/internal/avatars/users/default.png?format=auto&688931977&width=80&height=80" alt="Generic placeholder image" style="max-width:50px">
                                        <div class="media-body">
                                            <h6 class="my-0 text-dark d-block">Author : {{book.author}}</h6>
                                            <small>category : {{book.category}}</small>
                                            <button class="btn btn-primary ms-5" v-if="!isInCart(book)" @click="addToCart(book); book.hideButton = true">Add To Wishlist</button>
                                            <svg class="ms-5" xmlns="http://www.w3.org/2000/svg" width="40" height="40" fill="red"  viewBox="0 0 16 16" v-else>
                                                <path d="M1 2.828c.885-.37 2.154-.769 3.388-.893 1.33-.134 2.458.063 3.112.752v9.746c-.935-.53-2.12-.603-3.213-.493-1.18.12-2.37.461-3.287.811zm7.5-.141c.654-.689 1.782-.886 3.112-.752 1.234.124 2.503.523 3.388.893v9.923c-.918-.35-2.107-.692-3.287-.81-1.094-.111-2.278-.039-3.213.492zM8 1.783C7.015.936 5.587.81 4.287.94c-1.514.153-3.042.672-3.994 1.105A.5.5 0 0 0 0 2.5v11a.5.5 0 0 0 .707.455c.882-.4 2.303-.881 3.68-1.02 1.409-.142 2.59.087 3.223.877a.5.5 0 0 0 .78 0c.633-.79 1.814-1.019 3.222-.877 1.378.139 2.8.62 3.681 1.02A.5.5 0 0 0 16 13.5v-11a.5.5 0 0 0-.293-.455c-.952-.433-2.48-.952-3.994-1.105C10.413.809 8.985.936 8 1.783"/>
                                            </svg>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!--wishlist-->
            <div class="d-flex align-items-baseline justify-content-between p-2 m-2" v-else>
                <h4 class="w-100 text-center text-danger" v-if="datastore.cart.items.length==0">Sorry, Add books</h4>
                <table class="table table-bordered table-striped text-center" style="color: azure;" v-else>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Name</th>
                            <th>Price</th>
                            <th>Category</th>
                            <th>Isbn</th>
                            <th>Author</th>
                            <th>Pages</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in datastore.cart.items" :key="item.book.id" style="background-color: rgb(227, 179, 34);">
                            <td>{{item.book.id}}</td>
                            <td>{{item.book.name}}</td>
                            <td>{{item.book.price}}</td>
                            <td>{{item.book.category}}</td>
                            <td>{{item.book.isbn}}</td>
                            <td>{{item.book.author}}</td>
                            <td>{{item.book.pages}}</td>
                            <td><button class="btn btn-danger h5" @click="remove(item)">Remove</button></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>
    </div>
</template>

<script>
// import books from '../books';
import { usedatastore } from "@/stores/dataStorebooks";

export default {
    data: () => ({
        datastore: usedatastore(),
        iscartvisible: false
    }),
    methods: {
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
};
</script>


<style>
@import 'bootstrap/dist/css/bootstrap.css';
body{
    /* Created with https://www.css-gradient.com */
    background: #161616;
    }
 
    h1{
      color:#fff;
    }
    .lead{
      color:#aaa;
    }
    
    .wrapper{margin:10vh}
    /* //post card styles */
    
    .card{
      border: none;
      transition: all 500ms cubic-bezier(0.19, 1, 0.22, 1);
     overflow:hidden;
     border-radius:20px;
     min-height:450px;
       box-shadow: 0 0 12px 0 rgba(0,0,0,0.2);
    
     @media (max-width: 768px) {
      min-height:350px;
    }
    
    @media (max-width: 420px) {
      min-height:300px;
    }
    
     &.card-has-bg{
     transition: all 500ms cubic-bezier(0.19, 1, 0.22, 1);
      background-size:120%;
      background-repeat:no-repeat;
      background-position: center center;
      &:before {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        background: inherit;
        -webkit-filter: grayscale(1);
      -moz-filter: grayscale(100%);
      -ms-filter: grayscale(100%);
      -o-filter: grayscale(100%);
      filter: grayscale(100%);}
    
      &:hover {
        transform: scale(0.98);
         box-shadow: 0 0 5px -2px rgba(0,0,0,0.3);
        background-size:130%;
         transition: all 500ms cubic-bezier(0.19, 1, 0.22, 1);
    
        .card-img-overlay {
          transition: all 800ms cubic-bezier(0.19, 1, 0.22, 1);
          background: rgb(255,186,33);
         background: linear-gradient(0deg, rgba(255,186,33,0.5) 0%, rgba(255,186,33,1) 100%);
         }
      }
    }
     .card-footer{
      background: none;
       border-top: none;
        .media{
         img{
           border:solid 3px rgba(255,255,255,0.3);
         }
       }
     }
      .card-title{font-weight:800}
     .card-meta{color:rgba(0,0,0,0.3);
      text-transform:uppercase;
       font-weight:500;
       letter-spacing:2px;}
     .card-body{ 
       transition: all 500ms cubic-bezier(0.19, 1, 0.22, 1);
     
    
      }
     &:hover {
       .card-body{
         margin-top:30px;
         transition: all 800ms cubic-bezier(0.19, 1, 0.22, 1);
       }
     cursor: pointer;
     transition: all 800ms cubic-bezier(0.19, 1, 0.22, 1);
    }
  
     .card-img-overlay {
      transition: all 800ms cubic-bezier(0.19, 1, 0.22, 1);
     background: rgb(255,186,33);
    background: linear-gradient(0deg, rgba(255,186,33,0.3785889355742297) 0%, rgba(255,186,33,1) 100%);
    }
    }
    @media (max-width: 767px){
      
    }
</style>