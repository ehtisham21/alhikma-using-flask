import os


class DatabaseCredentials(object):
    db_name = os.environ.get('MYSQL_DATABASE', 'alhikmaflaskapplication')
    db_user = os.environ.get('MYSQL_USER', 'root')
    db_password = os.environ.get('MYSQL_PASSWORD', '')
    db_root_password = os.environ.get('MYSQL_ROOT_PASSWORD', 'root')
    container_name = os.environ.get('container_name', 'localhost')

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{db_user}:{db_password}@{container_name}/{db_name}'