<template>
<div>
     <div class="content-fluid">
            <nav id="styleguideSidebar" class="sidebar sidebar--mini sidebar--indigo" role="navigation">
                <div class="sidebar__header">
                    <a id="sidebar-toggle" class="sidebar-toggle hidden-xs hidden-sm">
                        <span class="icon-toggle-menu"></span>
                    </a>
                    <div class="sidebar__header-title">Cisco UI Kit</div>
                </div>
                <ul id="rootSidebar" data-kss-ref="styleguide.homepage">
                    <li class="sidebar__item" id="section-gettingStarted">
                        <a onclick="doNav('./index.html')" title="Getting Started">
                            <span class="icon-home"></span>
                            <span>Home</span>
                        </a>
                    </li>
                    <li class="sidebar__drawer">
                        <a tabindex="0" title="Resources">
                            <span class="icon-tools"></span>
                            <span>Resources</span>
                        </a>
                        <ul>
                            <li class="sidebar__item"><a href="http://bx.cisco.com/cbx-portal/" target="_blank">Cisco Brand Exchange</a></li>
                            <li class="sidebar__item"><a href="https://apps.na.collabserv.com/communities/service/html/communitystart?communityUuid=f440dc5c-b623-4fdb-b5da-a455c5a1ac58" target="_blank">UI Kit Home Page</a></li>
                            <li class="sidebar__item"><a href="https://apps.na.collabserv.com/wikis/home?lang=en-us#!/wiki/Wa4b9a3b71b87_4b16_88f1_7f66e71f0276/page/The%20UI%20Kit%20(Atlantic)%20-%20FAQs" target="_blank">UI Kit FAQ</a></li>
                            <li class="sidebar__item"><a href="https://wwwin-gitlab-sjc.cisco.com/cisco-ui-angular-1" target="_blank">Angular 1.x Components</a></li>
                            <li class="sidebar__item"><a href="https://wwwin-gitlab-sjc.cisco.com/cisco-ui-angular-4" target="_blank">Angular 4.x Components</a></li>
                            <li class="sidebar__item"><a href="https://wwwin-gitlab-sjc.cisco.com/cisco-ui-react" target="_blank">React Components</a></li>
                        </ul>
                    </li>
                    <li class="sidebar__drawer">
                        <a tabindex="0" title="For Designers">
                            <span class="icon-draw"></span>
                            <span>Files</span>
                        </a>
                        <ul>
                            <li class="sidebar__item"><a href="public/documents/sketch/CiscoUI-Icons.sketch" download="public/documents/sketch/CiscoUI-Icons.sketch">Icons (Sketch)</a></li>
                            <li class="sidebar__item"><a href="public/documents/sketch/button.sketch" download="public/documents/sketch/button.sketch">Buttons (Sketch)</a></li>
                            <li class="sidebar__item"><a href="public/documents/sketch/checkbox.sketch" download="public/documents/sketch/checkbox.sketch">Checkboxes (Sketch)</a></li>
                            <li class="sidebar__item"><a href="public/documents/sketch/radio.sketch" download="public/documents/sketch/radio.sketch">Radios (Sketch)</a></li>
                            <li class="sidebar__item"><a href="public/documents/sketch/switch.sketch" download="public/documents/sketch/switch.sketch">Switches (Sketch)</a></li>
                        </ul>
                    </li>
                    <li class="sidebar__drawer">
                        <a tabindex="0" title="Older Versions">
                            <span class="icon-history"></span>
                            <span>Versions</span>
                        </a>
                        <ul>
                            <li class="sidebar__item"><a href="http://swtg-rtp-dev-7/styleguide-dist/1.3.3-official/" target="_blank">Version 1.3.3</a></li>
                            <li class="sidebar__item"><a href="http://swtg-rtp-dev-7/styleguide-dist/1.3.2-official/" target="_blank">Version 1.3.2</a></li>
                            <li class="sidebar__item"><a href="http://swtg-rtp-dev-7/styleguide-dist/1.2.2-official/" target="_blank">Version 1.2.2</a></li>
                            <li class="sidebar__item"><a href="http://swtg-rtp-dev-7/styleguide-dist/1.2.0-official/" target="_blank">Version 1.2.0</a></li>
                            <li class="sidebar__item"><a href="http://swtg-rtp-dev-7/styleguide-dist/1.1.0-official/" target="_blank">Version 1.1.0</a></li>
                            <li class="sidebar__item"><a href="http://swtg-rtp-dev-7/styleguide-dist/1.0.5-official/" target="_blank">Version 1.0.5</a></li>
                            <li class="sidebar__item"><a href="http://swtg-rtp-dev-7/styleguide-dist/1.0.4-official/" target="_blank">Version 1.0.4</a></li>
                            <li class="sidebar__item"><a href="http://swtg-rtp-dev-7/styleguide-dist/1.0.3-official/" target="_blank">Version 1.0.3</a></li>
                            <li class="sidebar__item"><a href="http://swtg-rtp-dev-7/styleguide-dist/1.0.2-official/" target="_blank">Version 1.0.2</a></li>
                            <li class="sidebar__item"><a href="http://swtg-rtp-dev-7/styleguide-dist/1.0.1-official/" target="_blank">Version 1.0.1</a></li>
                            <li class="sidebar__item"><a href="http://swtg-rtp-dev-7/styleguide-dist/1.0.0-official/" target="_blank">Version 1.0.0</a></li>
                        </ul>
                    </li>
                    <li class="sidebar__drawer">
                        <a tabindex="0" title="Examples">
                            <span class="icon-applications"></span>
                            <span>Examples</span>
                        </a>
                        <ul>
                            <li class="sidebar__item">
                                <a href="assets/basic.html">Basic Page Template</a>
                            </li>
                            <li class="sidebar__item">
                                <a href="assets/list.html">List Page Template</a>
                            </li>
                            <li class="sidebar__item">
                                <a href="assets/standard.html">Standard Page Template</a>
                            </li>
                            <li class="sidebar__item">
                                <a href="assets/sidebar.html">Sidebar Page Template</a>
                            </li>
                            <li class="sidebar__item">
                                <a href="assets/wide.html">Wide Page Template</a>
                            </li>
                            <li class="sidebar__item">
                                <a href="assets/collage.html">Collage</a>
                            </li>
                        </ul>
                    </li>
                    <li id="rootDrawer" class="sidebar__drawer">
                        <a tabindex="0" title="Pattern Library">
                            <span class="icon-plugin"></span>
                            <span>Patterns</span>

                        </a>
                        <ul>
                            <li class="sidebar__item"><a href="index.html">Home</a></li>
                            <li class="sidebar__item"><a href="section-design.html#design-typography">Design</a></li>
                            <li class="sidebar__item"><a href="section-primitives.html#primitives-blockquote">Primitives</a></li>
                            <li class="sidebar__item"><a href="section-components.html#components-alert">Components</a></li>
                            <li class="sidebar__item"><a href="section-layout.html#layout-footer">Layout</a></li>
                            <li class="sidebar__item"><a href="section-utilities.html#utilities-helpers">Utilities</a></li>
                        </ul>
                    </li>
                </ul>
            </nav>
            <main>
                <header id="styleguideHeader" class="header header--compressed">
                    <div class="header-bar flex-center-sm container-fluid">
                        <a id="mobile-sidebar-toggle" class="sidebar-toggle visible-xs visible-sm base-margin-right">
                            <span class="icon-list-menu"></span>
                        </a>
                        <a class="header-bar__logo" href="http://www.cisco.com" target="_blank">
                            <span class="icon-cisco"></span>
                        </a>
                        <div class="header-bar__main hidden-xs hidden-sm">
                            <div class="header-heading">
                                <h1 class="page-title">Cisco UI Kit</h1>
                            </div>
                        </div>
                        <div class="header-toolbar hidden-xs hidden-sm hidden-md">

                            <div>
                                <a href="index.html">Home</a>
                                <a href="section-design.html#design-typography" class="base-margin-left">Design</a>
                                <a href="section-primitives.html#primitives-blockquote" class="base-margin-left">Primitives</a>
                                <a href="section-components.html#components-alert" class="base-margin-left">Components</a>
                                <a href="section-layout.html#layout-footer" class="base-margin-left">Layout</a>
                                <a href="section-utilities.html#utilities-helpers" class="base-margin-left">Utilities</a>

                                <div class="dropdown dropdown--left dropdown--tail base-margin-left">
                                    <a>Globals</a>
                                    <div class="dropdown__menu">
                                        <a>
                                            <label class="checkbox">
                                                <input id="global-animation" type="checkbox" checked>
                                                <span class="checkbox__input"></span>
                                            </label>
                                            <span>Animations</span>
                                        </a>
                                        <a>
                                            <label class="checkbox">
                                                <input id="global-headermargins" type="checkbox" checked>
                                                <span class="checkbox__input"></span>
                                            </label>
                                            <span>Header Margins</span>
                                        </a>
                                        <a>
                                            <label class="checkbox">
                                                <input id="global-spacing" type="checkbox">
                                                <span class="checkbox__input"></span>
                                            </label>
                                            <span>Compression</span>
                                        </a>
                                        <a>
                                            <label class="checkbox">
                                                <input id="global-wide" type="checkbox" checked>
                                                <span class="checkbox__input"></span>
                                            </label>
                                            <span>Wide View</span>
                                        </a>
                                        <a>
                                            <label class="checkbox">
                                                <input id="global-sticky" type="checkbox">
                                                <span class="checkbox__input"></span>
                                            </label>
                                            <span>Sticky Header/Footer</span>
                                        </a>
                                    </div>
                                </div>
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
        <home-page></home-page>   
    </div>
   
