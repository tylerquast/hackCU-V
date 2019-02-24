// Process.vue

<template>
  <div>
    <p>Welcome {{username}}</p>
    <br>
    <div v-for="(value, key) in tableData">
      {{ key }}: {{ value }}
    </div>
    <br>
    <p>Please Enter Your Bitcoin Address</p>
    <b-form-input class='userInput' v-model="bitcoinKey" type="text" placeholder="Enter Bitcoin Key" />
    <br>
    <b-button 
      class='submitButton' 
      variant="danger" 
      v-on:click="getRandomFromBackend()">
      Submit
    </b-button>
  </div>
</template>


<script>
  import axios from 'axios';
  export default{
    data() {
      return{
        username: '',
        tableData:[],
        bitcoinKey:''
      }
    },
    created(){
      var vars = {}
      var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
      vars[key] = value;
      });
      this.username = vars['name']
      this.getData()
      console.log(this.tableData)
      
    },
    methods:{
      submitToke(){
        var path = 'http://localhost:5000/api/submitToken'
      },
      getData () {
        self = this
        var path = 'http://localhost:5000/api/getData'
        axios.post(path, 
        {
          "name": this.username
        })
        .then(function (response) {
          self.tableData = response.data
        })
        .catch(function (error) {
          console.log(error);
        });
      }
    }
  }
  
</script>

<style>
.userInput{
  width:500px;
  margin:auto;
}
</style>
