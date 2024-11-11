import unittest
from nuclear_radius import nuclear_radius
from binding_energy_per_nucleon import binding_energy_per_nucleon
from atomic_mass import atomic_mass
from is_stable_against_beta_decay import is_stable_against_beta_decay
from can_split_into_even_even_fragments import can_split_into_even_even_fragments

class TestCalculations(unittest.TestCase):
    
    def test_nuclear_radius(self):
        A = 238
        expected_radius = 7.44
        self.assertAlmostEqual(nuclear_radius(A), expected_radius, places=2)

    def test_binding_energy_per_nucleon(self):
        A = 238
        Z = 92
        expected_binding_energy = 7.57
        self.assertAlmostEqual(binding_energy_per_nucleon(A, Z), expected_binding_energy, places=2)

    def test_atomic_mass(self):
        A = 238
        Z = 92
        expected_mass = 238.05
        self.assertAlmostEqual(atomic_mass(A, Z), expected_mass, places=2)

    def test_is_stable_against_beta_decay(self):
        A = 238
        Z = 92
        expected_stability = "Неустойчив к β⁻-распаду (избыток нейтронов)"
        self.assertEqual(is_stable_against_beta_decay(A, Z), expected_stability)
        
        A = 16
        Z = 8
        expected_stability_O16 = "Устойчив к β-распаду"
        self.assertEqual(is_stable_against_beta_decay(A, Z), expected_stability_O16)

    def test_can_split_into_even_even_fragments(self):
        A = 238
        Z = 92
        expected_split_result = "Можно разделить на два одинаковых четно-четных осколка"
        self.assertEqual(can_split_into_even_even_fragments(A, Z), expected_split_result)
        
        A = 31
        Z = 15
        expected_split_result_P31 = "Невозможно разделить на два одинаковых четно-четных осколка"
        self.assertEqual(can_split_into_even_even_fragments(A, Z), expected_split_result_P31)

if __name__ == "__main__":
    unittest.main()