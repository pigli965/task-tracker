import click
import task_tracker


@click.group()
def tracker():
    """
    Tracker task tracker tool
    """
    pass


@tracker.command('add',short_help='Add your task', type=any)
def add( **kwargs):  
    task=click.prompt('Please add your task')
    task_tracker.write_json(task)
    
    
@tracker.command('update',short_help="Update status of your task")
def update( **kwargs):
    print('update')

@tracker.command('delete',short_help="Delete your task")
def delete( **kwargs):
    print('delete')

@tracker.command('status',short_help="Check your task status")
def status( **kwargs):
    print('status')


if __name__ == '__main__':
    tracker()



    