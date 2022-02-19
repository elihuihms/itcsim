import os
import zipfile

from itcsimlib.utilities import *

from . import TestITCBase


class TestITCUtilities(TestITCBase):
	def test_rw_params_to_file(self):
		params = {'n':1.80546,'dG':-10.9522,'dH':-12.4281,'dCp':0.0}
		write_params_to_file( self.getFilePath(True), params )
		self.assertEqual( params, read_params_from_file( self.getFilePath() ) )

class TestITCConvertors(TestITCBase):
	def test_rw_experiment_file(self):
		E1 = read_itcsimlib_exp(self.get_data("utilities_1.txt"))
		write_itcsimlib_pickle( self.getFilePath(True), E1 )
		E2 = read_itcsimlib_pickle( self.getFilePath() )
		self.assertEqual( E1.npoints, E2.npoints ) 

	def test_read_nitpic(self):
		with zipfile.ZipFile( self.get_data("utilities_4.zip") ) as archive:
			archive.extractall(self.test_dir)
		E = read_nitpic_exp(self.get_data(os.path.join(self.test_dir, "ca-edta_tris-01.sedphat")))
		self.assertEqual( round(sum(E.dQ_exp),1), -6367.2 )

	def test_read_nitpikl(self):
		with zipfile.ZipFile( self.get_data("utilities_4.zip") ) as archive:
			archive.extractall(self.test_dir)
		E = read_nitpikl_exp(self.get_data(os.path.join(self.test_dir, "ca-edta_tris-01.sedphat", "ca-edta_tris-01.nitpkl")))
		self.assertEqual( round(sum(E.dQ_exp),1), -6367.2 )
		E = read_nitpikl_exp(self.get_data("utilities_2.nitpkl"))
		self.assertEqual( round(sum(E.dQ_exp),1), -831.3 )

	def test_read_origin(self):
		E = read_origin_exp(self.get_data("utilities_3.dh"))
		self.assertEqual( round(sum(E.dQ_exp),1), -2897.4 )