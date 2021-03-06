from __future__ import annotations

from local_data_api.resources import PostgresSQL


def test_create_connection_maker(mocker):
    mock_connect = mocker.patch('local_data_api.resources.postgres.psycopg2.connect')
    connection_maker = PostgresSQL.create_connection_maker(
        host='127.0.0.1',
        port=3306,
        user_name='root',
        password='pass',
        engine_kwargs={'auto_commit': True},
    )
    connection_maker(database='test')
    mock_connect.assert_called_once_with(
        auto_commit=True,
        host='127.0.0.1',
        password='pass',
        port=3306,
        user='root',
        dbname='test',
    )

    mock_connect = mocker.patch('local_data_api.resources.postgres.psycopg2.connect')
    connection_maker = PostgresSQL.create_connection_maker()
    connection_maker()
    mock_connect.assert_called_once_with()
