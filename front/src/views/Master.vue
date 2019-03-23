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
                  <div class='column'><Plugin />
                  "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
                  </div>
                  <div class='column'><Plugin />
                  "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
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
  }
}
</script>

<style scoped>

</style>

