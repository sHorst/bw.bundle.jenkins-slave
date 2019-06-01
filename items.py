from os.path import join
from bundlewrap.utils import get_file_contents

users = {
    'jenkins': {
        'password_hash': '*',
        'home': '/var/lib/jenkins',
        'shell': '/bin/bash',
    }
}

directories = {
    '/var/lib/jenkins': {
        'owner': 'jenkins',
        'group': 'jenkins',
        'mode': '0755'
    },
    '/var/lib/jenkins/.ssh': {
        'owner': 'jenkins',
        'group': 'jenkins',
        'mode': '0700'
    }
}

files = {
    '/var/lib/jenkins/.ssh/authorized_keys': {
        # TODO: configure this file
        'content': get_file_contents(join(repo.data_dir, 'jenkins', 'id_ed25519.pub')),
        'owner': 'jenkins',
        'group': 'jenkins',
        'mode': '0400'
    },
    '/var/lib/jenkins/.ssh/id_ed25519.pub': {
        'content': get_file_contents(join(repo.data_dir, 'jenkins', '{}_id_ed25519.pub'.format(node.name))),
        'owner': 'jenkins',
        'group': 'jenkins',
        'mode': '0400'
    },
    '/var/lib/jenkins/.ssh/id_ed25519': {
        'content': repo.vault.decrypt_file(join('jenkins', '{}_id_ed25519'.format(node.name))),
        'owner': 'jenkins',
        'group': 'jenkins',
        'mode': '0400'
    },
    '/etc/sudoers.d/jenkins': {
        'content': 'jenkins ALL=NOPASSWD: /usr/bin/docker,/usr/local/bin/docker-compose,/bin/chown\n',
        'mode': '0440'
    },
}


