This is a re-implementation of the Ruby on Rails tutorial in pylons.

I've tried to stay as close to the applicaiton for Rails, but in some instances this was not possible. The areas that require more works are:

- Model level validations: The model, its renderer and validators are tightly
  coupled in Rails. This is not the case for Pylons. I will revisit this after
  the initial port is done.

- The model doesn't keep the clear text password at all. As sson as it is set or
  changed, it is hashed.

- Form error rendering: It may be possible to generate a for with error messages
  that look very similar to the rails application, but it would require a lot of
  work - and maybe experimenting with alternate form rendering/validating
  libraries. I will leave this as is for now.

- Logging? No idea where/how things are logged in pylons. Need to stop passwords
  from being printed to the log files if it happens.


Progress: Finished Chapter 7
