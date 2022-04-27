# Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.
exec {'apt-get-update':
  command => '/usr/bin/apt-get -y update',
}

package {'nginx':
  ensure  => installed,
  require => Exec[apt-get-update],
}

file_line { 'a':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  require => Package['nginx'],
}

file_inline {'b':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'add_header X-Served-By $HOSTNAME;'
  require => Package['nginx'],
}

file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World',
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
