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
            sliveSnap:{
                
                rotation: function(value) {
                     //If you want to get id of knob, use this._eventTarget.id
                    console.log(value, this._eventTarget.id)
                    // if (window.currentTitle) {
                    //   window.players[window.currentTitle].volume.value = value / 10;
                    // }
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