import {createRouter,createWebHistory} from "vue-router"
import home  from "../components/views/HomeComponent.vue"
import books  from "../components/views/bookscomponent.vue"
import products  from "../components/views/shopcomponent.vue"
import catchAll  from "../components/views/catchAll.vue"
const routes=[
    {
     path:"/",
     component:home   
    },
    {
     path:"/books",
     component:books   
    },
    {
     path:"/products",
     component:products   
    },{
     path:"/:catchAll(.*)",
     component:catchAll   
    },
]
const router=createRouter({
routes:routes,
history:createWebHistory()
});
export default router