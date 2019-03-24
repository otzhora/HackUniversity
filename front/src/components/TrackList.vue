<template>
    <div class="tracklist">
        <nav class="panel">
            <p class="panel-heading">
                Songs
            </p>
            <div class="panel-block">
                <p class="control has-icons-left">
                <input class="input is-small" type="text" placeholder="search">
                <span class="icon is-small is-left">
                    <i class="fas fa-search" aria-hidden="true"></i>
                </span>
                </p>
            </div>
            
            <div v-bind:key="track.id"
                v-for="track in tracks">
                <Track v-bind:track="track" v-bind:url="track.url"/>
            </div>
        </nav>
        <button @click="megre_first_two"> 
            merge first two 
        </button>
    </div>
</template>

<script>
import TracksService from '@/services/TracksService';
import Track from './Track.vue';
import axios from 'axios';

export default {
    name: "TrackList",
    components: {
        Track
    },

    data() {
        return {
            loading: false,
            tracks: []
        }
    },

    async created() {
        window.players = []
        this.tracks = await TracksService.getTracksList();
        this.loading = false;
    }, 

    methods: {
         megre_first_two: async function() {
             let url = 'http://193.124.206.179:5000/concat/'
             await axios.post(url, {
                 'ids': [this.tracks[0]['id'], this.tracks[1]['id']]
             })
        }
    },
}
</script>

<style scoped>
</style>
