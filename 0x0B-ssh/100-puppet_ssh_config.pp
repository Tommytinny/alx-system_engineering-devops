exec { 'set-private-key':
  command => 'echo "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
  path    => ['/bin', '/usr/bin'],
}

exec { 'disable-password':
  command => 'echo "PasswordAuthentication no" >> /etc/ssh/ssh_config',
  path    => ['/bin', '/usr/bin'],
}
