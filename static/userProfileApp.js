const orderApp = Vue.createApp({
    data() {
        return {
            orders: []
        }
    },
    methods: {
    },
    mounted() {
        axios.get('/api/orders/')
        .then(meta => {
                    console.log(meta.data);
                    this.orders = meta.data;
                });
    },
})