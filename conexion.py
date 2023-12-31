from PyQt6 import QtWidgets, QtSql, QtCore

import clientes
import drivers
import eventos
import var
import datetime


class Conexion():
    def conexion(self=None):
        var.bbdd = 'bbdd.sqlite'
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(var.bbdd)

        if not db.open():

            print("Error de conexión")
            return False

        else:

            print("Base Datos conectada")
            return True

    def cargaprov(self=None):
        try:
            var.ui.cmbProv.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')

            if query.exec():
                var.ui.cmbProv.addItem("")

                while query.next():
                    var.ui.cmbProv.addItem(query.value(0))


        except Exception as error:

            print("Error al mostar cmbProv")

    def cargaprovcli(self=None):
        try:
            var.ui.cmbProvcli.clear()
            query = QtSql.QSqlQuery()
            query.prepare('select provincia from provincias')

            if query.exec():
                var.ui.cmbProvcli.addItem("")

                while query.next():
                    var.ui.cmbProvcli.addItem(query.value(0))


        except Exception as error:

            print("Error al mostar cmbProvcli")

    def selMuni(self=None):
        try:
            id = 0
            var.ui.cmbMuni.clear()
            prov = var.ui.cmbProv.currentText()
            query = QtSql.QSqlQuery()
            query.prepare('select idprov from provincias where provincia = :prov')
            query.bindValue(':prov', prov)

            if query.exec():

                while query.next():
                    id = query.value(0)

            query1 = QtSql.QSqlQuery()
            query1.prepare('select municipio from municipios where idprov = :id')
            query1.bindValue(':id', int(id))

            if query1.exec():

                var.ui.cmbMuni.addItem('')

                while query1.next():
                    var.ui.cmbMuni.addItem(query1.value(0))

        except Exception as error:
            print("Error seleccion municipios", error)


    def selMunicli(self=None):
        try:
            id = 0
            var.ui.cmbMunicli.clear()
            prov = var.ui.cmbProvcli.currentText()
            query = QtSql.QSqlQuery()
            query.prepare('select idprov from provincias where provincia = :prov')
            query.bindValue(':prov', prov)

            if query.exec():

                while query.next():
                    id = query.value(0)

            query1 = QtSql.QSqlQuery()
            query1.prepare('select municipio from municipios where idprov = :id')
            query1.bindValue(':id', int(id))

            if query1.exec():

                var.ui.cmbMunicli.addItem('')

                while query1.next():
                    var.ui.cmbMunicli.addItem(query1.value(0))

        except Exception as error:
            print("Error seleccion municipios clientes", error)

    @staticmethod
    def guardardri(newdriver):
        try:
            if (newdriver[0].strip() == "" or newdriver[1].strip() == "" or newdriver[2].strip() == ""):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Faltan Datos. Debe introducir al menos \n"
                             "DNI, Apellidos, Nombre, Fecha de Alta, Móvil")
                mbox.exec()

            else:
                query = QtSql.QSqlQuery()
                query.prepare('insert into drivers (dnidri, altadri, nombredri, apeldri, '
                              'direcciondri, provdri, munidri, movildri, salario, carnet) VALUES (:dni, :alta, :nombre, '
                              ':apel, :direccion, :prov, :muni, :movil, :salario, :carnet)')
                query.bindValue(':dni', str(newdriver[0]))
                query.bindValue(':alta', str(newdriver[1]))
                query.bindValue(':nombre', str(newdriver[2]))
                query.bindValue(':apel', str(newdriver[3]))
                query.bindValue(':direccion', str(newdriver[4]))
                query.bindValue(':prov', str(newdriver[5]))
                query.bindValue(':muni', str(newdriver[6]))
                query.bindValue(':movil', str(newdriver[7]))
                query.bindValue(':salario', str(newdriver[8]))
                query.bindValue(':carnet', str(newdriver[9]))

                if query.exec():
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText("Empleado dado de alta")
                    mbox.exec()
                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText("Error al guardar el driver")
                    mbox.exec()
                #Conexion.mostrardrivers()
                drivers.Drivers.selEstado()


        except Exception as error:
            print("Error al guardar el driver", error)


    @staticmethod
    def guardarcli(newcliente):
        try:
            if (newcliente[0].strip() == "" or newcliente[1].strip() == "" or newcliente[2].strip() == "" or newcliente[3].strip() == ""):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Faltan Datos. Debe introducir al menos \n"
                             "DNI, Nombre, Dirección, Móvil")
                mbox.exec()

            else:
                query = QtSql.QSqlQuery()
                query.prepare('insert into clientes (dnicli, razoncli, direccioncli, '
                              ' telefonocli, provcli, municli) VALUES (:dni, :nombrecli, '
                              ' :direccioncli, :movilcli, :provcli, :municli)')
                query.bindValue(':dni', str(newcliente[0]))
                query.bindValue(':nombrecli', str(newcliente[1]))
                query.bindValue(':direccioncli', str(newcliente[2]))
                query.bindValue(':movilcli', str(newcliente[3]))
                query.bindValue(':provcli', str(newcliente[4]))
                query.bindValue(':municli', str(newcliente[5]))

                if query.exec():
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setText("Cliente dado de alta")
                    mbox.exec()
                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    print(query.lastError())
                    mbox.setText("Error al guardar el cliente")
                    mbox.exec()

                clientes.Clientes.selEstadocli()


        except Exception as error:
            print("Error al guardar el cliente", error)

    @staticmethod
    def mostrardrivers():
        try:
            estado = 1
            Conexion.selectDrivers(estado)

        except Exception as error:
            print("error al cargar la tabla", error)

    @staticmethod
    def mostrarclientes():
        try:
            estado = 1
            Conexion.selectClientes(estado)

        except Exception as error:
            print("error al cargar la tabla", error)

    def onedriver(id):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select * from drivers where codigo = :id')

            query.bindValue(':id', int(id))
            if query.exec():
                while query.next():
                    for i in range(12):
                        registro.append(str(query.value(i)))
            return registro

        except Exception as error:
            print('error en fichero conexion dato de 1 driver', error)

    def onecli(id):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare('select * from clientes where codcli = :id')

            query.bindValue(':id', int(id))
            if query.exec():
                while query.next():
                    for i in range(8):
                        registro.append(str(query.value(i)))
            return registro


        except Exception as error:
            print('error en fichero conexion dato de 1 cliente', error)




    def codDri(dni):
        try:
            registro = None
            query = QtSql.QSqlQuery()
            query.prepare('select codigo from drivers where dniDri = :dni')
            query.bindValue(':dni', str(dni))

            if query.exec():
                while query.next():
                    codigo = query.value(0)
            try:

                registro = Conexion.onedriver(codigo)
            except Exception as error:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("No existe nadie con ese DNI")
                mbox.exec()
            return registro

        except Exception as error:
            print('error al buscar el dni', error)

    def comprobarModifDriver(modifdriver):
        try:
            codigo = var.ui.lblCodBD.text()

            if drivers.Drivers.comprobarfechabaja(codigo):
                eventos.Eventos.showModificarBaja()
                Conexion.modifDriver(modifdriver)

            else:

                Conexion.modifDriver(modifdriver)
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Datos conductor modificados")
                mbox.exec()

        except Exception as error:
            print("error en comprobarmodifdriver conexion", error)

    def comprobarModifCli(modifcliente):
        try:
            codigo = var.ui.lblCodBDcli.text()

            if drivers.Drivers.comprobarfechabaja(codigo):
                eventos.Eventos.showModificarBaja()
                Conexion.modifCliente(modifcliente)

            else:

                Conexion.modifCliente(modifcliente)
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Datos cliente modificados")
                mbox.exec()

        except Exception as error:
            print("error en comprobarmodifcli conexion", error)

    @staticmethod
    def modifDriver(modifdriver):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('update drivers set dnidri = :dni, altadri = :alta ,nombredri = :nombre, apeldri = :apel, '
                          'direcciondri = :direccion, provdri = :provincia, munidri = :municipio,'
                          'movildri = :movil, salario = :salario, carnet = :carnet where codigo = :codigo')

            query.bindValue(':codigo', int(modifdriver[0]))
            query.bindValue(':dni', str(modifdriver[1]))
            query.bindValue(':alta', str(modifdriver[2]))
            query.bindValue(':apel', str(modifdriver[3]))
            query.bindValue(':nombre', str(modifdriver[4]))
            query.bindValue(':direccion', str(modifdriver[5]))
            query.bindValue(':provincia', str(modifdriver[6]))
            query.bindValue(':municipio', str(modifdriver[7]))
            query.bindValue(':movil', str(modifdriver[8]))
            query.bindValue(':salario', str(modifdriver[9]))
            query.bindValue(':carnet', str(modifdriver[10]))

            if query.exec():

                drivers.Drivers.selEstado()

            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Error al modificar los datos del conductor")
                mbox.exec()

        except Exception as error:
            print('error en modifdriver', error)


    @staticmethod
    def modifCliente(modifcliente):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('update clientes set dnicli = :dnicli, razoncli = :razoncli, '
                          'direccioncli = :direccioncli, telefonocli = :telefonocli,'
                          ' provcli = :provincia, municli = :municipio'
                          ' where codcli = :codcli')

            query.bindValue(':codcli', int(modifcliente[0]))
            query.bindValue(':dnicli', str(modifcliente[1]))
            query.bindValue(':razoncli', str(modifcliente[2]))
            query.bindValue(':direccioncli', str(modifcliente[3]))
            query.bindValue(':telefonocli', str(modifcliente[4]))
            query.bindValue(':provincia', str(modifcliente[5]))
            query.bindValue(':municipio', str(modifcliente[6]))

            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Datos del cliente modificados")
                mbox.exec()
                var.ui.lblValidarDNIcli.clear()

                clientes.Clientes.selEstadocli()

            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Error al modificar los datos del cliente")
                mbox.exec()

        except Exception as error:
            print('error en modifcliente', error)

    def borraDriv(dni):
        try:
            query1 = QtSql.QSqlQuery()
            query1.prepare('select bajadri from drivers where '
                           'dnidri = :dni')
            query1.bindValue(':dni', str(dni))
            if query1.exec():
                while query1.next():
                    valor = query1.value(0)

            if str(valor) == '':
                fecha = datetime.date.today()
                fecha = fecha.strftime('%d/%m/%Y')
                query = QtSql.QSqlQuery()
                query.prepare('update drivers set bajadri = :fechabaja where '
                              'dnidri = :dni')
                query.bindValue(':fechabaja', str(fecha))
                query.bindValue(':dni', str(dni))

                if query.exec():
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setText("Conductor dado de baja")
                    mbox.exec()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Error al dar de baja el conductor")
                mbox.exec()

            pass
        except Exception as error:
            print("error en borradriv en conexion", error)


    def borracli(dni):
        try:
            query1 = QtSql.QSqlQuery()
            query1.prepare('select bajacli from clientes where '
                           'dnicli = :dni')
            query1.bindValue(':dni', str(dni))
            if query1.exec():
                while query1.next():
                    valor = query1.value(0)

            if str(valor) == '':
                fecha = datetime.date.today()
                fecha = fecha.strftime('%d/%m/%Y')
                query = QtSql.QSqlQuery()
                query.prepare('update clientes set bajacli = :fechabaja where '
                              'dnicli = :dni')
                query.bindValue(':fechabaja', str(fecha))
                query.bindValue(':dni', str(dni))

                if query.exec():
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setText("Cliente dado de baja")
                    mbox.exec()
            else:
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("Error al dar de baja el cliente")
                mbox.exec()

            pass
        except Exception as error:
            print("error en borracli en conexion", error)

    def selectDrivers(estado):
        try:
            registro = []

            consulta = "select codigo, apeldri, nombredri, movildri, carnet, bajadri from drivers"

            if int(estado) == 1:

                consulta = consulta + " where bajadri is null"

            elif int(estado) == 2:

                consulta = consulta + " where bajadri is not null"

            query = QtSql.QSqlQuery()
            query.prepare(consulta)

            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registro.append(row)
            drivers.Drivers.cargartabladri(registro)
        except Exception as error:
            print('error al seleccionar driver', error)

    @staticmethod
    def selectClientes(estado):
        try:
            registro = []

            consulta = "select * from clientes"

            if int(estado) == 0:

                consulta = consulta + " where bajacli is null"

            query = QtSql.QSqlQuery()
            query.prepare(consulta)

            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registro.append(row)

            clientes.Clientes.cargartablacli(registro)

        except Exception as error:
            print('error al seleccionar cliente', error)

    @staticmethod
    def selectclientestodos():
        try:
            registros = []

            query = QtSql.QSqlQuery()
            query.prepare('Select * from clientes')

            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registros.append(row)
            return registros
        except Exception as error:
            print('error al devolver todos los clientes', error)

    @staticmethod
    def selectdriverstodos():
        try:
            registros = []

            query = QtSql.QSqlQuery()
            query.prepare('Select * from drivers order by apeldri')
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]
                    registros.append(row)
            return registros
        except Exception as error:
            print('error al devolver todos los drivers', error)

    @staticmethod
    def borrarfechabaja(codigo):
        try:

            query = QtSql.QSqlQuery()
            query.prepare("update drivers set bajadri = null where codigo = :codigo")

            query.bindValue(':codigo', str(codigo))

            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Driver dado de alta")
                mbox.exec()

        except Exception as error:
            print('error al borrar fecha baja', error)


    @staticmethod
    def borrarfechabajacli(codigo):
        try:

            query = QtSql.QSqlQuery()
            query.prepare("update clientes set bajacli = null where codcli = :codigo")

            query.bindValue(':codigo', str(codigo))

            if query.exec():
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Cliente dado de alta")
                mbox.exec()

        except Exception as error:
            print('error al borrar fecha baja cliente', error)

    @staticmethod
    def guardarimport(new):
        try:

            if drivers.Drivers.validarDNI(str(new[1])):

                query = QtSql.QSqlQuery()

                if str(new[11]) == '':
                    query.prepare(
                        'insert into drivers values(null, :dni, :alta, :nombre, :apel, :direccion, :prov, :muni, '
                        ':movil, :salario, :carnet, null)'
                    )
                    query.bindValue(':dni', str(new[1]))
                    query.bindValue(':alta', str(new[2]))
                    query.bindValue(':nombre', str(new[3]))
                    query.bindValue(':apel', str(new[4]))
                    query.bindValue(':direccion', str(new[5]))
                    query.bindValue(':prov', str(new[6]))
                    query.bindValue(':muni', str(new[7]))
                    query.bindValue(':movil', str(new[8]))
                    query.bindValue(':salario', str(new[9]))
                    query.bindValue(':carnet', str(new[10]))
                else:
                    query.prepare(
                        'insert into drivers values(null, :dni, :alta, :nombre, :apel, :direccion, :prov, :muni, '
                        ':movil, :salario, :carnet, :baja)'
                    )
                    query.bindValue(':dni', str(new[1]))
                    query.bindValue(':alta', str(new[2]))
                    query.bindValue(':nombre', str(new[3]))
                    query.bindValue(':apel', str(new[4]))
                    query.bindValue(':direccion', str(new[5]))
                    query.bindValue(':prov', str(new[6]))
                    query.bindValue(':muni', str(new[7]))
                    query.bindValue(':movil', str(new[8]))
                    query.bindValue(':salario', str(new[9]))
                    query.bindValue(':carnet', str(new[10]))
                    query.bindValue(':baja', str(new[11]))

                if query.exec():
                    pass
                else:
                    print(query.lastError().text())
        except Exception as error:
            print('error en guardarimport', error)

    @staticmethod
    def guardarimportcli(new):
        try:
            if clientes.Clientes.validarDNIcli(str(new[0])):

                query = QtSql.QSqlQuery()

                query.prepare(
                    'insert into clientes values(null, :dni, :nombre, :direccion, :movil, :prov, :muni, null)'
                )
                query.bindValue(':dni', str(new[0]))
                query.bindValue(':nombre', str(new[1]))
                query.bindValue(':direccion', str(new[2]))
                query.bindValue(':movil', str(new[3]))
                query.bindValue(':prov', str(new[4]))
                query.bindValue(':muni', str(new[5]))

                if query.exec():
                    pass
                else:
                    print(query.lastError().text())
            else:
                print("dni no válido")
        except Exception as error:
            print('error en guardarimportcli', error)


