<template>
  <div class="master">
    <Header />
    <TrackList />
    <PlayWindow />
    <h1>This is a master page</h1>
  </div>
</template>

<script>
import Header from '../components/Header'
import TrackList from '../components/TrackList'
import PlayWindow from '../components/PlayWindow'
export default {
  name: 'Master',
  components: {
    Header,
    TrackList,
    PlayWindow
  }
}
</script>

<style scoped>

</style>

