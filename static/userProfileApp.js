const orderApp = Vue.createApp({
    data() {
        return {
            orders: [],
            meta: {},
            likedItems:[]
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
        },
        removeLike(id){
            console.log(id)
            axios.post('/api/like/', {'itemId':id, like:false})
        }
    },
    mounted() {
        axios.get('/api/order/')
        .then(meta => {
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
        axios.get('/api/like/')
        .then(meta => {
            for(const itemId of meta.data){
                axios.get('/api/items/'+itemId.item)
                .then(
                    meta => {
                        this.likedItems.push(meta.data)
                    }
                )
            }
        })
    },
})