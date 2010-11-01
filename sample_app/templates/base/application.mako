<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang="en" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>${h.title()}</title>
    ${stylesheets.body()}
  </head>
  <body>
    <div class="container">
      ${header.body()}
      <div id="content" class="round">
        ${self.body()}
      </div>
      ${footer.body()}
    </div>
  </body>
</html>

<%namespace name="stylesheets" file="/layouts/stylesheets.mako" />
<%namespace name="header" file="/layouts/header.mako" />
<%namespace name="footer" file="/layouts/footer.mako" />
