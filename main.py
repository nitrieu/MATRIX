import os
import colorama
from Deployment import deploy as de
from Deployment import aws_deploy as awsde
from Deployment import scaleway_deploy as sde
from Execution import end_to_end as e2e
from Reporting import analyze_results as ar
from Reporting import upload_elastic as ue

d = {'blue': colorama.Fore.BLUE,
     'green': colorama.Fore.GREEN,
     'yellow': colorama.Fore.YELLOW,
     'red': colorama.Fore.RED,
     'magenta': colorama.Fore.MAGENTA}


def color_print(text, color):
    c = d[color]
    print('{}{}'.format(c, text))


def print_main_menu():
    color_print('Welcome to MATRIX system.\nPlease Insert your choice:', 'blue')
    color_print('1. Deploy Menu', 'blue')
    color_print('2. Execute Menu', 'blue')
    color_print('3. Analysis Menu', 'blue')
    color_print('4. Generate Circuits', 'blue')
    color_print('5. Exit', 'blue')
    selection = input('Your choice:')
    return selection


def print_instances_management_menu(conf_file_path):
    color_print('Choose cloud provider:', 'blue')
    color_print('1. AWS', 'blue')
    color_print('2. Scaleway', 'blue')
    
    cp = input('Your choice:')
    if cp == '1':
        color_print('Choose deployment task', 'red')
        color_print('1. Deploy Instance(s)', 'red')
        color_print('2. Create Key pair(s)', 'red')
        color_print('3. Create security group(s)', 'red')
        color_print('4. Get instances network data', 'red')
        color_print('5. Terminate machines', 'red')
        color_print('6. Change machines types', 'red')
        color_print('7. Start instances ', 'red')
        color_print('8. Stop instances', 'red')
        selection = input('Your choice:')
    
        deploy = awsde.AmazonCP(conf_file_path)
    
        if selection == '1':
            deploy.deploy_instances()
        elif selection == '2':
            deploy.create_key_pair()
        elif selection == '3':
            deploy.create_security_group()
        elif selection == '4':
            deploy.get_network_details()
        elif selection == '5':
            deploy.terminate()
        elif selection == '6':
            deploy.change_instance_types()
        elif selection == '7':
            deploy.start_instances()
        elif selection == '8':
            deploy.stop_instances()
    
    elif cp == '2':
        color_print('Choose deployment task', 'magenta')
        color_print('1. Deploy Instance(s)', 'magenta')
        color_print('2. Create Key pair(s)', 'magenta')
        color_print('3. Create security group(s)', 'magenta')
        color_print('4. Get instances network data', 'magenta')
        color_print('5. Terminate machines', 'magenta')
        color_print('6. Change machines types', 'magenta')
        color_print('7. Start instances ', 'magenta')
        color_print('8. Stop instances', 'magenta')
        selection = input('Your choice:')

        deploy = sde.ScalewayCP(conf_file_path)
        if selection == '1':
            deploy.deploy_instances()
        elif selection == '2':
            deploy.create_key_pair()
        elif selection == '3':
            deploy.create_security_group()
        elif selection == '4':
            deploy.get_network_details()
        elif selection == '5':
            deploy.terminate()
        elif selection == '6':
            deploy.change_instance_types()
        elif selection == '7':
            deploy.start_instances()
        elif selection == '8':
            deploy.stop_instances()


def print_execution_menu(conf_file_path):
    color_print('Choose task to be executed:', 'yellow')
    color_print('1. Preform pre process operations', 'yellow')
    color_print('2. Install Experiment', 'yellow')
    color_print('3. Execute Experiment', 'yellow')
    color_print('4. Update libscapi', 'yellow')
    selection = input('Your choice:')

    ee = e2e.E2E(conf_file_path)

    if selection == '1':
        ee.pre_process()
    elif selection == '2':
        ee.install_experiment()
    elif selection == '3':
        ee.execute_experiment()
    elif selection == '4':
        ee.update_libscapi()


def print_analysis_menu(conf_file_path):
    color_print('Choose analysis task to be executed:', 'green')
    color_print('1. Download & Analyze Results', 'green')
    color_print('2. Download Results', 'green')
    color_print('3. Analyze Results', 'green')
    color_print('4. Upload data to Elasticsearch', 'green')
    selection = input('Your choice:')

    a = ar.Analyze(conf_file_path)

    if selection == '1':
        a.download_data()
        a.analyze_all()
    elif selection == '2':
        a.download_data()
    elif selection == '3':
        a.analyze_all()
    elif selection == '4':
        e = ue.Elastic(conf_file_path)
        e.upload_all_data()


def main():
    selection = print_main_menu()

    while not selection == '5':
        if int(selection) > 5:
            print('Choose valid option!')
            selection = print_main_menu()
            continue

        if selection == '4':
            de.DeployCP.generate_circuits()
        else:
            color_print('Enter configuration file(s):', 'blue')
            conf_file_path = input('Configuration file path (current path is: %s): ' % os.getcwd())

            if selection == '1':
                print_instances_management_menu(conf_file_path)

            elif selection == '2':
                print_execution_menu(conf_file_path)

            elif selection == '3':
                print_analysis_menu(conf_file_path)

        selection = print_main_menu()


if __name__ == '__main__':
    main()
