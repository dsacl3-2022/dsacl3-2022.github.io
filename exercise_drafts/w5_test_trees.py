from unittest import TestCase
from w5_trees import *


class Test(TestCase):
    def test_to_array1(self):
        you = Node("you")
        cousin = Node("cousin")
        mother = Node("mother", you)
        aunt = Node("aunt", cousin)
        grandmother = Node("grandmother", mother, aunt)
        self.assertListEqual(["grandmother", "mother", "aunt", "you", None, "cousin"], grandmother.to_array())

    def test_to_array2(self):
        a = Node("a")
        nice = Node("nice")
        tree = Node("tree")
        det = Node("Det", a)
        adj = Node("Adj", nice)
        adjp = Node("AdjP", adj)
        noun = Node("N", tree)
        np1 = Node("NP", noun)
        np2 = Node("NP", adjp, np1)
        root = Node("NP", det, np2)

        expected = [None for _ in range(28)]
        expected[0] = "NP"
        expected[1] = "Det"
        expected[2] = "NP"
        expected[3] = "a"
        expected[5] = "AdjP"
        expected[6] = "NP"
        expected[11] = "Adj"
        expected[13] = "N"
        expected[23] = "nice"
        expected[27] = "tree"

        self.assertListEqual(expected, root.to_array())

    def test_get_depth(self):
        the = Node("the")
        big = Node("big")
        dog = Node("dog")
        very = Node("very")
        adv = Node("Adv", very)
        advP = Node("AdvP", adv)
        adj = Node("Adj", big)
        adjP = Node("AdjP", advP, adj)
        n = Node("N", dog)
        np2 = Node("NP", adjP, n)
        det = Node("Det", the)
        np1 = Node("NP", det, np2)
        self.assertEqual(3, np1.get_depth(dog))

    def test_get_depth2(self):
        the = Node("the")
        big = Node("big")
        dog = Node("dog")
        very = Node("very")
        adv = Node("Adv", very)
        advP = Node("AdvP", adv)
        adj = Node("Adj", big)
        adjP = Node("AdjP", advP, adj)
        n = Node("N", dog)
        np2 = Node("NP", adjP, n)
        det = Node("Det", the)
        np1 = Node("NP", det, np2)
        self.assertEqual(5, np1.get_depth(very))

    def test_qtree1(self):
        you = Node("you")
        cousin = Node("cousin")
        mother = Node("mother", you)
        aunt = Node("aunt", cousin)
        grandmother = Node("grandmother", mother, aunt)

        self.assertEqual(grandmother.to_qtree().strip(),
                         "\Tree [.grandmother [.mother  you ].mother [.aunt  cousin ].aunt ].grandmother")

    def test_qtree2(self):
        the = Node("the")
        very = Node("very")
        big = Node("big")
        dog = Node("dog")
        slept = Node("slept")
        quite = Node("quite")
        peacefully = Node("peacefully")
        adv1 = Node("Adv", very)
        advP1 = Node("AdvP", adv1)
        adj = Node("Adj", big)
        adjP = Node("AdjP", advP1, adj)
        n = Node("N", dog)
        np2 = Node("NP", adjP, n)
        det = Node("Det", the)
        np1 = Node("NP", det, np2)
        v = Node("V", slept)
        adv2 = Node("Adv", quite)
        advP2 = Node("AdvP", adv2)
        adv3= Node("Adv", peacefully)
        advP3 = Node("AdvP", advP2, adv3)
        vp = Node("VP", v, advP3)
        s = Node("S", np1, vp)
        self.assertEqual(
            "\Tree [.S [.NP [.Det  the ].Det [.NP \qroof{very big}.AdjP [.N  dog ].N ].NP ].NP [.VP [.V  slept ].V " +
            "[.AdvP \qroof{quite}.AdvP [.Adv  peacefully ].Adv ].AdvP ].VP ].S",
            s.to_qtree().strip())


    def test_make_roof1(self):
        the = Node("the")
        big = Node("big")
        dog = Node("dog")
        very = Node("very")
        adv = Node("Adv", very)
        advP = Node("AdvP", adv)
        adj = Node("Adj", big)
        adjP = Node("AdjP", advP, adj)
        n = Node("N", dog)
        np2 = Node("NP", adjP, n)
        det = Node("Det", the)
        np1 = Node("NP", det, np2)
        self.assertEqual("\qroof{very big dog}.NP", np2.make_roof().strip())

    def test_make_roof2(self):
        the = Node("the")
        big = Node("big")
        dog = Node("dog")
        very = Node("very")
        adv = Node("Adv", very)
        advP = Node("AdvP", adv)
        adj = Node("Adj", big)
        adjP = Node("AdjP", advP, adj)
        n = Node("N", dog)
        np2 = Node("NP", adjP, n)
        det = Node("Det", the)
        np1 = Node("NP", det, np2)
        self.assertEqual("\qroof{the very big dog}.NP", np1.make_roof().strip())



