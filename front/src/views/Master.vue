<template>
  <div class="master">
    <section class="section">
      
        <div class='columns is-gapless'>
          <div class='column is-one-third'>
            <TrackList v-bind:sctracks="sctracks"/>
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
          ],
          sctracks:[{
            id:1,
            name: 'Girl i want/girl I need [rough]',
            url: 'https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/465705123&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true'
          },
          {
            id:2,
            name: "When you're near",
            url: 'https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/427416225&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true'
          },
          {
            id:3,
            name: 'Hardwell - Spaceman (Carnage Festival Trap Remix)',
            url: 'https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/59527799&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true'
          }
          ]
      }
  }
}
</script>

<style scoped>

</style>

