const itemPageApp = Vue.createApp({
    data() {
        return {
            item : {},
            quantityToAdd: 0
        };
    },
    methods: {
        addItem() {
            this.quantityToAdd += 1;
            
        },
        removeItem() {
            this.quantityToAdd -= 1;
        },
        setItemQuantity(value) {
            if ((+value && +value >= 0 && ((+value) % 1) === 0) || +value === 0) {
                this.quantityToAdd = Number(value);
            }
        },
        addToCart() {
            axios.post('/api/cart/', {quantity:this.quantityToAdd, itemId:this.item.id});
        }
    },
    mounted() {
        axios.get('/api/items/' + item_id)
        .then(meta => {this.item = meta.data;} );
    },
    computed: {
    }
});