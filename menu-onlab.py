import netaddr
import os
import fileinput

os.system('clear')


def choice_sub_menu():
    print("""
1. Proceed
2. Change
3. Go back
            """)

def external_iface_select():
    print("""
1. Enter External_Iface
2. Go back
                           """)

def  management_iface_select():
    print("""
1. Enter Management_Iface
2. Go back
                       """)

def external_ip_select():
    print("""
1. Enter External ip
2. Go back
                    """)

def mgmnt_ip_select():
    print("""
1. Enter Management ip
2. Go back
                 """)

def fabric_ip_select():
    print("""
1. Enter Fabric ip
2. Go back
                 """)

def seed_select():
    print("""
 1. Enter Seed ip
 2. Go back
                  """)


def main_select():
    print("""
1.Customize Pod Config File
2.Quit
      """)

def commit_select():
    print("""
1.Commit Modifications To Pod Config File
2.Restart
      """)


def pod_rules():

        config_path = (os.getcwd() + "/cord/config/")
        print ('''
=================================================================
You'll need to customize POD deployment
by updating the \"onlab_develop_pod.yml\" config file.

You're welcome to do so interactively or
Just \"Quit\" and manually update...

Location: %s

Please re-run main setup script if manual update
is chosen.
=================================================================
           ''') % config_path


def seed_action():
    is_valid = 0
    while not is_valid:
        try:

            seed_action.seedip = raw_input("Enter SeedServer ip: ")
            netaddr.ip.IPAddress(seed_action.seedip)
            is_valid = 1
        except netaddr.core.AddrFormatError:
            print 'Invalid IP Address Format, please try again!'
        else:
            print '\nYou Entered... %s' % seed_action.seedip
            is_valid = 0

            while not is_valid:
                try:
                    choice_sub_menu()
                    choice = int(raw_input('Enter your choice [1-3] : '))
                    is_valid = 1
                except:
                    print 'Invalid input...'

            if choice == 1:
                print '\nProceeding with Fabric ip...\n'
                fabric_ip_choice()

            elif choice == 2:
                seed_action()

            elif choice == 3:
                seed_choice()

            elif choice > 3:
                print 'Selection out of range: %d' % choice
                is_valid = 0
                seed_action()

            elif choice > 3:
                print 'Selection out of range: %d' % choice
                is_valid = 0
                seed_action()


def seed_choice():
    seed = 'SeedServer ip'
    is_valid = 0
    while not is_valid:
        try:
            seed_select()
            choice = int(raw_input('Enter your choice [1-2] : '))
            is_valid = 1

        except:
            print 'Invalid input, selection of of range!'
        else:

            if choice == 1:
                seed_action()

            elif choice == 2:
                onlab_menu()

            elif choice > 2:
                print 'Selection out of range: %d' % choice
                is_valid = 0
                seed_choice()


def fabric_ip_action():
    is_valid = 0

    while not is_valid:
        try:
            fabric_ip_action.fabric_ip = raw_input("Enter Frabric ip: ")
            netaddr.IPNetwork(fabric_ip_action.fabric_ip)
            is_valid = 0
        except netaddr.core.AddrFormatError:
            print 'Invalid Network Format, please try again!'
        else:
            print '\nYou Entered... %s' % fabric_ip_action.fabric_ip
            is_valid = 0

            while not is_valid:
                try:
                    choice_sub_menu()
                    choice = int(raw_input('Enter your choice [1-3] : '))
                    is_valid = 1
                except:
                    print 'Invalid input...'

            if choice == 1:
                print '\nProceeding with Management ip...\n'
                mgmnt_ip_choice()

            elif choice == 2:
                fabric_ip_action()

            elif choice == 3:
                fabric_ip_choice()

            elif choice > 3:
                print 'Selection out of range: %d' % choice
                is_valid = 0
                fabric_ip_action()

