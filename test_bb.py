"""Test suit for BB"""
import pytest
import util

"""Tests for BB Vel"""

def test_bbvel_dir_exists():
    util.test_dir_exists(util.BB_VEL)


def test_bbvel_numoffiles():
    util.test_numoffiles(util.BB_VEL)


def test_bbvel_extensions():
    util.test_extensions(util.BB_VEL)


def test_bbvel_check_size():
    util.test_check_size(util.BB_VEL)


def test_bbvel_checksum():
    util.test_checksum(util.BB_VEL)


"""Tests for BB Acc"""

def test_bbacc_dir_exists():
    util.test_dir_exists(util.BB_ACC)


def test_bbacc_numoffiles():
    util.test_numoffiles(util.BB_ACC)


def test_bbacc_extensions():
    util.test_extensions(util.BB_ACC)


def test_bbacc_check_size():
    util.test_check_size(util.BB_ACC)


def test_bbacc_checksum():
    util.test_checksum(util.BB_ACC)