const app = Vue.createApp({
    data() {
        return {
            items: null,
        }
    },
    methods: {
        addToCart(id) {
            axios.put('/api/cart/', {quantity:1, item_id:id});
        }
    },
    mounted() {
        axios.get('/api/items/')
        .then(meta => {
                    this.items = meta.data;
                });
    },
})