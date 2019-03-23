<template>
    <div class="track">
        <a class="panel-block is-active" @click="sendToPlayer">
                
                
            {{track.name}}
        
        
            <img class="right" src="https://img.icons8.com/material/24/000000/play.png">
                    
                
                
                
        </a>
    </div>
</template>

<script>
export default {
    name: "Track",
    props: ["track"],
    methods: {
        sendToPlayer: function(){
            alert(this.track.name + "sent to player")
        }
    }
}
</script>

<style scoped>
.right {
    margin: 0 0 0 auto;
}
</style>