/* Manage tracks */

export default {

    getTracksList() {
        let tracks = [
            {id: 1, title: 'Old Town Road', url: 'https://soundcloud.com/secret-service-862007284/old-town-road'},
            {id: 2, title: 'some track #2'},
            {id: 3, title: 'some track #3'},
            {id: 4, title: 'some track #4'}
        ];

        return tracks;
    },

    getTrack(id) {
        return {id: id, title: `some track #${id}`};
    }
}