new Vue({
    el: "#index_w_api",
    data: {
        items: []
    },
    created: function () {
        const vm = this;
        axios.get('/api/index/')
        .then(function(response){
            vm.items = response.data
        })
    }
})