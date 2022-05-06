# config file nging debugin 4

exec { 'this will output stuff':
  path    => '/bin',
  command => 'echo "ULIMIT=\"-n 25000\"" > /etc/default/nginx;  sudo service nginx restart',
}