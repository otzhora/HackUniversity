<template>
    <div class="track" :class="{ 'blue-border': isPlaying }">
        <img v-if="!track.local" src="https://img.icons8.com/windows/32/000000/soundcloud.png">
        <a class="panel-block is-active" @click="sendToPlayer">
            {{track.title}}
            <img class="right" src="https://img.icons8.com/material/24/000000/play.png">
        </a>
        <a class="panel-block is-active" @click="stopToPlayer">
            <img class="right" src="https://img.icons8.com/material/24/000000/stop.png">
        </a>
        <div :id="'wave-' + componentid" v-show="isPlaying"></div>
    </div>
</template>

<script>

export default {
    name: "Track",
    props: ["track"],
    data: function() {
        return {
            isPlaying: false,
            componentid: null,
            siriWavePlayer: null
        }
    },
    methods: {
        sendToPlayer: function(){
            // alert(this.track.title + " sent to player")

            if (this.isPlaying) return;

            this.isPlaying = true;
            window.p1 = new window.Tone.Player("http://localhost:5000/audio/uploads/83f46255-2822-43f7-ac0e-5582f31b68ad", function() {
                window.p1.start();
            }).toMaster();

            if (this.siriWavePlayer == null) {
                this.siriWavePlayer = new SiriWave({
                    container: document.getElementById("wave-" + this.componentid),
                    color: '#3373dc'
                });
            } 

            this.siriWavePlayer.start();           
        },
        stopToPlayer: function() {

            if (this.isPlaying) {
                
                
                window.p1.stop();

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