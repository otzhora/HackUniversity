/* Manage tracks */
import axios from 'axios';

export default {
    async getTracksList() {
        let tracks = [
            {
                id:1,
                local: false,
                title: 'Girl i want/girl I need [rough]',
                url: 'https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/465705123&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true'
              },
              {
                id:2,
                local: false,
                title: "When you're near",
                url: 'https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/427416225&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true'
              },
              {
                id:3,
                local: false,
                title: 'Hardwell - Spaceman (Carnage Festival Trap Remix)',
                url: 'https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/59527799&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true'
              }
        ];
        
        let url = 'http://localhost:5000/audio/uploads'
        let res = await axios.get(url)
        res = res.data
        for(let key in res) {
          tracks.push({
            id:key,
            title:res[key]['title'],
            url: url + '/' + key
          })
        }
        return tracks;
    },

    getTrack(id) {
        return {id: id, title: `some track #${id}`};
    },

    getScTracksList() {
        let sctracks = [
            {
                id:101,
                local: true,
                title: 'Hardcoded Track 1',
                url: 'https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/465705123&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true'
              },
              {
                id:102,
                local: true,
                title: "Hardcoded Track 2",
                url: 'https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/427416225&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true'
              },
              {
                id:103,
                local: true,
                title: 'Hardcoded Track 3',
                url: 'https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/59527799&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true'
              }
        ];

        return sctracks;
    }
}