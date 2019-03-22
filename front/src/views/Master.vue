<template>
  <div class="master">
    <Header />
    <TrackList />
    <PlayWindow />
    <Plugin />
    <Plugin />
    <h1>This is a master page</h1>
  </div>
</template>

<script>
import Header from '../components/Header'
import TrackList from '../components/TrackList'
import PlayWindow from '../components/PlayWindow'
import Plugin from '../components/Plugin'
export default {
  name: 'Master',
  components: {
    Header,
    TrackList,
    PlayWindow,
    Plugin
  }
}
</script>

<style scoped>

</style>