def fabric_ip_choice():
    is_valid = 0
    while not is_valid:
        try:
            fabric_ip_select()
            choice = int(raw_input('Enter your choice [1-2] : '))
            is_valid = 1

        except:
            print 'Invalid input...'
        else:

            if choice == 1:
                fabric_ip_action()

            elif choice == 2:
                seed_choice()

            elif choice > 2:
                print 'Selection out of range: %d' % choice
                is_valid = 0


def mgmnt_ip_action():
    is_valid = 0
    while not is_valid:

        try:
            mgmnt_ip_action.mgmnt_ip = raw_input("Enter Management ip: ")
            netaddr.IPNetwork(mgmnt_ip_action.mgmnt_ip)
            is_valid = 1
        except netaddr.core.AddrFormatError:
            print 'Invalid Network Format, please try again!'
        else:
            print '\nYou Entered... %s' % mgmnt_ip_action.mgmnt_ip
            is_valid = 0

        while not is_valid:
            try:
                choice_sub_menu()
                choice = int(raw_input('Enter your choice [1-3] : '))
                is_valid = 1
            except:
                print 'Invalid input...'

            if choice == 1:
                print '\nProceeding with External ip...\n'
                external_ip_choice()

            elif choice == 2:
                mgmnt_ip_action()

            elif choice == 3:
                mgmnt_ip_choice()

            elif choice > 3:
                print 'Selection out of range: %d' % choice
                is_valid = 0
                mgmnt_ip_action()


def mgmnt_ip_choice():
    is_valid = 0
    while not is_valid:
        try:
            mgmnt_ip_select()
            choice = int(raw_input('Enter your choice [1-2] : '))
            is_valid = 1

        except:
            print 'Invalid input...'
        else:

            if choice == 1:
                mgmnt_ip_action()

            elif choice == 2:
                fabric_ip_choice()

            elif choice > 2:
                print 'Selection out of range: %d' % choice
                is_valid = 0



def external_ip_action():
    is_valid = 0
    while not is_valid:

        try:
            external_ip_action.external_ip = raw_input("Enter External ip: ")
            netaddr.IPNetwork(external_ip_action.external_ip)
            is_valid = 1
        except netaddr.core.AddrFormatError:
            print 'Invalid Network Format, please try again!'
        else:
            print '\nYou Entered... %s' % external_ip_action.external_ip
            is_valid = 0

            while not is_valid:
                try:
                    choice_sub_menu()
                    choice = int(raw_input('Enter your choice [1-3] : '))
                    is_valid = 1
                except:
                    print 'Invalid input...'

                if choice == 1:
                    print '\nProceeding with Management_Iface...\n'
                    management_iface_choice()

                elif choice == 2:
                    external_ip_action()

                elif choice == 3:
                    external_ip_choice()

                elif choice > 3:
                    print 'Selection out of range: %d' % choice
                    is_valid = 0
                    external_ip_action()

                elif choice > 3:
                    print 'Selection out of range: %d' % choice
                    is_valid = 0
                    external_ip_action()


def external_ip_choice():
    is_valid = 0
    while not is_valid:
        try:
            external_ip_select()
            choice = int(raw_input('Enter your choice [1-2] : '))
            is_valid = 1

        except:
            print 'Invalid input...'
        else:

            if choice == 1:
                external_ip_action()

            elif choice == 2:
                mgmnt_ip_choice()

            elif choice > 2:
                print 'Selection out of range: %d' % choice
                is_valid = 0
                external_ip_choice()



def management_iface_action():
    #is_valid = 0
    while True:
        management_iface_action.mgmt_iface = raw_input("Enter Management Iface: ")
        try:
            val = management_iface_action.mgmt_iface
            len(val) > 10
        except ValueError:
            print 'Invalid -- 10 Character Limit!'
        else:
            print '\nYou Entered... %s' % management_iface_action.mgmt_iface
            break

    is_valid = 0
    while not is_valid:
        try:
            choice_sub_menu()
            choice = int(raw_input('Enter your choice [1-3] : '))
            is_valid = 1
        except:
            print 'Invalid input...'
        else:
            if choice == 1:
                print '\nProceeding with External_iface...\n'
                external_iface_choice()

            elif choice == 2:
                management_iface_action()

            elif choice == 3:
                management_iface_choice()

            elif choice > 3:
                print 'Selection out of range: %d' % choice
                is_valid = 0


