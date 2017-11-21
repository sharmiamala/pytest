# """Test suit for post_emod3d"""
import pytest
import os
import glob
import util
import qcore.xyts as xyts

PATH = util.LF


def test_dir_exists():
    util.test_dir_exists(PATH)


def test_numoffiles():
    util.test_numoffiles(PATH)


def test_extensions():
    util.test_extensions(PATH)


def test_check_size():
    util.test_check_size(PATH)


def test_checksum():
    util.test_checksum(PATH)


def test_xyts_presence():
    """check the presence of summary xyts"""
    print "\n========================CHECKING XYTS.E3D FILE ========================"
    pattern="*"+'xyts.e3d'
    xyts = glob.glob1(util.XYTS_PATH,pattern)
    # print "xxxxxxx",xyts
    if len(xyts)!=1:
        print "Summary xyts file not present"
    assert len(xyts)==1


def test_xyts_integrity():
    """check if the actual xyts size is as expected"""
    print "\n========================CHECKING XYTS INTEGRITY ========================"
    pattern = "*" + 'xyts.e3d'
    xyts_filename = glob.glob1(util.XYTS_PATH, pattern)
    # print "xxxxxxx",xyts_filename
    filename=xyts_filename[0]
    f=xyts.XYTSFile(os.path.join(util.XYTS_PATH,filename))
    # print "fnx ",f.nx
    # print "fny ",f.ny
    # print "fnt ",f.nt
    expected_size=(f.nx*f.ny*f.nt*3*4) +60
    assert expected_size == (os.stat(os.path.join(util.XYTS_PATH,filename))).st_size

