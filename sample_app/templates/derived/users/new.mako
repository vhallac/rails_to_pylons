<%inherit file="/base/application.mako" />

<h2>Sign up</h2>

${h.form(h.url(controller="users", action="create"), method="post")}
<div class="field">
  <label for="name">Name</label><br />
  ${h.text(name='name', size=30, label="Name")}
</div>
<div class="field">
  <label for="email">E-mail</label><br />
  ${h.text(name='email', size=30)}
</div>
<div class="field">
  <label for="password">Password</label><br />
  ${h.password(name='password', size=30)}
</div>
<div class="field">
  <label for="password_confirmation">Confirmation</label><br />
  ${h.password(name='password_confirmation', size=30)}
</div>
<div class="actions">
  ${h.submit(value="Sign up", name='submit')}
</div>
${h.end_form()}
