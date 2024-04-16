<template>

  <h3 class="d">Home {{datastore.count}}</h3>
  <img src="./kasem1-01.png" width="100" height="80%">
  
</template>
<script>
import {usedatastore} from "@/stores/dataStore"
export default {
data:()=>({
  datastore:usedatastore()
})
}
</script>

<style>
.d{
  color: azure;
}
</style>