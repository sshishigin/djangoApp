const app = Vue.createApp({
    data() {
        return {
            items: null,
        }
    },
    methods: {
        addToCart(id) {
            axios.post('/api/cart/', {quantity:1, itemId:id});
        },
        like(id) {
            axios.post('/api/like/', {itemId:id, like:true})
        }

    },
    mounted() {
        axios.get('/api/items/')
        .then(meta => {
                    this.items = meta.data;
                });
    },
})