<script lang="ts">
import {getFullAnimeNames, getFullAnimeImages, getAnimeGenresList, getAnimeFullDataList} from "@/services/anime/anime.service";
export default {
  data(){
    return{
      animeData: [],
      filteredAnimeData: [],
      loadedAnimeData: [],
      genres: [],
      toLoad: 100,
      textFilter: "",
      genreFilter: "",
      notFound: false,
      notFoundByGenre: false,
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
    updateFilters(){
      this.notFound = false;
      this.notFoundByGenre = false;
      this.filteredAnimeData = this.animeData
          .filter(anime => anime.name.toLowerCase().includes(this.textFilter.toLowerCase()));
      if(this.filteredAnimeData.length == 0) {
        this.filteredAnimeData = this.animeData;
        this.notFound = true;
      }
      console.log(this.filteredAnimeData[0])
      if(this.genreFilter){
        this.filteredAnimeData = this.filteredAnimeData
            .filter(anime => anime.genres.includes(this.genreFilter));
      }
      if(this.filteredAnimeData.length == 0) {
        this.filteredAnimeData = this.animeData;
        this.notFoundByGenre = true;
      }
      this.loadedAnimeData = [];
      this.loadMore()
    }
  },
  created() {
    getAnimeGenresList().then((genres)=>{
      this.genres = genres;
    })
    getAnimeFullDataList().then((response)=>{
      this.animeData = []
      for(let i = 0; i < response.length; i++){
        this.animeData.push({  name: response[i].name, image: response[i].image, id: i, genres: response[i].genres  })
      }
      this.filteredAnimeData = this.animeData
      this.loadMore()
      console.log(this.animeData)
    })
  },
  watch: {
    textFilter(newValue) {
      this.updateFilters();
    },
    genreFilter(newValue){
      this.updateFilters();
    }
  }
}
</script>

<template>
  <div v-if="loadedAnimeData.length > 0">
    <div class="margin-1">
      <div class="flex-row align-center flex-center margin-1 gap">
        <div class="flex-col align-center margin-1">
          <div>Busca tus animes por nombre:</div>
          <div><pv-input v-model="textFilter" :class="notFound?'p-invalid min-width':'min-width'"/></div>
        </div>
        <div class="flex-col align-center margin-1">
          <div>Busca tus animes por genero:</div>
          <div><pv-dropdown v-model="genreFilter" :options="genres" :class="notFoundByGenre?'p-invalid min-width':'min-width'"/></div>
        </div>
      </div>
      <div v-if="notFound" class="margin-1">No se ha encontrado ningun anime con el nombre {{textFilter}}</div>
      <div v-else-if="notFoundByGenre" class="margin-1">No se ha encontrado ningun anime con el genero {{genreFilter}} con el nombre {{textFilter}}</div>
    </div>
    <div class="flex-auto picker-container">
      <div v-for="data in loadedAnimeData" :key="data.id" @click="select(data.id)" class="picker-item">
        <pv-image :src="data.image" class="picker-img"/>
        <div class="picker-text-container">
          {{data.name}}
        </div>
      </div>
    </div>
    <div class="margin-10" v-if="loadedAnimeData.length !== filteredAnimeData.length">
      <pv-button @click="loadMore" :disabled="loadedAnimeData.length === filteredAnimeData.length" label="Cargar más"/>
    </div>
    <div class="margin-10" v-else-if="!notFound">
      No se han encontrado más animes
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
  object-fit: fill;
  border-radius: 1rem;
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
.flex-center{
  align-items: center;
  align-content: center;
  justify-content: center;
}
</style>