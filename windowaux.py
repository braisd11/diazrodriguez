from datetime import datetime

import drivers
import eventos
import var
from AboutWindow import *
from CalendarBajaWindow import *
from CalendarWindow import *
from ExitWindow import *
from ModificarBajaWindow import *


class About(QtWidgets.QDialog):
    def __init__(self):
        super(About, self).__init__()
        var.aboutWindow = Ui_dlgAbout()
        var.aboutWindow.setupUi(self)

        var.aboutWindow.lblVersion.setText(f"Versión: {var.version}")


class Baja(QtWidgets.QDialog):
    def __init__(self):
        super(Baja, self).__init__()
        var.dlgModificarBajaWindow = Ui_dlgModificarBajaWindow()
        var.dlgModificarBajaWindow.setupUi(self)

        var.dlgModificarBajaWindow.btnModificarFechaSi.clicked.connect(eventos.Eventos.confirmarModificar)
        var.dlgModificarBajaWindow.btnModificarFechaNo.clicked.connect(eventos.Eventos.cancelarModificar)


class Calendar(QtWidgets.QDialog):

    def __init__(self):
        super(Calendar, self).__init__()
        var.calendar = Ui_dlgCalendar()
        var.calendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year
        var.calendar.Calendar.setSelectedDate((QtCore.QDate(ano, mes, dia)))
        var.calendar.Calendar.clicked.connect(drivers.Drivers.cargarFecha)


class CalendarBaja(QtWidgets.QDialog):

    def __init__(self):
        super(CalendarBaja, self).__init__()
        var.dlgCalendarbaja = Ui_dlgCalendarBaja()
        var.dlgCalendarbaja.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year
        var.dlgCalendarbaja.calendarBaja.setSelectedDate((QtCore.QDate(ano, mes, dia)))
        var.dlgCalendarbaja.calendarBaja.clicked.connect(drivers.Drivers.cargarFechaBaja)


class Exit(QtWidgets.QDialog):

    def __init__(self):
        super(Exit, self).__init__()
        var.exitWindow = Ui_dlgSalir()
        var.exitWindow.setupUi(self)

        '''
            Zona de Eventos de botones de dlgSalir
        '''

        var.exitWindow.btnSalirSi.clicked.connect(eventos.Eventos.confirmarSalir)
        var.exitWindow.btnSalirNo.clicked.connect(eventos.Eventos.cancelarSalir)


class FileDialogAbrir(QtWidgets.QFileDialog):

    def __init__(self):
        super(FileDialogAbrir, self).__init__()
