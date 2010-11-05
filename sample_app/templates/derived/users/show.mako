<%inherit file="/base/application.mako" />

<table class="profile">
  <tr>
    <td class="main">
      <h2>
        ${h.gravatar_img(c.user.email)}
        ${escape(c.user.name)}
      </h2>
    </td>
    <td class="sidebar round">
      <strong>Name</strong> ${c.user.name}<br />
      <strong>URL</strong>  ${h.link_to(h.url("user", id=c.user.id),h.url("user", id=c.user.id))}
    </td>
  </tr>
</table>
