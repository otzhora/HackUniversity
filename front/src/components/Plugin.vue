<template>
    <div class="plugin">
        <div class="knobBG">
            <div class="knob" v-bind:id="id">
            </div>
        </div>
    </div>
</template>

<script>
import Draggable from 'gsap/Draggable'
export default {
    name: "Plugin",
    props: ["id"],
    mounted(){
        
        Draggable.create(".knob", {
            type: "rotation",
            bounds:{minRotation:-180, maxRotation:180}, 
            throwProps: true,
            liveSnap:{
                
                rotation: function(value) {
                     //If you want to get id of knob, use this._eventTarget.id
                    if (this._eventTarget.id === "1" && window.players.length > 0) {
                      const [p1] = window.players;
                      p1.volume.value = value / 10;
                    } else if (this._eventTarget.id === "2" && window.players.length > 0) {
                      const [p1] = window.players;
                      p1.playbackRate = 1 + value / 180;
                    }
                    else if (this._eventTarget.id === "5" && window.players.length > 1) {
                      const [_, p2] = window.players;
                      p2.volume.value = value / 10;
                    }
                    else if (this._eventTarget.id === "6" && window.players.length > 1) {
                      const [_, p2] = window.players;
                      p2.playbackRate = 1 + value / 180;
                    }
                    return Math.round(value / 10) * 10; 
                }
            },
            
        })
        
    }
}
</script>

<style scoped>
.knobBG, .knob {
  background-image: url('https://s3-us-west-2.amazonaws.com/s.cdpn.io/16327/knob_Base.png');
  background-size: 100px 100px;
  width:100px; 
  height:100px;
}
.knob{
  background-image: url('https://s3-us-west-2.amazonaws.com/s.cdpn.io/16327/knob_Spinner.png');
  z-index: 1;

}

</style>