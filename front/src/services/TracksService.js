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
    }
}