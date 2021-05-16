const itemPageApp = Vue.createApp({
    data() {
        return {
            item : {},
            blabla : {'hui':2},
        }
    },
    methods: {
    },
    mounted() {
        axios.get('/api/items/' + item_id)
        .then(meta => {this.item = meta.data;} );
    },
})