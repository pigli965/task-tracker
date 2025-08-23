import click

task_tracker={}

@click.group()
def cli():
    """
    Tracker task CLI tool
    """
    pass


@cli.command('add',short_help='Add your task')

def add():  

    task=input("Enter your task:")
    # task_tracker.update({task})

@cli.command('update',short_help="Update status of your task")
def update():
    print('update')

@cli.command('delete',short_help="Delete your task")
def delete():
    print('delete')

@cli.command('status',short_help="Check your task status")
def status():
    print('status')



if __name__ == '__main__':
    cli()



    