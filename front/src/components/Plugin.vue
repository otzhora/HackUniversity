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
        let knob = document.querySelector('.knob')
        console.log(knob)
        Draggable.create(".knob", {type: "rotation", throwProps: true});
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