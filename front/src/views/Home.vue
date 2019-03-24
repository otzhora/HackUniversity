<template>
  <div class="home">
    <MainPage />
  </div>
</template>

<script>
// @ is an alias to /src
import MainPage from '@/components/MainPage.vue'

export default {
  name: 'Home',
  components: {
    MainPage
  },

  mounted() {

    let waveformScriptTag = document.createElement('script');
        //waveformScriptTag.src = "https://unpkg.com/siriwave/dist/siriwave.js";
        waveformScriptTag.src = "../../dist/wavesurfer.js";
        document.head.appendChild(waveformScriptTag);
  }
}
</script>

<style scoped>

</style>


