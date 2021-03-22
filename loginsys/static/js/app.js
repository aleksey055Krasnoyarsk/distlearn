Vue.component('all-groups', {
  props: ['groups'],
    template: '<li>ID Группы: {{ groups.id }}  Название Группы:{{ groups.group }}<button class="btn btn-danger" v-on:click="DelGroup(i.id)">Удалить</button></li>'
})


Vue.component('btn-delGroup', {
  methods: {

  DelGroup(id) {
      axios
          .delete('http://127.0.0.1:8000/api/groups/' + id, {headers: {"X-CSRFToken": 'E7GBSFXgTWVWhiHVTfJNFLn4POqrEW8Hmz03bK8WfQpk8MlefZc2v7c5v2QabATZ'}},)
          .then(response => {
            this.response = response.data.id
            console.log(response.data.id)
            console.log(this.response)

      })
      }

  },
  template: '<button class="btn btn-danger" v-on:click="DelGroup(i.id)">Удалить</button>'
})





 // register modal component
Vue.component("modal", {
    template: "#modal-template"
});


new Vue({
  el: '#loginsys_app',
  data: {

    groups: [],
    danye: {
      group: "",
      id: 0
    },
    showModal: false,
    showInput: false,
    update: {
       group: '',
       id: null
    },

  },

  computed: {
    id: function () {
      // `this` указывает на экземпляр vm
      return this.danye.id
    }
  },

  mounted: function() {
   this.AllGroups();
  },

  methods: {

   AllGroups() {
      axios
        .get('http://127.0.0.1:8000/api/groups/', {headers: {"X-CSRFToken": 'E7GBSFXgTWVWhiHVTfJNFLn4POqrEW8Hmz03bK8WfQpk8MlefZc2v7c5v2QabATZ'}},)
        .then(response => (this.groups = response.data))
        .catch(error => {
          console.log(error)
      })
  },


   GetGroup(id) {
      axios
        .get('http://127.0.0.1:8000/api/groups/' + id, {headers: {"X-CSRFToken": 'E7GBSFXgTWVWhiHVTfJNFLn4POqrEW8Hmz03bK8WfQpk8MlefZc2v7c5v2QabATZ'}},)
        .then(response => {
          this.response = response.data.id
          console.log(response.data.id)
          console.log(this.response)

      })


  },

   AddGroup() {
      axios
        .post('http://127.0.0.1:8000/api/groups/', {"group": this.danye.group }, {headers: {"X-CSRFToken": 'E7GBSFXgTWVWhiHVTfJNFLn4POqrEW8Hmz03bK8WfQpk8MlefZc2v7c5v2QabATZ'}},)
        .then(function (response) { console.log(response); })
        .catch(function (error) { console.log(error.response); });
  },

   UpdateGroup(id) {
      axios
        .put('http://127.0.0.1:8000/api/groups/' + id + '/', {"group": this.update.group }, {headers: {"X-CSRFToken": 'E7GBSFXgTWVWhiHVTfJNFLn4POqrEW8Hmz03bK8WfQpk8MlefZc2v7c5v2QabATZ'}},)
        .then(function (response) { console.log(response); })
        .catch(function (error) { console.log(error.response); });
   },


   DelGroup(id) {
      axios
        .delete('http://127.0.0.1:8000/api/groups/' + id, {headers: {"X-CSRFToken": 'E7GBSFXgTWVWhiHVTfJNFLn4POqrEW8Hmz03bK8WfQpk8MlefZc2v7c5v2QabATZ'}},)
        .then(response => {
          this.response = response.data.id
          console.log(response.data.id)
          console.log(this.response)

      })

      },
  },



});
