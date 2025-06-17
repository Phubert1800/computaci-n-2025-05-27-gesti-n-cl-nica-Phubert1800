import unittest
from src.modelo.receta import Receta
from src.modelo.paciente import Paciente
from src.modelo.medico import Medico
from src.modelo.especialidad import Especialidad


class TestReceta(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Tomas Merino", "12345678", "27/12/1999")
        self.medico = Medico("Dr. Francisco Hubert, "1254")
        self.medico.agregar_especialidad(Especialidad("Pediatría", ["lunes"]))
        
        self.medicamentos = ["Paracetamol", "Ibuprofeno"]
        self.receta = Receta(self.paciente, self.medico, self.medicamentos)

    def test_obtener_paciente(self):
        self.assertEqual(self.receta.obtener_paciente(), self.paciente)

    def test_obtener_medico(self):
        self.assertEqual(self.receta.obtener_medico(), self.medico)

    def test_obtener_medicamentos(self):
        medicamentos = self.receta.obtener_medicamentos()
        self.assertEqual(medicamentos, ["Paracetamol", "Ibuprofeno"])

    def test_obtener_fecha(self):
        fecha = self.receta.obtener_fecha()
        self.assertIsNotNone(fecha)

    def test_str(self):
        receta_str = str(self.receta)
        self.assertIn("Tomas Merino", receta_str)
        self.assertIn("Dr. Francisco Hubert", receta_str)
        self.assertIn("Paracetamol", receta_str)
        self.assertIn("Ibuprofeno", receta_str)


if __name__ == "__main__":
    unittest.main()
