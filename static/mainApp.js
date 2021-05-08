const app = Vue.createApp({
    data() {
        return {
            items: null,
            cart_quantity : 0
        }
    },
    methods: {
        addToCart(id) {
            axios.post('cart/add/', {quantity:1, item_id:id});
        }
    },
    mounted() {
        axios.get('/api/items/')
        .then(meta => {
                    console.log(meta.data);
                    this.items = meta.data;
                });
        axios.get('/cart/api')
        .then(meta => {
            this.cart_quantity=meta.data.length
        });
    },
})