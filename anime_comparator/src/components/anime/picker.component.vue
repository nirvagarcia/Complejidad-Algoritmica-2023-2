<script lang="ts">
import {getFullAnimeNames, getFullAnimeImages} from "@/services/anime/anime.service";
export default {
  data(){
    return{
      animeData: [],
      filteredAnimeData: [],
      loadedAnimeData: [],
      toLoad: 20,
      textFilter: "",
    }
  },
  methods:{
    loadMore(){
      let limit = this.toLoad + this.loadedAnimeData.length
      if(limit > this.filteredAnimeData.length) limit = this.filteredAnimeData.length;
      for(let i = this.loadedAnimeData.length; i < limit; i++){
        this.loadedAnimeData.push(this.filteredAnimeData[i]);
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
          this.filteredAnimeData = this.animeData
          for(let i = 0; i < this.toLoad && i < this.animeData.length; i++){
            this.loadedAnimeData.push(this.animeData[i]);
          }
        }
      })
    })
  },
  watch: {
    textFilter(newValue, oldValue) {
      this.filteredAnimeData = this.animeData.filter(anime => anime.name.toLowerCase().includes(newValue.toLowerCase())).slice(0, this.toLoad);
      this.loadedAnimeData = [];
      this.loadMore()
    }
  }
}
</script>

<template>
  <div v-if="loadedAnimeData.length > 0">
    <div class="flex-col align-center margin-10">
      <div>Busca tus animes por nombre:</div>
      <div><pv-input v-model="textFilter"/></div>

    </div>
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