const app = Vue.createApp({
    data() {
        return {
        items : null
        }
    },
    methods: {
        cleanCart() {
            axios.patch('/api/cart/', {clearCart: true})
        },
        remove(id) {
            axios.put('/api/cart/', {itemIdList: [id], 'clearCart': false});
            this.items[id]['removed'] = true;
        }
    },
    mounted() {
        axios.get('/api/cart/')
        .then(meta => {
            this.items = meta.data;
            for (i = 0; i < this.items.length; i++) {
                this.items[i]['removed'] = false;
            };
            console.log(this.items)
        })
    },
})