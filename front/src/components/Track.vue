<template>       

    <div class="track" :class="{ 'blue-border': isPlaying }" >
        <!--<img v-if="!track.local" src="https://img.icons8.com/windows/32/000000/soundcloud.png">-->
        <a class="panel-block is-active" >
            <div style="width:100px">
                <img class="right" src="https://img.icons8.com/material/24/000000/play.png" @click="play">
                <img class="right" src="https://img.icons8.com/material/24/000000/stop.png" @click="stop">
                <img class="right" src="https://img.icons8.com/material/24/000000/pause.png" @click="pause">
            </div>
            <span style="max-width:300px">{{track.title}}</span>
        </a>
        <div :id="'wave-' + componentid" v-show="isPlaying"></div>
    </div>

</template>


<script>

export default {
    name: "Track",
    props: ["track", "url"],

    data: function() {
        return {
            isPlaying: false,
            componentid: null,
            siriWavePlayer: null
        }
    },
        
    methods: {
        play: function(){

            if (this.isPlaying) return;

            this.isPlaying = true;

            window.currentTitle = this.track.title.toString()
            window.players[window.currentTitle] = new Tone.Player(this.track.url, function() {
                window.players[window.currentTitle].start();
            }).toMaster();

            if (this.siriWavePlayer == null) {
                this.siriWavePlayer = new SiriWave({
                    container: document.getElementById("wave-" + this.componentid),
                    color: '#3373dc'
                });
            } 

            this.siriWavePlayer.start();
        },
        stop: function() {

            if (this.isPlaying) {
                window.currentTitle = this.track.title.toString();
                window.players[window.currentTitle].stop();

                if (this.siriWavePlayer != null)
                    this.siriWavePlayer.stop();
            }

            this.isPlaying = false;
        },
        pause: function() {
            if (this.isPlaying) {
                window.currentTitle = this.track.title.toString()
                window.players[window.currentTitle].stop()

                if (this.siriWavePlayer != null)
                    this.siriWavePlayer.stop();
            }

            this.isPlaying = false;
        }
    },
    mounted () {
        this.componentid = this._uid
    }
}
</script>

<style scoped>
.right {
    margin: 0 0 0 auto;
}

.blue-border {
    border: 1px solid #3373dc !important;
}

#waveform:hover {
  opacity: 1;
}

</style>