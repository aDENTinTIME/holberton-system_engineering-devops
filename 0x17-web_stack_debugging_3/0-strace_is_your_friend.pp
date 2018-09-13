# Sets the env
exec { 'set env':
  command => 'source /etc/apache2/envvars'
}
