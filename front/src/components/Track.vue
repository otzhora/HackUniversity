<template>       

    <div class="track media panel-block is-active" :class="{ 'blue-border': isPlaying }" >
        <figure class="media-left">
            <div style="width:100px">
                <img v-if="isPlaying" :src="'https://img.icons8.com/ios/64/000000/pause.png'" @click="stop">
                <img v-else :src="'https://img.icons8.com/ios/64/000000/play.png'" @click="play">
            </div>
            <div class="tags has-addons">
                <span class="tag"><img src="https://img.icons8.com/ios/16/000000/bit-rate-filled.png"></span>
                <span class="tag is-info">{{track.bpm}}</span>
            </div>
        </figure>
        
        <div class="media-content">
            <div class="content">
                <span>
                    <strong v-show="isPlaying">{{track.title}}</strong> <small> @ateam</small>
                    <br>
                    <span v-show="!isPlaying">{{track.title}}</span>
                    <div>
                        <div :id="'wave-' + componentid" v-show="isPlaying"></div>
                    </div>
                </span>
            </div>          
        </div>

        <div class="media-right">
            <p class="is-small">{{track.bpm}}</p>
        </div>
        <!--<img v-if="!track.local" src="https://img.icons8.com/windows/32/000000/soundcloud.png">-->   
    </div>

</template>


<script>

export default {
    name: "Track",
    props: ["track", "url", "img"],

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

            window.player = this.player = new Tone.Player(this.track.url, function() {
                window.player.start();
            }).toMaster();

            window.players.push(window.player); //todo

            if (window.players.length == 1) {
                var w1 = document.getElementById("first_waveform");
                var w1_range = document.getElementById("first_waveform_range");
                w1.src = this.track.img;
                window.player.context._ticker._worker.onmessage = function() { 
                    const [p] = window.players;
                    var pos = p.position / p.buffer.duration * 100;
                    w1_range.value = pos;
                }
            } else if (window.players.length == 2) {
                var w2 = document.getElementById("second_waveform");
                var w2_range = document.getElementById("second_waveform_range");
                w2.src = this.track.img;
                window.player.context._ticker._worker.onmessage = function() { 
                    const [_, p] = window.players;
                    var pos = p.position / p.buffer.duration * 100;
                    w2_range.value = pos;
                }
            }

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
                this.player.stop();
                this.player.context._ticker._worker.onmessage=null
                
                window.players.pop(this.player);

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