</div>
</div>
<footer class="footer footer--basic">
    <div class="footer__links">
        <ul class="list">
            <li><a href="http://www.cisco.com/cisco/web/siteassets/contacts/index.html" target="_blank">Contacts</a></li>
            <li><a href="https://secure.opinionlab.com/ccc01/o.asp?id=jBjOhqOJ" target="_blank">Feedback</a></li>
            <li><a href="https://www.cisco.com/c/en/us/about/help.html" target="_blank">Help</a></li>
            <li><a href="http://www.cisco.com/c/en/us/about/sitemap.html" target="_blank">Site Map</a></li>
            <li><a href="https://www.cisco.com/c/en/us/about/legal/terms-conditions.html" target="_blank">Terms &amp; Conditions</a></li>
            <li><a href="https://www.cisco.com/c/en/us/about/legal/privacy-full.html" target="_blank">Privacy Statement</a></li>
            <li><a href="https://www.cisco.com/c/en/us/about/legal/privacy-full.html#cookies" target="_blank">Cookie Policy</a></li>
            <li><a href="https://www.cisco.com/c/en/us/about/legal/trademarks.html" target="_blank">Trademarks</a></li>
        </ul>
    </div>
</footer>
</main>
        <div id="modal-backdrop" class="modal-backdrop hide"></div>
</div>
</div>
</template>
<script>
import Home from '../components/VueHome'
export default {
   components:{
       'home-page' : Home
   }
}
</script>

