"""Test suite for rlog files"""
import os
import util
import pytest

PATH = util.RLOG_PATH

# def setup_module(module):
#     """ setup any state specific to the execution of the given module."""
#     print "setup"
#
# # @pytest.mark.first
# # def test_dir_exists():
# #     assert os.path.isdir(PATH)
#
# def teardown_module(module):
#     """ teardown any state that was previously setup with a setup_module
#     method.
#     """
#     print "tear down"

def test_dir_exists():
    util.test_dir_exists(PATH)



def test_num_rlog():
    """check if the total number of rlog files is equal to the expected number """
    print "\n========================CHECKING NUMBER OF RLOGS========================"
    result=util.filecount(PATH)
    assert result == util.NUM_RLOG_FILES


def test_file_completion():
    """check if every rlog program is succcessfully finished"""
    print "\n========================CHECKING FILE COMPLETION========================"
    filelist = os.listdir(PATH)
    err_files = []
    for f in filelist:
        if os.path.isfile(os.path.join(PATH, f)):
            file = os.path.join(PATH, f)
            with open(file, "r") as f1:
                last_line = f1.readlines()[-1]
                if last_line.strip() != "PROGRAM emod3d-mpi IS FINISHED":
                    err_files.append(file)

    util.display_error(err_files)
    assert len(err_files) == 0




# def display_success(filename):

# fixture example to iterate list of files
# @pytest.fixture(params=filelist.__iter__())
# def get_file_list(request):
#     return request.param
#
# def test_file_completion(get_file_list):
#     if os.path.isfile(os.path.join(path, get_file_list)):
#         file=os.path.join(path, get_file_list)
#         result = stringmatch(file)
#         assert result.strip() == "PROGRAM emod3d-mpi IS FINISHED"



# from:http://pythontesting.net/framework/pytest/pytest-fixtures-nuts-bolts/
# @pytest.fixture(params=[1,2,3])
# def test_data(request):
#     return request.param
#
# def test_not_2(test_data):
#     print('test_data: %s' % test_data)
#     assert test_data != 2