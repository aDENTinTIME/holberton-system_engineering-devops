# Sets the env
exec { '/etc/apache2/envvars':
  command => 'source /etc/apache2/envvars'
}
