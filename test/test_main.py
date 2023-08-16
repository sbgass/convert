import os 
from unittest.mock import patch, call
import tempfile 
from pathlib import Path 
import pytest 
import shutil

import generate_test_data

from convert.main import convert_all_parquet_files, create_csv_copy


DATA_DIR = Path(__file__).parent / "data"

@pytest.fixture(scope="class")
def create_temp_dir(request):

    with tempfile.TemporaryDirectory() as tmpdir:
        open(os.path.join(tmpdir,"a.parquet"),'a').close() 
        open(os.path.join(tmpdir,"b.parquet"),'a').close()
        open(os.path.join(tmpdir,"c.txt"),'a').close()
        open(os.path.join(tmpdir,"a.json"),'a').close()
        os.makedirs(os.path.join(tmpdir, "subdir"))
        open(os.path.join(tmpdir, "subdir","c.parquet"),'a').close()
        request.cls.tmpdir = Path(tmpdir)
        yield 


@pytest.mark.usefixtures("create_temp_dir")
class TestIteration:
    @patch("convert.main.create_csv_copy")
    def test_convert_all_parquet_files(self, mock_convert):
        convert_all_parquet_files(self.tmpdir)
        assert mock_convert.call_count == 3
        calls = [call(self.tmpdir / "a.parquet"), call(self.tmpdir / "b.parquet"), call(self.tmpdir / "subdir"/ "c.parquet")]
        mock_convert.assert_has_calls(calls)
        


@pytest.fixture(scope="class")
def stage_test_data(request):

    with tempfile.TemporaryDirectory() as tmpdir:
        src_data = DATA_DIR / "data.parquet"
        dst_data = Path(tmpdir) / "data.parquet"
        shutil.copy(src_data, dst_data)
        request.cls.data_path = dst_data
        yield 


@pytest.mark.usefixtures("stage_test_data")
class TestCsvCopy:
    def test_create_csv_copy(self): 
        create_csv_copy(self.data_path) 

        # Assert 
        resulting_files = list(self.data_path.parent.iterdir())
        assert len(resulting_files) == 2, "CSV copy was not created correctly"
        assert self.data_path in resulting_files, "Expected parquet file to be in output directory"
        resulting_files.pop(resulting_files.index(self.data_path))
        assert resulting_files[0] == self.data_path.with_suffix(".csv")
        