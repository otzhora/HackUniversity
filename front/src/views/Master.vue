<template>
  <div class="master">
    <TrackList />
    <PlayWindow />
    <Plugin />
    <Plugin />
    <h1>This is a master page</h1>
  </div>
</template>

<script>
import TrackList from '../components/TrackList'
import PlayWindow from '../components/PlayWindow'
import Plugin from '../components/Plugin'

// require( 'tone' )(); Not work for me

export default {
  name: 'Master',
  components: {
    TrackList,
    PlayWindow,
    Plugin
  },
  mounted() {
    if (document.getElementById('main')) return; // was already loaded
    var scriptTag = document.createElement("script");
    scriptTag.src = "https://cdnjs.cloudflare.com/ajax/libs/tone/13.0.1/Tone.min.js";
    scriptTag.id = "main";
    document.getElementsByTagName('head')[0].appendChild(scriptTag);
  }
}
</script>

<style scoped>

</style>

