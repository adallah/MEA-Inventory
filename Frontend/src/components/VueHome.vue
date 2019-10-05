<template>
  <div class="home">
    <div class="row text-center">
      <div class="card col-md-4 offset-md-4">
        <div class="card__body">
          <h3 class="text-uppercase base-margin-bottom">Enter credentials</h3>
          <div class="flex">
            <form @submit.prevent="send" class="form-group">
              <div class="row">
                <div class="form-group__text col-md-12">
                      <label for="email">Email</label>
                      <input v-model="data.username" id="email" type="text" class="form-control">
                </div>
                <div class="form-group__text col-md-12">
                      <label for="Password">Password</label>
                      <input v-model="data.password" id="Password" type="Password" class="form-control">
                </div>
              </div>
          
            <div class="base-margin-top">
              <input type="submit" class="btn btn--wide btn--primary-ghost" value="Login">
            </div>
          </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'home',
  data(){
    return{
      data : {
        grant_type: 'password',
        username : '',
        password : '',
        client_id: process.env.VUE_APP_clientID,
        client_secret: process.env.VUE_APP_clientSecret
      }
    }
  },
  methods:{
    send(){
      this.axios.post(process.env.VUE_APP_API_DOMAIN+'/o/token/',this.data)
      .then(response => {
        window.localStorage.setItem('authData',JSON.stringify(response.data))
        redirect('/portal')
      }).catch(errors => {
        ce(errors)
      })
    }
  }
}
</script>
