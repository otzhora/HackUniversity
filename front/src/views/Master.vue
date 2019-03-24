<template>
  <div class="master">
    <section class="section">
      
        <div class='columns is-gapless'>
          <div class='column is-one-third'>
            <TrackList/>
          </div>
          <div class='column'>
            <PlayWindow />
            <div class='columns'>
              
              <div class="column">
                <div class='columns'>
                  <div class='column' >
                    <div class='columns' id='cp1'>
                      <div class='column'><Plugin v-bind:id="1"/></div>
                      <div class='column'><Plugin v-bind:id="2"/></div>
                      <div class='column'><Plugin v-bind:id="3"/></div>
                      <div class='column'><Plugin v-bind:id="4"/></div>
                      
                    </div>
                    <!-- Каждую крутилку добавляем вручную и назначаем ей ID в соответствии с функционалом-->
                    
                  </div>
                  <div class='column' id='cp2'></div>
                  <div class='column' >
                    
                    <div class='columns'>
                      <div class='column'><Plugin v-bind:id="5"/></div>
                      <div class='column'><Plugin v-bind:id="6"/></div>
                      <div class='column'><Plugin v-bind:id="7"/></div>
                      <div class='column'><Plugin v-bind:id="8"/></div>
                    </div>
                    
                  </div>
                </div>
              </div>
            </div>
            
          </div>
        </div>
      
    </section>
    
    
  </div>
</template>

<script>
import TrackList from '../components/TrackList'
import PlayWindow from '../components/PlayWindow'
import Plugin from '../components/Plugin'

// require( 'tone' )(); Not works for me

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

    let waveformScriptTag = document.createElement('script');
        //waveformScriptTag.src = "https://unpkg.com/siriwave/dist/siriwave.js";
        waveformScriptTag.src = "https://howlerjs.com/assets/howler.js/examples/player/siriwave.js";
        document.head.appendChild(waveformScriptTag);
  }
}
</script>

<style scoped>
  background-image: url(/logo1.jpg);
</style>

