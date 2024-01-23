#  SSH client configuration to use the private key ~/.ssh/school
exec { 'set-private-key':
  command => 'echo "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
  path    => ['/bin', '/usr/bin'],
}

# SSH client configuration to refuse to authenticate using a password
exec { 'disable-password':
  command => 'echo "PasswordAuthentication no" >> /etc/ssh/ssh_config',
  path    => ['/bin', '/usr/bin'],
}
