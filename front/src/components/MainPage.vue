<template>
  <section class="hero is-light is-bold is-medium">
    <div class="hero-body" v-if="masterTrack != null">
      <div class="container">
        <h1 class="title">
          {{masterTrack.title}}
        </h1>
        <h2 class="subtitle">
          by /{{masterTrack.author}}/
        </h2>
      </div>
    </div>
    
    <div id="waveform"></div>

    <div>
      <a class="button is-normal is-primary is-outlined is-rounded :disabled=" @click="playPause">
        {{ isPlaying ? 'Pause' : 'Play' }}
      </a>
    </div>
    
  </section>
</template>

<script>

import TracksService from '@/services/TracksService';
require('../../dist/wavesurfer.js');
require('../../dist/plugin/wavesurfer.cursor.js');

export default {
  name: 'MainPage',

  data() {
      return {
          masterTrack: null,
          ready: false,
          isPlaying: false,
          wavesurfer: null
      }
  },

  async created() {
      this.masterTrack = await TracksService.getMasterTrack();
  },

  methods: {
    playPause: function() {
      if (this.wavesurfer == null) {
        this.wavesurfer = window.WaveSurfer.create({
          container : '#waveform',
          cursorColor: 'hsl(171, 100%, 41%)',
          plugins: [
            window.WaveSurfer.cursor.create({
                showTime: true,
                opacity: 1,
                customShowTimeStyle: {
                    color: '#fff',
                    padding: '2px',
                    'font-size': '10px'
                }
            })
          ]
        });

        window.wavesurfer = this.wavesurfer;
      }

      this.wavesurfer.on('ready', function () {
        window.wavesurfer.playPause();
      });

      this.wavesurfer.load(this.masterTrack.url);
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
