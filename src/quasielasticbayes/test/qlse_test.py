"""Characterization tests for QLres module"""
import os.path
import platform
import unittest
import numpy as np
import sys
import tempfile

from quasielasticbayes.testing import add_path, load_json, RELATIVE_TOLERANCE_FIT, RELATIVE_TOLERANCE_PROB
from quasielasticbayes.QLse import qlstexp

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')


class QLresTest(unittest.TestCase):
    """
    Characterization tests using inputs that have been accepted as correct.
    The output is based on running BayesQuasi algorithm in mantid 6.2
    with the inputs taken from the BayesQuasiTest unit test
    """

    def test_qlres_minimal_input(self):
        with open(os.path.join(DATA_DIR, 'qlse', 'qlse_input.json'), 'r') as fh:
            inputs = load_json(fh)

        with tempfile.TemporaryDirectory() as tmp_dir:
            inputs['wrks'] = add_path(tmp_dir, inputs['wrks'])

            nd, xout, yout, eout, yfit, yprob = qlstexp(inputs['numb'],
                                                      inputs['Xv'],
                                                      inputs['Yv'],
                                                      inputs['Ev'],
                                                      inputs['reals'],
                                                      inputs['fitOp'],
                                                      inputs['Xdat'],
                                                      inputs['Xb'],
                                                      inputs['Yb'],
                                                      inputs['Wy'],
                                                      inputs['We'],
                                                      inputs['dtn'],
                                                      inputs['xsc'],
                                                      inputs['wrks'],
                                                      inputs['wrkr'],
                                                      inputs['lwrk'])

            # verify
            with open(os.path.join(DATA_DIR, 'qlse', 'qlse_output.json'), 'r') as fh:
                reference = load_json(fh)

            self.assertEqual(reference['nd'], nd)
            np.testing.assert_allclose(reference['xout'], xout)
            np.testing.assert_allclose(reference['yout'], yout)
            np.testing.assert_allclose(reference['eout'], eout)
            if sys.platform == "linux":
                np.testing.assert_allclose(reference['yfit'], yfit, rtol=0.015)
            elif sys.platform == "darwin" and platform.machine().lower() == "arm64":
                np.testing.assert_allclose(reference['yfit'], yfit, rtol=0.01)
            else:
                np.testing.assert_allclose(reference['yfit'], yfit, rtol=RELATIVE_TOLERANCE_FIT)
            np.testing.assert_allclose(reference['yprob'], yprob, rtol=RELATIVE_TOLERANCE_PROB)


if __name__ == '__main__':
    unittest.main()
