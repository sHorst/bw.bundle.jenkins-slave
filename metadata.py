defaults = {}

if node.has_bundle("iptables"):
    defaults += (repo.libs.iptables.accept()
                 .chain('INPUT')
                 .input('vboxnet0')
                 .state('NEW,RELATED,ESTABLISHED'))

    defaults += (repo.libs.iptables.accept()
                 .chain('OUTPUT')
                 .output('vboxnet0')
                 .state('NEW,RELATED,ESTABLISHED'))
