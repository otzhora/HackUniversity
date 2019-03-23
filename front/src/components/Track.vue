<template>
    <div class="track">
        <a class="panel-block is-active" >
            <span style="max-width:300px">{{track.title}}</span>
            <img class="right" src="https://img.icons8.com/material/24/000000/play.png" @click="play">
            <img class="right" src="https://img.icons8.com/material/24/000000/stop.png" @click="stop">
            <img class="right" src="https://img.icons8.com/material/24/000000/pause.png" @click="pause">
        </a>
    </div>
</template>

<script>
export default {
    name: "Track",
    props: ["track", "url"],
    methods: {
        play: function(){
            console.log(this.track)
            window.p1 = new window.Tone.Player(this.track.url, function() {
                window.p1.start();
            }).toMaster();
            
        },
        stop: function() {
            window.p1.stop()
        },
        pause: function() {
            window.p1.stop()
        }
    }
}
</script>

<style scoped>
.right {
    margin: 0 0 0 auto;
}
</style>