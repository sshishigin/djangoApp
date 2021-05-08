const itemPageApp = Vue.createApp({
    data() {
        return {
            item : {}
        }
    },
    methods: {
    },
    mounted() {
        axios.get('/api/items/' + item_id)
        .then(meta => {this.item = meta.data;} );
    },
})