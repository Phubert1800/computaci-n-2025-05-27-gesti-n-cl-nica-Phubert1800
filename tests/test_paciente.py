import unittest
from src.modelo.paciente import Paciente
from src.modelo.exepciones import DatosInvalidosException


class TestPaciente(unittest.TestCase):
    
    def test_creacion_paciente_exitosa(self):
        """Prueba la creación exitosa de un paciente."""
        paciente = Paciente("Tomas Merino", "12345678", "27/12/1999")
        self.assertEqual(paciente.obtener_dni(), "12345678")
        self.assertEqual(paciente.obtener_nombre(), "Tomas Merino")
        self.assertEqual(paciente.obtener_fecha_nacimiento(), "27/12/1999")
        self.assertEqual(str(paciente), "Tomas Merino, 12345678, 27/12/1999")

    def test_nombre_vacio(self):
        """Prueba error cuando el nombre está vacío."""
        with self.assertRaises(DatosInvalidosException):
            Paciente("", "12345678", "27/12/1999")

    def test_nombre_solo_espacios(self):
        """Prueba error cuando el nombre son solo espacios."""
        with self.assertRaises(DatosInvalidosException):
            Paciente(" ", "12345678", "27/12/1999")

    def test_nombre_con_caracteres_invalidos(self):
        """Prueba error cuandoPérez el nombre contiene caracteres inválidos."""
        with self.assertRaises(DatosInvalidosException):
            Paciente("Tomas1123", "12345678", "27/12/1999")

    def test_dni_vacio(self):
        """Prueba error cuando el DNI está vacío."""
        with self.assertRaises(DatosInvalidosException):
            Paciente("Tomas Merino", "", "27/12/19999")

    def test_dni_muy_corto(self):
        """Prueba error cuando el DNI es muy corto."""
        with self.assertRaises(DatosInvalidosException):
            Paciente("Tomas Merino", "123456", "27/12/1999")

    def test_dni_muy_largo(self):
        """Prueba error cuando el DNI es muy largo."""
        with self.assertRaises(DatosInvalidosException):
            Paciente("Tomas Merino", "123456789", "27/12/1999")

    def test_dni_con_letras(self):
        """Prueba error cuando el DNI contiene letras."""
        with self.assertRaises(DatosInvalidosException):
            Paciente("Tomas Merino", "1234567A", "27/12/1999")

    def test_fecha_vacia(self):
        """Prueba error cuando la fecha está vacía."""
        with self.assertRaises(DatosInvalidosException):
            Paciente("Tomas Merino", "12345678", "")

    def test_fecha_formato_incorrecto(self):
        """Prueba error cuando la fecha tiene formato incorrecto."""
        with self.assertRaises(DatosInvalidosException):
            Paciente("Tomas Merino, "12345678", "1999-12-27")

    def test_fecha_invalida(self):
        """Prueba error cuando la fecha es inválida."""
        with self.assertRaises(DatosInvalidosException):
            Paciente("Tomas Merino", "12345678", "32/13/2000")

    def test_dni_diferente(self):
        """Prueba que pacientes diferentes tienen DNIs diferentes."""
        paciente1 = Paciente("Tomas Merino, "12345678", "27/12/1999")
        paciente2 = Paciente("JOaquina Hubert", "87654321", "15/01/1990")
        self.assertNotEqual(paciente1.obtener_dni(), paciente2.obtener_dni())


if __name__ == "__main__":
    unittest.main()
