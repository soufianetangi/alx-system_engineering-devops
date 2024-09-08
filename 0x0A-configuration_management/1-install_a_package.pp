# Puppet manifest to install Flask 2.1.0 and Werkzeug 2.0.3

# Ensure pip3 is installed
package { 'python3-pip':
  ensure => installed,
}

# Install Flask 2.1.0
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Install Werkzeug 2.0.3 (compatible with Flask 2.1.0)
package { 'Werkzeug':
  ensure   => '2.0.3',
  provider => 'pip3',
}
