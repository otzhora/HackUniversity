<template>
  <div id="app">
    <div id="nav">
      <nav class="navbar" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">

          <a class="navbar-item" href="/">
            <img src="./assets/logo1.jpg" alt="logo" >
          </a>
          
        </div>
        <div class="navbar-menu">
          <div class="navbar-start">
            <!-- navbar items -->
          </div>

          <div class="navbar-end">
            <!-- navbar items -->
            <a class="navbar-item">
              <router-link to="/">Home</router-link>
            </a>
            <a class="navbar-item">
              <router-link to="/master">Master</router-link>
            </a>
            
          </div>
        </div>
        
      </nav>
      
      
    </div>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

</style>
