# A manifest that kills a process
exec { 'kill_killmenow_process':
  command => 'pkill -9 -f killmenow',
  path    => ['/usr/bin', '/bin', '/usr/sbin'],
}
