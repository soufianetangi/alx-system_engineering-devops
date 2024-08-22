# Puppet manifest to optimize Nginx configuration for handling high amount of requests

exec { 'replace':
  provider => shell,
  command  => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['restart'],
}

exec { 'restart':
  provider => shell,
  command  => 'service nginx restart',
}

