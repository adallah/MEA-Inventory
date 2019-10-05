<template>
    <div>
        <!-- Dropdown Structure -->
            <ul id="dropdown1" class="dropdown-content">
            <li><a href="#!">Account</a></li>
            <li class="divider"></li>
            <li><a href="#!">Logout</a></li>
            </ul>
            <nav>
            <div class="nav-wrapper">
                <a href="/" class="brand-logo">Portal</a>
                <ul class="right hide-on-med-and-down">
                <li><a href="register">Register</a></li>
                <li><a href="/">Login</a></li>
                <!-- Dropdown Trigger -->
                <li><a class="dropdown-trigger" href="#!" data-target="dropdown1">Dropdown<i class="material-icons right">arrow_drop_down</i></a></li>
                </ul>
            </div>
            </nav>  
    </div>
</template>
<script>
export default {
    mounted(){
        $(".dropdown-trigger").dropdown();
    }
}
</script>
