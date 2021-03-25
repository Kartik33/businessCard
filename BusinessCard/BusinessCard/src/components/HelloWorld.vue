<template>
  <div>
    <h1>{{ msg }}</h1>
        <div class="vue-tempalte">
     <form ref="signup" id="signup" @submit.prevent="signup">
        <h3>Sign Up</h3>

            <div class="form-element">
                <p><label>First Name:  </label>
                <input pv-model="form.first_name" type="text" /></p>

                <p><label>Last Name:  </label>
                <input pv-model="form.last_name" type="text" /></p>

                <p><label>Email address</label>
                <input type="email" v-model="form.email"/></p>

                <p><label>Password</label>
                <input type="password" v-model="form.password"/></p>
            </div>
            <br>
            <button type="submit">Sign Up</button>

            <p>
                Already registered 
                <router-link :to="{name: 'login'}">sign in?</router-link>
            </p>
        </form>
    </div>
  </div>
</template>

<script>
new Vue({
  el: '#signup',
  data: {
    form : {
      first_name: ''
    }
  }
})
export default {
  name: 'HelloWord',
  props: {
    msg: String
  }
}
</script>


<style>
    .form-element label {
    display: inline-block;
    width: 150px;
}
</style>
