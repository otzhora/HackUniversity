<template>
    <div class="playwindow">
        <!-- <img src="../assets/playwindow.png" alt=""> -->
        <h1 class="title is-1" contenteditable="true">{{masterTrackName}}</h1>
        <div class='columns'>
          <div class='column'>
            <img id="first_waveform" src="../assets/wave.png" alt="">
            <input id="first_waveform_range" type="range" v-model="first_value" @click="seek_first"></div>
          <div class='column'>
            <img id="second_waveform" src="../assets/wave.png" alt="">
            <input id="second_waveform_range" type="range" v-model="second_value" @click="seek_second">
        
          </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "PlayWindow",
    data: function() {
      return {
        first_value: 0,
        second_value: 0,
        masterTrackName: '{your awesome track}'
      }
    },
    methods: {
      seek_first: function() {
        if (window.players.length > 0) {
          var p = window.players[0];
          var d = p.buffer.duration * this.first_value / 100;
          p.seek(d);
        }
      },
      seek_second: function() {
        if (window.players.length > 1) {
          var p = window.players[1];
          var d = p.buffer.duration * this.second_value / 100;
          p.seek(d);
        }
      }
    }
}
</script>

<style scoped>
input[type=range] {
  height: 26px;
  -webkit-appearance: none;
  margin: 10px 0;
  width: 500px;
}
input[type=range]:focus {
  outline: none;
}
input[type=range]::-webkit-slider-runnable-track {
  width: 100%;
  height: 14px;
  cursor: pointer;
  animate: 0.2s;
  box-shadow: 1px 1px 1px #50555C;
  background: #50555C;
  border-radius: 14px;
  border: 0px solid #000000;
}
input[type=range]::-webkit-slider-thumb {
  box-shadow: 0px 0px 0px #000000;
  border: 0px solid #000000;
  height: 20px;
  width: 40px;
  border-radius: 12px;
  background: #529DE1;
  cursor: pointer;
  -webkit-appearance: none;
  margin-top: -3px;
}
input[type=range]:focus::-webkit-slider-runnable-track {
  background: #50555C;
}
input[type=range]::-moz-range-track {
  width: 100%;
  height: 14px;
  cursor: pointer;
  animate: 0.2s;
  box-shadow: 1px 1px 1px #50555C;
  background: #50555C;
  border-radius: 14px;
  border: 0px solid #000000;
}
input[type=range]::-moz-range-thumb {
  box-shadow: 0px 0px 0px #000000;
  border: 0px solid #000000;
  height: 20px;
  width: 40px;
  border-radius: 12px;
  background: #529DE1;
  cursor: pointer;
}
input[type=range]::-ms-track {
  width: 100%;
  height: 14px;
  cursor: pointer;
  animate: 0.2s;
  background: transparent;
  border-color: transparent;
  color: transparent;
}
input[type=range]::-ms-fill-lower {
  background: #50555C;
  border: 0px solid #000000;
  border-radius: 28px;
  box-shadow: 1px 1px 1px #50555C;
}
input[type=range]::-ms-fill-upper {
  background: #50555C;
  border: 0px solid #000000;
  border-radius: 28px;
  box-shadow: 1px 1px 1px #50555C;
}
input[type=range]::-ms-thumb {
  margin-top: 1px;
  box-shadow: 0px 0px 0px #000000;
  border: 0px solid #000000;
  height: 20px;
  width: 40px;
  border-radius: 12px;
  background: #529DE1;
  cursor: pointer;
}
input[type=range]:focus::-ms-fill-lower {
  background: #50555C;
}
input[type=range]:focus::-ms-fill-upper {
  background: #50555C;
}
</style>