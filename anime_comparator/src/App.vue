<script>
import { RouterLink, RouterView } from 'vue-router'
import "primevue/resources/themes/lara-dark-purple/theme.css"
import {setOuterContainerID, setOuterIDs, getOuterContainerID,getOuterIDs} from "@/services/cache/test"
export default {
  components: {RouterView, RouterLink},
  data(){
    return{
      ids: [-1, -1],
      containerID: 1,
    }
  },
  methods: {
    updateID(contenedor, nuevo_id){
      this.ids[contenedor-1] = nuevo_id
      setOuterIDs(this.ids)
    },
    selectedByPicker(animeID){
      this.ids[this.containerID-1] = animeID
      setOuterIDs(this.ids)
      this.$router.push("/home");
    },
    goToPicker(containerID){
      this.containerID = containerID;
      setOuterContainerID(containerID);
      this.$router.push("/picker");
    }
  },
  created(){
    this.ids = getOuterIDs();
    this.containerID = getOuterContainerID();
  }
}
</script>

<template>
  <div class="flex-col gap margin-10 align-center">
    <div class="align-center">
      <div class="title">
        Similanime
      </div>
      Un sitio que te dirá que tan probable es que te guste un anime si otro te gusto anteriormente.
      <br>
      Modo de uso: Selecciona un anime que hallas visto anteriormente en el recuadro de la izquierda.
      <br>
      luego, selecciona un anime que quieras ver a la derecha. El número del centro reflejará que tan
      <br>
      probable es que te guste el anime de la izquierda si te gustó el ánime de la derecha.
    </div>
    <div class="align-center">
      <RouterView
          @update="updateID"
          @selectByImage="goToPicker"
          @selected="selectedByPicker"
          :anime1id="ids[0]"
          :anime2id="ids[1]"
      />
    </div>
  </div>
</template>
<style></style>