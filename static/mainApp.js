window.csrfToken = document.querySelector('meta[name="csrf-token"]').content;
const app = Vue.createApp({
    data() {
        return {
            items: null,
            cart : 0
        }
    },
    methods: {
        addToCart() {
            this.cart += 1
        },
        add(id) {
            axios.defaults.xsrfHeaderName = "X-CSRFToken";
            axios.post('/cart/add/' + id + '/',{_token:csrfToken, data:{quantity:1}})
        }
    },
    mounted() {
        axios.get('/api/items/')
        .then(meta => { console.log(meta.data);
                  this.items = meta.data
                })
    },
})