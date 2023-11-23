<script lang="ts">
import {getFullAnimeNames, getAnimeInfoByID, getFullAnimeImages} from "@/services/anime/anime.service";

export default {
  props: {
    animeID: {
      required: true,
      type: Number,
    },
    containerID:{
      required: true,
      type: Number,
    }
  },
  data() {
    return {
      image: "images/noimage.png",
      selectedAnime: -1,
      animeList: [],
    }
  },
  methods:{
    loadOptions(){
      getFullAnimeNames().then((response: any)=>{
        let temporary = [];
        for (let id = 0; id < response.length; id++){
          temporary.push({name: response[id], code: id})
        }
        this.animeList = temporary;
      })
    }
  },
  created(){
    this.loadOptions();
    if(this.animeID !== -1){
      this.selectedAnime = this.animeID
      getAnimeInfoByID(this.selectedAnime).then((response)=>{
        this.image = response.image;
      })
    }
  },
  watch: {
    selectedAnime: {
      handler(newImageID, viejo){
        this.$emit("selected", this.containerID, newImageID)
        getAnimeInfoByID(this.selectedAnime).then((response)=>{
          this.image = response.image;
          if(this.image === undefined){
            getFullAnimeImages().then((response)=>{
              this.image = response[this.animeID];
            })
          }
        }).catch((e)=>{
          getFullAnimeImages().then((response)=>{
            this.image = response[this.animeID];
          })
        })
      }
    }
  }
}
</script>

<template>
  <div class="align-center flex-col">
    <pv-image :src="image" class="min-width" @click="$emit('selectByImage', containerID)"/>
    <pv-dropdown v-model="selectedAnime" :options="animeList" option-label="name" option-value="code" placeholder="¡Elige un Anime!" class="min-width"/>
  </div>
</template>

<style>
.p-dropdown-item{
  white-space: nowrap;
  overflow: hidden;
  width: 18rem;
}
.min-width img{
  object-fit: cover;
  height: 31rem;
  border-radius: 1rem;
}
</style>