<script lang="ts">
import animeComponent from "@/components/anime/anime.component.vue";
import {compareTwoAnimes} from "@/services/anime/anime.service";

export default {
  name: 'comparatorComponent',
  components: {animeComponent},
  props: {
    anime1id: {
      required: true,
      default: -1,
      type: Number
    },
    anime2id: {
      required: true,
      default: -1,
      type: Number
    },
  },
  data(){
    return {
      similitude: 0,
    }
  },
  methods:{
    updateSimilitude(){
      console.log(this.anime1id, this.anime2id)
      if(this.anime1id !== -1 && this.anime2id !== -1){
        compareTwoAnimes(this.anime1id, this.anime2id).then((response)=>{
          this.similitude = response;
        })
      }
    },
    changeAnime(container: number, newID: number){
      this.$emit("update", container, newID)
    },
    selectByImage(containter: number){
      this.$emit('selectByImage', containter)
    }
  },
  watch: {
    anime1id:{
      handler(nuevo, antiguo){
        this.updateSimilitude()
      }
    },
    anime2id:{
      handler(nuevo, antiguo){
        this.updateSimilitude()
      }
    }
  },
  created(){
    this.updateSimilitude()
  }
}
</script>

<template>
  <div class="comparator-container align-justify gap align-center">
    <animeComponent :animeID="anime1id" @selected="changeAnime" @selectByImage="selectByImage" :containerID="1"/>
    <pv-knob v-model="similitude" readonly valueTemplate="{value}%"/>
    <animeComponent :animeID="anime2id" @selected="changeAnime" @selectByImage="selectByImage" :containerID="2"/>
  </div>
</template>

<style>
@media (min-width: 1100px) {
  .comparator-container{
    display: flex;
    flex-direction: row;
  }
}
@media (max-width: 1099px) {
  .comparator-container{
    display: flex;
    flex-direction: column;
  }
}
</style>