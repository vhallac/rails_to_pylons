<%inherit file="/base/application.mako" />

<h1>Sample App</h1>
<p>
  This is the home page for the
  <a href="http://www.railstutorial.org/">Ruby on Rails Tutorial</a>
  sample application.
</p>

${h.link_to("Sign up now!", h.url('signup'), class_="signup_button round")}
