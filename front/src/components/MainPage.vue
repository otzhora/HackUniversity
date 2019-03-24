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
/*import WaveSurfer from 'wavesurfer.js';*/
/*import WaveSurfer from '../../dist/wavesurfer.js';*/
require('../../dist/wavesurfer.js');
require('../../dist/plugin/wavesurfer.cursor.js');
//import wavesurfer from "wavesurfer.js";

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

  created() {
      // console.log(window.WaveSurfer);

      // this.wavesurfer = wavesurfer.create({
      //   container: '#waveform',
      //   plugins: [
      //     wavesurfer.cursor.create({
      //         showTime: true,
      //         opacity: 1,
      //         customShowTimeStyle: {
      //             color: '#fff',
      //             padding: '2px',
      //             'font-size': '10px'
      //         }
      //     })
      //   ]
      // });

      // this.wavesurfer.on('ready', function () {
      //   this.ready = true;
      // });
    
      this.masterTrack = /*await*/ TracksService.getMasterTrack();
      // this.wavesurfer.load(this.masterTrack.url);

  },

  methods: {
    playPause: function() {

      console.log('init play');

      if (this.wavesurfer == null) {
        this.wavesurfer = window.WaveSurfer.create({
          container : '#waveform',
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

      console.log('created');
      console.log('this.wavesurfer: ' + this.wavesurfer);

      this.wavesurfer.on('ready', function () {
        console.log('onready');

        //this.ready = true;

        window.wavesurfer.playPause();
        //window.isPlaying = win.wavesurfer.isPlaying();

      });

      console.log('before play');

      this.wavesurfer.load(this.masterTrack.url);

      console.log('after play');
      
      
      /*this.wavesurfer.playPause();
      this.isPlaying = this.wavesurfer.isPlaying();*/

      /*

      this.wavesurfer.on('ready', function () {
        ready = true;

      });*/
    
    /*
      this.wavesurfer.load(this.masterTrack.url);


      this.wavesurfer.playPause();
      this.isPlaying = this.wavesurfer.isPlaying();

      */
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
