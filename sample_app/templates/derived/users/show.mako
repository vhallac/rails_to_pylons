<%inherit file="/base/application.mako" />

<h2>
  ${h.gravatar_img(c.user.email)}
  ${escape(c.user.name)}
</h2>
