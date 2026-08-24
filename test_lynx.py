import unittest
from lynx import LynxEvaluator, LynxConfig

class TestLynx(unittest.TestCase):
    def test_near_reference_low_novelty(self):
        ev = LynxEvaluator([[0,0],[0.1,0.1]], config=LynxConfig(novelty_threshold=0.5))
        out = ev.evaluate([0.05,0.05], replication=1.0)
        self.assertLess(out["novelty_score"],0.5)

    def test_far_candidate_higher_novelty(self):
        ev = LynxEvaluator([[0,0],[0.1,0.1]])
        near = ev.evaluate([0.05,0.05])
        far = ev.evaluate([1.0,1.0])
        self.assertGreater(far["novelty_score"], near["novelty_score"])

    def test_rediscovery_penalty(self):
        ev = LynxEvaluator([[0,0]], rare_archive=[[1,1]])
        rediscovered = ev.evaluate([1,1])
        other = ev.evaluate([1,-1])
        self.assertLess(rediscovered["novelty_score"], other["novelty_score"])

if __name__ == "__main__":
    unittest.main()
