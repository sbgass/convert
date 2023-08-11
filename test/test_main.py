from convert.main import cli 

def test_cli():
    res = cli()
    assert res is None 