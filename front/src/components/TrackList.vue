<template>
    <div class="tracklist">
        This is tracklist
        <div v-bind:key="track.id"
        v-for="track in tracks">
            <Track v-bind:track="track"/>
        </div>
        

    </div>
</template>

<script>
import Track from './Track'
export default {
    name: "TrackList",
    props:["tracks"],
    components: {
        Track
    }
}
</script>

<style scoped>

</style>
