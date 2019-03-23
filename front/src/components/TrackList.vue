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
            <p class="panel-tabs">
                <a class="is-active">Soundcloud</a>
                <a>Local</a>
            </p>
            <div v-bind:key="track.id"
                v-for="track in sctracks">
                <Track v-bind:track="track"/>
            </div>
        </nav>
        
        

    </div>
</template>

<script>
import Track from './Track'
export default {
    name: "TrackList",
    props:["sctracks"],
    components: {
        Track
    }
}
</script>

<style scoped>

</style>
