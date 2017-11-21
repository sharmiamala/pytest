"""common methods for every test suit"""
import os
import sys
import hashlib

EXT_LIST=[".000",".090",".ver"]
STATIONFILES_LOC="/var/www/simulation_data/Albury/fd_rt01-h0.400.ll"
LF = "/var/www/simulation_data/Albury/LF/Albury_HYP01-01_S1244/Vel"
HF = "/var/www/simulation_data/Albury/HF/Cant1D_v2-midQ_leer_hfnp2mm+_rvf0p8_sd50_k0p045/Albury_HYP01-01_S1244/Acc"
BB_ACC = "/var/www/simulation_data/Albury/BB/Cant1D_v2-midQ_leer_hfnp2mm+_rvf0p8_sd50_k0p045/Albury_HYP01-01_S1244/Acc"
BB_VEL = "/var/www/simulation_data/Albury/BB/Cant1D_v2-midQ_leer_hfnp2mm+_rvf0p8_sd50_k0p045/Albury_HYP01-01_S1244/Vel"
SIM_PATH ="/var/www/simulation_data/Albury/"
XYTS_PATH ="/var/www/simulation_data/Albury/LF/Albury_HYP01-01_S1244/OutBin"
RLOG_PATH = "/var/www/simulation_data/Albury/LF/Albury_HYP01-01_S1244/Rlog"
NUM_RLOG_FILES = 512 # TODO: change this to take number of files from params of workflow
MARK ='/dummyVel'

def filecount(path):
    """ Counts the number of files in a directory """
    # print " \n FILECOUNT "
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1
    return count


def display_error(err_files):
    """display error msg
        err_files: a list of errors
    """
    # print "*****DISPLAYING ERRORS*****"
    err_msg=""
    if (len(err_files) != 0):
        err_msg="Failure. The error files are: \n"
        err_msg += '\n'.join(err_files)
    print err_msg


def get_stations():
    """return a list of station names in a specified directory"""
    station_names=[]
    with open(STATIONFILES_LOC) as infp:
        for line in infp:
            if line.strip():
                station_name = line.split()[-1]
                station_names.append(station_name)

    # print num_lines
    return station_names


# Methods here to test  LF, HF and BB
def test_dir_exists(path):
    """Test if a directory exist given a path"""
    # print " The directory we are looking for is : ",PATH
    # assert os.path.isdir(PATH)
    print "\n========================CHECKING IF DIR EXISTS======================== "
    if not os.path.isdir(path):
        # print "\n========================CHECKING IF DIR EXISTS======================== "
        print("{} DOES NOT EXIST".format(path))
    assert os.path.isdir(path)


def test_numoffiles(PATH):
    """check for number of files - each station has 3 files"""
    print "\n========================CHECKING NUM OF FILES========================"
    num_of_stations = len(get_stations())
    num_files = filecount(PATH)
    expected_files = num_of_stations * 3
    print "The expected number of files is {}. The number of files we got is {}. There are {} difference in the number of files".format(expected_files,num_files,num_files-expected_files)
    assert num_files == expected_files


def test_extensions(PATH):
    """checks whether there are 3 files with extensions .000, .090, .ver for each station"""
    print "\n========================CHECKING EXTENSION========================"
    err_files=[]
    prefix = ""
    if "/HF/" in PATH: # HF files are named differently from LF and BB
        prefix = "hf_"
    for station in get_stations():
        for i in range(3):
            name = prefix+station+EXT_LIST[i]
            # print("name is ", name)
            # print("join is", os.path.join(LF, name))
            if not os.path.isfile(os.path.join(PATH, name)):
                err_files.append(os.path.join(PATH, name))
    display_error(err_files)
    assert len(err_files) == 0


def test_check_size(PATH):
    """check if each file has the same size"""
    print "\n========================CHECKING FILE SIZE======================== "
    err_files = []
    size_set=set()
    names = os.listdir(PATH)
    # paths = [os.path.join(test_data, name) for name in names]
    # sizes = [(os.stat(path).st_size) for path in paths]
    pre_len = 1
    for name in names:
        path=os.path.join(PATH, name)
        size = (os.stat(path)).st_size
        size_set.add(size)
        post_len=(len(size_set))
        if pre_len != post_len:
            err_files.append(path)
            pre_len = post_len
    # print "sssssssssssssss",size_set
    display_error(err_files)
    assert len(size_set)==1


# TODO: change to accommodate the path_benchmark
def test_checksum(PATH):
    """check if the output file has the same hash value as the corresponding benchmark file"""
    print "\n========================COMPARING FILE CHECKSUM======================== "
    # err_files = []
    path_benchmark=PATH+MARK
    # print "path_benchmark >>>> ",path_benchmark
    test_dir_exists(path_benchmark)

    for f in os.listdir(PATH):
        actual_path=os.path.join(PATH,f)

        if os.path.isfile(actual_path):
            hash1 = hashlib.md5(open(actual_path, 'rb').read()).hexdigest()
        else:
            hash1='file does not exist'.format(actual_path)
            # err_files.append("actual path doesnt exists".format(actual_path))
        exp_name =os.path.join(path_benchmark, f)
        if os.path.isfile(exp_name):
            hash2= hashlib.md5(open(exp_name, 'rb').read()).hexdigest()
        else:
            hash2='file does not exist'.format(exp_name)
        #     err_files.append("expected path doesnt exists".format(exp_name))
        # util.display_error(err_files)
        assert hash1 == hash2
    #     if hash1 != hash2:
    #         err_files.append(actual_path)
    #
    # util.display_error(err_files)
    # assert len(err_files) == 0