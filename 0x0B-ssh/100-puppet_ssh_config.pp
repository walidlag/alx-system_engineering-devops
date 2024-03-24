#!/usr/bin/env bash
# make the changes to configuration file

file { '/etc/ssh/ssh_config':
  ensure  => present,
content => "
    # SSH configuration
    Host *
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
