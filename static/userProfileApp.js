const orderApp = Vue.createApp({
    data() {
        return {
            orders: [],
            meta: {}
        }
    },
    methods: {
        addOrderId(id) {
            if (id in this.meta && this.meta[id] != undefined) {
                delete this.meta[id]
            } else {
                this.meta[id] = undefined
            }
        },
        getItems(id) {
            if (this.meta[id] === undefined){
                axios.get('/api/orderItems/', {params:{"order":id}})
                    .then(
                        meta => {this.meta[id] = meta}
                    )
                }
            return this.meta[id].data
        }
    },
    mounted() {
        axios.get('/api/orders/')
        .then(meta => {
                    console.log(meta.data);
                    this.orders = meta.data;
                    for (const order of this.orders){
                        axios.get('/api/orderItems/', {params:{"order":order.id}})
                        .then(
                            meta => {
                                order['items'] = meta.data
                            }
                        )
                    }
                });
    },
})