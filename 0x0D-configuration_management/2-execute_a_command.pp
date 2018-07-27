# Kills a process

exec { 'pkill killmenow':
  unless => 'pgrep killmenow',
}
