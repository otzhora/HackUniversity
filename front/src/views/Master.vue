<template>
  <div class="master">
    <TrackList />
    <PlayWindow />
    <Plugin />
    <Plugin />
    <h1>This is a master page</h1>
  </div>
</template>

<script>
import TrackList from '../components/TrackList'
import PlayWindow from '../components/PlayWindow'
import Plugin from '../components/Plugin'
export default {
  name: 'Master',
  components: {
    TrackList,
    PlayWindow,
    Plugin
  }
}
</script>

<style scoped>

</style>

