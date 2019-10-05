<template>
  <div class="portal">
     <div class="row text-center">
      <div class="card col-md-4 offset-md-4">
        <div class="card__body">
          <h3 class="text-uppercase base-margin-bottom">Portal</h3>
          <div v-show="errors" class="alert alert-danger">
            <ul >
              <li  v-for="error,index in errors">
               {{index}} : {{error[0]}} 
              </li>
            </ul>
           
          </div>
          <div class="alert alert-success" v-if='this.done'>your application submitted successfully</div>
          <div class="flex">
           <form @submit.prevent="send" class="form-group">
            <div class="card-content">
              <div class="row">
               

                <div class="form-group__text col-md-12">
                      <input v-model="data.name" id="name" type="text" class="validate" placeholder="">
                      <label for="cec">CEC
                         <div class="tooltip">?
                            <span class="tooltiptext">your cisco username</span>
                        </div>
                      </label>
                </div>


                     <div class="form-group__text col-md-12">
                     <select name="country" id="country" v-model='data.country'>
                       <option value="" disabled selected>Select your region</option>
                       <option value="KSA">KSA</option>
                       <option value="IXC">IXC</option>
                       <option value="Dubai">Dubai</option>
                       <option value="Turkey">Turkey</option>
                     </select>
                      <label for="country">Region 
                        <div class="tooltip">?
                            <span class="tooltiptext">Select the country that you are making the order from</span>
                        </div>

                      </label>
                </div>


                <div class="form-group__text col-md-12">
                      <label for="product">Product</label>
                      <select name="product" id="product" class="select" v-show="this.products.length">
                        <option value="" disabled selected>Select the product</option>
                        <option v-for="product in products" :value="product.model.name" >{{product.model.name}}</option>
                      </select>
                      <i class="fa fa-spinner fa-spin" v-if="!this.products.length"></i>
                </div>

                <div class="form-group__text col-md-12">
                      <input v-model="data.duration" id="duration" type="number" class="validate" placeholder="">
                      <label for="duration">Duration
                         <div class="tooltip">?
                            <span class="tooltiptext">Number of duration in days</span>
                        </div>
                      </label>
                </div>

                <div class="form-group__text col-md-12">
                      <input v-model="data.did" id="did" type="text" class="validate" placeholder="Enter your Deal ID">
                      <label for="did">Deal ID</label>
                </div>

           
              


              </div>
            </div>
            <div class="base-margin-top">
             
              <button type="submit" :disabled='this.loading' class="btn btn--wide btn--primary-ghost" > Send <i v-show="this.loading" class="fa fa-spinner fa-spin"></i></button>
              
            </div>
          </form>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>
<script>
import {getHeader} from '../config'
export default {
  mounted(){
    this.getHardware()
    $('.select').on('select2:select', (e) =>  {
        var selected = e.params.data;
        this.data.product = selected.id 
        
    });
  },
  data(){
    return{
      data : {
        name : '',
        cid : '1',
        did : '',
        product : '',
        duration : '',
        country : '',
        username :'',
        password : '',
      },
        loading : false,
        done : false,
      errors : false,
      products : []
    }
  },
  methods:{
    send(){
      this.loading = true;
      this.errors = false;
      this.axios.post(process.env.VUE_APP_API_DOMAIN+'/api/portal/',this.data
       // ,{headers:getHeader(localStorage.getItem('authData'))}
      )
            .then(response => {
              this.loading = false;
              cl(response)
              this.done = true
            }).catch(err => {
                this.loading = false;
                 if (err.response.status === 400 && typeof(err.response.data) !== 'string') {
                    this.errors = err.response.data
                 }else{
                   this.errors = {
                     'Message' : ['Something went wrong, please try again later']
                   }
                 }
            })
    },
    getHardware(){
        this.axios.post(process.env.VUE_APP_API_DOMAIN+'/api/hardware/',this.data
        // ,{headers:getHeader(localStorage.getItem('authData'))}
        )
            .then(response => {
              this.products = JSON.parse(response.data)
              this.products = this.products.rows
              cl(this.products.length)
              setTimeout(() => {
                $('.select').select2();
              }, 500);
            }).catch(err => {
                ce(err.response)
            })
    },
  }
}
</script>
