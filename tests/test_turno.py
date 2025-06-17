import unittest
from datetime import datetime
from src.modelo.turno import Turno
from src.modelo.paciente import Paciente
from src.modelo.medico import Medico
from src.modelo.especialidad import Especialidad


class TestTurno(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Tomas Merino", "12345678", "27/12/1999")
        self.medico = Medico("Dr. Francisco Hubert", "1233")
        self.medico.agregar_especialidad(Especialidad("Pediatría", ["lunes"]))
        
        self.fecha_hora = datetime(2026, 6, 1, 10, 0)
        self.especialidad = "Pediatría"
        self.turno = Turno(self.paciente, self.medico, self.fecha_hora, self.especialidad)

    def test_obtener_medico(self):
        self.assertEqual(self.turno.obtener_medico(), self.medico)

    def test_obtener_paciente(self):
        self.assertEqual(self.turno.obtener_paciente(), self.paciente)

    def test_obtener_fecha_hora(self):
        self.assertEqual(self.turno.obtener_fecha_hora(), self.fecha_hora)

    def test_obtener_especialidad(self):
        self.assertEqual(self.turno.obtener_especialidad(), self.especialidad)

    def test_str(self):
        turno_str = str(self.turno)
        self.assertIn("Tomas Merino", turno_str)
        self.assertIn("Dr. Francisco HUbert", turno_str)
        self.assertIn("Pediatría", turno_str)
        self.assertIn("01/06/2026", turno_str)


if __name__ == "__main__":
    unittest.main()
