<template>
<div>
     <div class="content-fluid">
            <nav id="styleguideSidebar" class="sidebar sidebar--mini sidebar--indigo" role="navigation">
                <div class="sidebar__header">
                    <a id="sidebar-toggle" class="sidebar-toggle hidden-xs hidden-sm">
                        <span class="icon-toggle-menu"></span>
                    </a>
                    <div class="sidebar__header-title">Cisco MEA Inventory</div>
                </div> 
                <ul id="rootSidebar" data-kss-ref="styleguide.homepage">
                    <li class="sidebar__item" id="section-gettingStarted">
                        <a href="http://inventory.cisco.com" title="Getting Started">
                            <span class="icon-home"></span>
                            <span>Home</span>
                        </a>
                    </li>
                </ul>
            </nav>
            <main>
                <header id="styleguideHeader" class="header header--compressed">
                    <div class="header-bar flex-center-sm container-fluid">
                        <a id="mobile-sidebar-toggle" class="sidebar-toggle visible-xs visible-sm base-margin-right">
                            <span class="icon-list-menu"></span>
                        </a>
                        <a class="header-bar__logo" href="http://inventory.cisco.com" target="_blank">
                            <span class="icon-cisco"></span>
                        </a>
                        <div class="header-bar__main hidden-xs hidden-sm">
                            <div class="header-heading">
                                <h1 class="page-title">Cisco MEA Inventory</h1>
                            </div>
                        </div>
                        <div class="header-toolbar hidden-xs hidden-sm hidden-md">

                            <div>
                                <a href="/">Home</a>
                            </div>
                        </div>
                    </div>
                </header>
                <div class="content content--alt"> <p><div class="container-fluid center-xs">
    <div id="broadcast" class="alert hide">
        <div class="alert__icon icon-info-circle"></div>
        <div id="broadcast-msg" class="alert__message"></div>
    </div>
   <div class="base-padding-top dbl-padding-bottom dbl-margin-bottom">
        <portal-page></portal-page>   
    </div>
   
</div>
</div>

</main>
        <div id="modal-backdrop" class="modal-backdrop hide"></div>
</div>
</div>
</template>
<script>
import Portal from '../components/VuePortal'
export default {
   components:{
       'portal-page' : Portal
   }
}
</script>

