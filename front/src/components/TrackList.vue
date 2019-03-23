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
import TracksService from '@/services/TracksService';
import Track from './Track.vue';

export default {
    name: "TrackList",
    props:["tracks"],
    components: {
        Track
    },

    data() {
        return {
            loading: false
        }
    },

    created() {
        this.tracks = TracksService.getTracksList();
        this.loading = false;
    }
}
</script>

<style scoped>
</style>
