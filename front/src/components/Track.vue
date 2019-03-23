<template>
    <div class="track">
        <a class="panel-block is-active" >
            <div style="width:100px">
                <img class="right" src="https://img.icons8.com/material/24/000000/play.png" @click="play">
                <img class="right" src="https://img.icons8.com/material/24/000000/stop.png" @click="stop">
                <img class="right" src="https://img.icons8.com/material/24/000000/pause.png" @click="pause">
            </div>
            <span style="max-width:300px">{{track.title}}</span>
        </a>
    </div>
</template>

<script>
export default {
    name: "Track",
    props: ["track", "url"],
    methods: {
        play: function(){
            window.currentTitle = this.track.title.toString()
            window.players[window.currentTitle] = new Tone.Player(this.track.url, function() {
                window.players[window.currentTitle].start();
            }).toMaster()
        },
        stop: function() {
            window.currentTitle = this.track.title.toString()
            window.players[window.currentTitle].stop()
        },
        pause: function() {
            window.currentTitle = this.track.title.toString()
            window.players[window.currentTitle].stop()
        }
    }
}
</script>

<style scoped>
.right {
    margin: 0 0 0 auto;
}
</style>