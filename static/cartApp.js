const app = Vue.createApp({
    data() {
        return {
        cart_total_quantity : 0,
        items : null
        }
    },
    methods: {
        cleanCart() {
            axios.post('clear/', {_token:csrfToken})
        },
        remove(id) {
            axios.post('remove/',
            {_token:csrfToken, data:{item_id:id}});
            this.items[id]['removed'] = true;
        }
    },
    mounted() {
        axios.get('/cart/api')
        .then(meta => {
            this.items = meta.data;
            for (i = 0; i < this.items.length; i++) {
                this.items[i]['removed'] = false;
                console.log(this.items[i]);
            }
        })
    },
})