<template>
    <div class="track">
        <img v-if="!track.local" src="https://img.icons8.com/windows/32/000000/soundcloud.png">
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
    props: ["track"],
    methods: {
        sendToPlayer: function(){
            // alert(this.track.title + " sent to player")
            window.p1 = new window.Tone.Player("http://localhost:5000/audio/uploads/83f46255-2822-43f7-ac0e-5582f31b68ad", function() {
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