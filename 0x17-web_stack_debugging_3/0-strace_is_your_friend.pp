# This Puppet manifest automates the fix for Apache 500 Internal Server Error

# Ensure the Apache service is running
service { 'apache2':
  ensure => running,
  enable => true,
}

# Ensure necessary packages are installed
package { ['libapache2-mod-php5', 'php5', 'php5-mysql']:
  ensure => installed,
}

# Fix file permissions for Apache
file { '/var/www/html/wp-content':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  recurse => true,
}

# Restart Apache service to apply changes
exec { 'restart_apache':
  command     => '/etc/init.d/apache2 restart',
  refreshonly => true,
  subscribe   => File['/var/www/html/wp-content'],
}

