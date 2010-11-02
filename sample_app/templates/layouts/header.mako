<div id="header">
  ${h.link_to(h.image("/images/logo.png", alt="Sample App", class_="round"), h.url("home"))}
  <ul class="navigation round">
    <li>${h.link_to("Home", h.url("home"))}</li>
    <li>${h.link_to("Help", h.url("help"))}</li>
    <li>${h.link_to("Sign in", "#")}</li>
  </ul>
</div>
