@metadata_processor
def add_iptables_rule(metadata):
    if node.has_bundle("iptables"):
        metadata += (repo.libs.iptables.accept()
                     .chain('INPUT')
                     .input('vboxnet0')
                     .state('NEW,RELATED,ESTABLISHED'))

        metadata += (repo.libs.iptables.accept()
                     .chain('OUTPUT')
                     .output('vboxnet0')
                     .state('NEW,RELATED,ESTABLISHED'))

    return metadata, DONE
