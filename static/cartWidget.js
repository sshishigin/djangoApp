const cartWidgetApp = Vue.createApp({
    data() {
        return {
            items: null,
            cart_quantity : 0
        }
    },
    methods: {
        cartDetail(){
            axios.get('/api/cart/')
        }
    },
    mounted() {
        axios.get('/api/cart/')
        .then(meta => {
            this.cart_quantity=meta.data.length;
        })
    },
})