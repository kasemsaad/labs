
<template>
  
  <div class="container">
    <div class="row g-0 my-2 ">
  <!-- <ul class="nav bg-warning justify-content-evenly align-items-baseline">
    <li class="nav-item"><a class="nav-link font-weight-bold text-black rounded" href="#" @click.prevent="targetcomponent='home'">Home</a></li>
    <li class="nav-item"><a class="nav-link font-weight-bold text-black rounded" href="#" @click.prevent="targetcomponent='books'">Books</a></li>
    <li class="nav-item"><a class="nav-link font-weight-bold text-black rounded" href="#" @click.prevent="targetcomponent='products'">Shop</a></li>
  </ul> -->
  <ul class="nav bg-warning justify-content-evenly align-items-baseline">
    <li class="nav-item"><RouterLink to="/">Home</RouterLink></li>
    <li class="nav-item"><RouterLink to="/books">Books</RouterLink></li>
    <li class="nav-item"><RouterLink to="/products">shop</RouterLink></li>
  </ul>
</div>
    <div class="row g-0 my-2">
      <h4 class="text-center text-danger col-12">Dynamic Component</h4>
      <router-view></router-view>

      <!-- <component :is="targetcomponent"/> -->
    
    </div>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import home from './components/views/HomeComponent.vue';
import books from './components/views/bookscomponent.vue';
import products from './components/views/shopcomponent.vue';

export default {
  data() {
    return {
        targetcomponent: "home"
    };
},
  components: {
  home,
  books,
  products,
  }

}
</script>

<style>
.nav {
  border-radius: 10px;
  font-size: larger;
}
</style>