def management_iface_choice():
    is_valid = 0
    while not is_valid:
        try:
            management_iface_select()
            choice = int(raw_input('Enter your choice [1-2] : '))
            is_valid = 1

        except:
            print 'Invalid input...'
        else:

            if choice == 1:
                management_iface_action()

            elif choice == 2:
                external_ip_choice()

            elif choice > 2:
                print 'Selection out of range: %d' % choice
                is_valid = 0


def external_iface_action():
    #is_valid = 0
    while True:
        external_iface_action.ext_iface = raw_input("Enter External Iface: ")
        try:
            val = external_iface_action.ext_iface
            len(val) > 10
        except ValueError:
            print 'Invalid -- 10 Character Limit!'
        else:
            print '\nYou Entered... %s' % external_iface_action.ext_iface
            break

    is_valid = 0
    while not is_valid:
        try:
            choice_sub_menu()
            choice = int(raw_input('Enter your choice [1-3] : '))

        except:
            print 'Invalid input...'
        else:
            is_valid = 1
            if choice == 1:
                print '\nCommit Settings....\n'
                end_result()
            elif choice == 2:
                external_iface_action()
            elif choice == 3:
                management_iface_choice()
            elif choice > 3:
                print 'Selection out of range: %d' % choice
                is_valid = 0


def external_iface_choice():
    is_valid = 0
    while not is_valid:
        try:
            external_iface_select()
            choice = int(raw_input('Enter your choice [1-2] : '))
            is_valid = 1

        except:
            print 'Invalid input...'
        else:

            if choice == 1:
                external_iface_action()

            elif choice == 2:
                management_iface_choice()

            elif choice > 2:
                print 'Selection out of range: %d' % choice
                is_valid = 0



def onlab_update_config():
    myconfig = 'onlab_develop_pod.yml'

    rep = {'myseedip':'%s' % seed_action.seedip,
           'myfrabricip':'%s' % fabric_ip_action.fabric_ip,
           'mymanip':'%s' % mgmnt_ip_action.mgmnt_ip,
           'myextip':'%s' % external_ip_action.external_ip,
           'mymaniface':'%s' % management_iface_action.mgmt_iface,
           'myextiface':'%s' % external_iface_action.ext_iface}

    with open(myconfig, 'r+') as fd:

        # read in all the data
        text = fd.read()

        fd.seek(0)
        fd.truncate()

        for key in rep.keys():
            text = text.replace(key, rep[key])

        fd.write(text)


def onlab_menu():
    is_valid = 0
    pod_rules()
    while not is_valid:
        try:
            main_select()
            choice = int(raw_input('Enter your choice [1-2] : '))
            is_valid = 1
        except:
            print 'Invalid input...'
        else:
            if choice > 2:
                print 'Selection out of range: %d' % choice
                is_valid = 0

    if choice == 1:
        seed_choice()
    elif choice == 2:
        raise SystemExit


def end_result():
    print """
Current Network Settings...
-----------------------------------------
Seed Server IP:     %s

fabric_ip:          %s

management_ip:      %s

external_ip:        %s

management_iface:   %s

external_iface:     %s
-----------------------------------------
    """ % (
        seed_action.seedip,
        fabric_ip_action.fabric_ip,
        mgmnt_ip_action.mgmnt_ip,
        external_ip_action.external_ip,
        management_iface_action.mgmt_iface,
        external_iface_action.ext_iface
          )

    is_valid = 0
    while not is_valid:
        try:
            commit_select()
            choice = int(raw_input('Enter your choice [1-2] : '))
            is_valid = 1
        except:
            print 'Invalid input...'
        else:
            if choice > 2:
                print 'Selection out of range: %d' % choice
                is_valid = 0
            elif choice == 1:
                print 'writing to onlab file...'
                onlab_update_config()
            elif choice == 2:
                onlab_menu()



if __name__=='main':
    onlab_menu()
