<script lang="ts">
import {getFullAnimeNames, getFullAnimeImages} from "@/services/anime/anime.service";
export default {
  data(){
    return{
      animeData: [],
      loadedAnimeData: [],
      toLoad: 10,
    }
  },
  methods:{
    loadMore(){
      let limit = this.toLoad + this.loadedAnimeData.length
      if(limit > this.animeData.length) limit = this.animeData.length;
      for(let i = this.loadedAnimeData.length; i < limit; i++){
        this.loadedAnimeData.push(this.animeData[i]);
      }
    },
    select(id: number){
      this.$emit("selected", id)
    },
  },
  created() {
    getFullAnimeImages().then((imageList)=>{
      getFullAnimeNames().then((nameList)=>{
        if(imageList.length == nameList.length){
          for(let i = 0; i < imageList.length; i++){
            this.animeData.push({  name: nameList[i], image: imageList[i], id: i  })
          }
          for(let i = 0; i < this.toLoad && i < this.animeData.length; i++){
            this.loadedAnimeData.push(this.animeData[i]);
          }
        }
      })
    })

  }
}
</script>

<template>
  <div v-if="loadedAnimeData.length > 0">
    <div class="flex-auto picker-container">
      <div v-for="data in loadedAnimeData" :key="data.id" @click="select(data.id)" class="picker-item">
        <pv-image :src="data.image" class="picker-img"/>
        <div class="picker-text-container">
          {{data.name}}
        </div>
      </div>
    </div>
    <div class="margin-10">
      <pv-button @click="loadMore" :disabled="loadedAnimeData.length === animeData.length" label="Cargar más"/>
    </div>
  </div>
  <div v-else class="margin-10">
    Cargando datos...
  </div>

</template>

<style>
.picker-img,
.picker-img img{
  width: 10rem;
  height: 16rem;
  object-fit: cover;
}
.picker-container{
  horiz-align: center;
  overflow: hidden;
  justify-content: center;
}
.picker-item{
  max-width: 11rem;
  width: 11rem;
}
.picker-text-container{

}
</style>