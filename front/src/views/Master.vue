<template>
  <div class="master">
    <section class="section">
      
        <div class='columns is-gapless'>
          <div class='column is-one-third'>
            <TrackList v-bind:tracks="tracks"/>
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
export default {
  name: 'Master',
  components: {
    TrackList,
    PlayWindow,
    Plugin
  },
  data(){
      return {
          tracks: [
              {
                  id: 1,
                  text: 'Track1'
              },
              {
                id:2,
                text: 'Track2'
              }
          ]
      }
  }
}
</script>

<style scoped>

</style>

