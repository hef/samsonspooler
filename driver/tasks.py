from celery import task
import driver


@task()
def print_s3g(file):
    printer = driver.ReplicatorDriver()
    printer.connect()
    printer.print_file(file)
