<template>
    <div class="track">
        <a class="panel-block is-active" @click="sendToPlayer">
            {{track.title}}
            <img class="right" src="https://img.icons8.com/material/24/000000/play.png">
        </a>
        <a class="panel-block is-active" @click="stopToPlayer">
            <img class="right" src="https://img.icons8.com/material/24/000000/stop.png">
        </a>
    </div>
</template>

<script>
export default {
    name: "Track",
    props: ["track", "url"],
    methods: {
        sendToPlayer: function(){
            // alert(this.track.title + " sent to player")
            window.p1 = new window.Tone.Player(this.url, function() {
                window.p1.start();
            }).toMaster();
            
        },
        stopToPlayer: function() {
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