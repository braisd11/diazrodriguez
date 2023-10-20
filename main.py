import drivers
import eventos
from windowaux import *
from MainWindow import *
from AboutWindow import *
import sys, var
import locale

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)  # Método encargado de generar la interfaz
        var.calendar = Calendar()
        var.exitWindow = Exit()
        var.aboutWindow = About()

        '''
        
            Zona de eventos de botones
        
        '''

        var.ui.btnCalendar.clicked.connect(eventos.Eventos.abrirCalendar)
        var.ui.btnAltaDriver.clicked.connect(drivers.Drivers.altaDriver)

        '''
            
            Zona de eventos del menubars
        
        '''

        var.ui.actionSalir.triggered.connect(eventos.Eventos.showSalir)
        var.ui.actionAcerca_de.triggered.connect(eventos.Eventos.acercade)

        '''
        
            Zona de eventos de las cajas de texto
        
        '''

        var.ui.txtDNI.editingFinished.connect(drivers.Drivers.validarDNI)
        var.ui.txtApel.editingFinished.connect(eventos.Eventos.letraCapital)
        var.ui.txtNombre.editingFinished.connect(eventos.Eventos.letraCapital)
        var.ui.txtSalario.editingFinished.connect(eventos.Eventos.letraCapital)

        '''
            
            Zona de eventos de la toolbar
        '''

        var.ui.actionSalir.triggered.connect(eventos.Eventos.showSalir)
        var.ui.actionlimpiarPanel.triggered.connect(drivers.Drivers.limpiarPanel)

        '''
            Zona de ejecución de accionas al iniciar programa
        '''

        eventos.Eventos.cargastatusbar(self)
        eventos.Eventos.cargaprov(self)
        rbtDriver = [var.ui.rbtTodos, var.ui.rbtAlta, var.ui.rbtBaja]
        for i in rbtDriver:
            i.clicked.connect(eventos.Eventos.selEstado)


        '''
        
            Eventos de Tablas
        '''
        eventos.Eventos.resizeTabdrivers(self)

    def closeEvent(self, event):
        # event.ignore()
        # eventos.Eventos.showSalir(self)

        mbox = QtWidgets.QMessageBox.information(self, 'Salir', '¿Estás seguro de que quieres salir?',
                                                 QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

        if mbox == QtWidgets.QMessageBox.StandardButton.Yes:
            app.quit()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
