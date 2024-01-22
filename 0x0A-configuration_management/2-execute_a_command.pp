# A manifest that kills a process
exec { 'kill_killmenow_process':
  command => '/usr/bin/pkill killnow',
  onlyif  => '/usr/bin/pgrep killnow',
}
