"""Test suit for HF"""
import pytest
import util

PATH = util.HF


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