const cartWidgetApp = Vue.createApp({
    data() {
        return {
            items: null,
            cart_quantity : 0
        }
    },
    methods: {
        cartDetail(){
            axios.get('/cart')
        }
    },
    mounted() {
        axios.get('/cart/api')
        .then(meta => {
            this.cart_quantity=meta.data.length;
            console.log(meta.data)
        })
    },
})