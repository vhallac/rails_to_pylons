<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html lang="en" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>${h.title()}</title>
    ${h.stylesheet_link('/stylesheets/blueprint/screen.css', media='screen') }
    ${h.stylesheet_link('/stylesheets/blueprint/print.css', media='print') }
  </head>
  <body>
    ${self.body()}
  </body>
</html>
