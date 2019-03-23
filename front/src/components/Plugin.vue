<template>
    <div class="plugin" id='p1'>
        <div class="knobBG">
            <div class="knob">
            </div>
        </div>
        
    </div>
</template>

<script>
import Draggable from 'gsap/Draggable'
export default {
    name: "Plugin",
    mounted(){
        
        Draggable.create(".knob", {
            type: "rotation",
            bounds:{minRotation:-180, maxRotation:180}, 
            throwProps: true,
            liveSnap:{
                rotation: function(value) {
                    if (window.currentTitle) {
                      window.players[window.currentTitle].volume.value = value / 10;
                    }
                    return Math.round(value / 10) * 10; 
                }
            },
            
        })
        
    },
    methods: {

    }
}
</script>

<style scoped>
.knobBG, .knob {
  position:absolute;
  background-image: url('https://s3-us-west-2.amazonaws.com/s.cdpn.io/16327/knob_Base.png');
  width:355px; 
  height:355px;
}
.knob{
  background-image: url('https://s3-us-west-2.amazonaws.com/s.cdpn.io/16327/knob_Spinner.png');
  z-index: 1;

}
</style>