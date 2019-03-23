/* Manage tracks */
import axios from 'axios';

export default {
    async getTracksList() {
        let tracks = [ ];
        
        let url = 'http://193.124.206.179:5000/audio/uploads'
        let res = await axios.get(url)
        res = res.data
        for(let key in res) {
          tracks.push({
            id:key,
            title:res[key]['title'],
            url: url + '/' + key
          });
        }
        return tracks;
    },

    /*async*/ getMasterTrack() {
      // http://193.124.206.179:5000/audio/uploads/6d4bbe1b-c06d-49b2-ba63-3be00706c25c
      return {
        id: 1,
        title: 'For Hack with love',
        author: 'A team ai dj',
        url: 'http://193.124.206.179:5000/audio/uploads/6d4bbe1b-c06d-49b2-ba63-3be00706c25c',
        includes: [
          {start: 1, end: 20, title: 'some music'},
          {start: 21, end: 60, title: 'yet another track'}
        ]
      };

    }
}