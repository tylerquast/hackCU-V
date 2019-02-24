// Home.vue

<template>
  <div>
    <b-form-input class='userInput' v-model="text1" type="text" placeholder="Enter your username" />
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
  export default {
    data() {
      return {
        text1: ''
      }
    },
    methods:{
        getRandomFromBackend () {
          var path = 'http://localhost:5000/api/random'
          axios.post(path, 
          {
            "Name": this.text1
          })
          .then(function (response) {
            console.log(response.data)
          })
          .catch(function (error) {
            console.log(error);
          });
      },
    }
  }
</script>

<style>
  .userInput{
    width:500px;
    margin:auto;
  }
  .submitButton{
    width:200px;
    margin:auto;
  }
</style>
