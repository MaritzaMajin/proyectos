# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Barrios(models.Model):
    idbarrios = models.IntegerField(db_column='idBarrios', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField()
    ciudad_idciudad = models.ForeignKey('Ciudad', models.DO_NOTHING, db_column='Ciudad_idCiudad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'barrios'


class Cabeza(models.Model):
    idcabeza = models.AutoField(db_column='idCabeza', primary_key=True)  # Field name made lowercase.
    comprobante = models.CharField(max_length=45)
    fecha = models.DateField()
    establecimiento = models.CharField(max_length=45)
    serie = models.CharField(max_length=45)
    precio_unitario = models.DecimalField(max_digits=9, decimal_places=2)
    precio_total = models.DecimalField(max_digits=9, decimal_places=2)
    hora = models.TimeField()
    persona_idpersona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='Persona_idPersona')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cabeza'


class Ciudad(models.Model):
    idciudad = models.IntegerField(db_column='idCiudad', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField()
    municipio_idmunicipio = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='Municipio_idMunicipio')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ciudad'


class Cuerpo(models.Model):
    idcuerpo = models.IntegerField(db_column='idCuerpo', primary_key=True)  # Field name made lowercase.
    sub_factura = models.DecimalField(max_digits=9, decimal_places=2)
    sub_total = models.DecimalField(max_digits=9, decimal_places=2)
    iva = models.DecimalField(max_digits=9, decimal_places=2)
    sub_iva = models.DecimalField(max_digits=9, decimal_places=2)
    iva_total = models.DecimalField(max_digits=9, decimal_places=2)
    total_factura = models.DecimalField(max_digits=9, decimal_places=2)
    fecha_generada = models.DateField()
    fecha_pago = models.DateField()
    hora_pago = models.TimeField()
    cabeza_idcabeza = models.ForeignKey(Cabeza, models.DO_NOTHING, db_column='Cabeza_idCabeza')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cuerpo'


class Departamento(models.Model):
    iddepartamento = models.IntegerField(db_column='idDepartamento', primary_key=True)  # Field name made lowercase.
    nombre_departamento = models.CharField(max_length=45)
    descripcion = models.TextField()

    class Meta:
        managed = False
        db_table = 'departamento'


class Desparasitacion(models.Model):
    iddesparasitacion = models.IntegerField(db_column='idDesparasitacion', primary_key=True)  # Field name made lowercase.
    nombre_medicamento = models.CharField(max_length=80)
    lote = models.CharField(max_length=45)
    labaratorio = models.CharField(max_length=45)
    registro_invima = models.CharField(max_length=80)
    indicaciones = models.TextField()
    contraindicaciones = models.TextField()
    dirigido = models.CharField(max_length=80)
    fecha_creacion = models.DateField()
    fecha_vencimiento = models.DateField()
    composicion = models.TextField()
    cantidad_composicion = models.CharField(max_length=100)
    cuidados = models.TextField()
    fecha_aplicacion = models.DateField()
    hora_aplicacion = models.TimeField()
    proxima_fecha = models.DateField()
    proxima_hora = models.TimeField()
    cantidad_aplicada = models.CharField(max_length=80)
    especie_idespecie = models.ForeignKey('Especie', models.DO_NOTHING, db_column='Especie_idEspecie')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'desparasitacion'


class Enfermedades(models.Model):
    idenfermedades = models.AutoField(db_column='idEnfermedades', primary_key=True)  # Field name made lowercase.
    tipo_enfermedad = models.CharField(max_length=80)
    casos = models.TextField()
    descripcion = models.TextField()
    frecuencia_casos = models.CharField(max_length=80)
    tratamiento = models.TextField()
    cuidados_enfermedad = models.TextField()
    enfermedadescol = models.CharField(db_column='Enfermedadescol', max_length=45)  # Field name made lowercase.
    causas = models.TextField()

    class Meta:
        managed = False
        db_table = 'enfermedades'


class Especie(models.Model):
    idespecie = models.PositiveIntegerField(db_column='idEspecie', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField()

    class Meta:
        managed = False
        db_table = 'especie'


class EsquemaVacunacion(models.Model):
    idesquema_vacunacion = models.IntegerField(db_column='idEsquema_vacunacion', primary_key=True)  # Field name made lowercase.
    vacuna_aplicada = models.CharField(max_length=60)
    dosis_aplicadas = models.CharField(max_length=45)
    dosis_aplicar = models.CharField(max_length=45)
    dosis_faltantes = models.CharField(max_length=100)
    fecha_aplicacion = models.DateField()
    hora_aplicacion = models.TimeField()
    proxima_fecha = models.DateField()
    cantidad_aplicada = models.CharField(max_length=80)
    zona_aplicada = models.CharField(max_length=80)
    via_aplicada = models.CharField(max_length=45)
    especie_idespecie = models.ForeignKey(Especie, models.DO_NOTHING, db_column='Especie_idEspecie')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'esquema_vacunacion'


class Evoluciones(models.Model):
    idevoluciones = models.IntegerField(db_column='idEvoluciones', primary_key=True)  # Field name made lowercase.
    tipo_evolucion = models.CharField(max_length=60)
    examen_fisico = models.TextField()
    parte_medico = models.TextField()
    descripcion = models.TextField()
    aspectos_positivos = models.TextField()
    aspectos_negativos = models.TextField()
    signos_vitales = models.CharField(max_length=100)
    fecha_inicial = models.DateField()
    proxima_fecha = models.DateField()
    fecha_final = models.DateField()
    procedimientos_idprocedimientos = models.ForeignKey('Procedimientos', models.DO_NOTHING, db_column='Procedimientos_idProcedimientos')  # Field name made lowercase.
    medicamentos_idmedicamentos = models.ForeignKey('Medicamentos', models.DO_NOTHING, db_column='Medicamentos_idMedicamentos')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'evoluciones'


class Habitat(models.Model):
    idhabitat = models.AutoField(db_column='idHabitat', primary_key=True)  # Field name made lowercase.
    tipo_habitat = models.CharField(max_length=45)
    descripcion = models.TextField()

    class Meta:
        managed = False
        db_table = 'habitat'


class HistoriaClinica(models.Model):
    idhistoria_clinica = models.IntegerField(db_column='idHistoria_clinica', primary_key=True)  # Field name made lowercase.
    informacion = models.TextField()
    mascota_idmascota = models.ForeignKey('Mascotas', models.DO_NOTHING, db_column='Mascota_idMascota')  # Field name made lowercase.
    vacunacion_idvacunacion = models.ForeignKey('Vacunacion', models.DO_NOTHING, db_column='Vacunacion_idVacunacion')  # Field name made lowercase.
    resumen_servicio_idresumen_servicio = models.ForeignKey('ResumenServicio', models.DO_NOTHING, db_column='Resumen_servicio_idResumen_servicio')  # Field name made lowercase.
    ingreso_idingreso = models.ForeignKey('Ingreso', models.DO_NOTHING, db_column='Ingreso_idIngreso')  # Field name made lowercase.
    desparasitacion_iddesparasitacion = models.ForeignKey(Desparasitacion, models.DO_NOTHING, db_column='Desparasitacion_idDesparasitacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'historia_clinica'


class Ingreso(models.Model):
    idingreso = models.AutoField(db_column='idIngreso', primary_key=True)  # Field name made lowercase.
    lugar = models.CharField(max_length=60)
    fecha = models.DateField()
    hora = models.TimeField()
    sintomas = models.TextField()
    comportamientos = models.TextField()
    descripcion = models.TextField()
    remision = models.CharField(max_length=60)
    personal_encargado = models.CharField(max_length=100)
    enfermedades_idenfermedades = models.ForeignKey(Enfermedades, models.DO_NOTHING, db_column='Enfermedades_idEnfermedades')  # Field name made lowercase.
    evoluciones_idevoluciones = models.ForeignKey(Evoluciones, models.DO_NOTHING, db_column='Evoluciones_idEvoluciones')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ingreso'


class Localidades(models.Model):
    idlocalidades = models.IntegerField(db_column='idLocalidades', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=80)
    descripcion = models.TextField()
    municipio_idmunicipio = models.ForeignKey('Municipio', models.DO_NOTHING, db_column='Municipio_idMunicipio')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'localidades'


class Mascotas(models.Model):
    idmascotas = models.AutoField(db_column='idMascotas', primary_key=True)  # Field name made lowercase.
    tipo_animal = models.CharField(max_length=45)
    clasificacion_animal = models.CharField(max_length=80)
    nombre = models.CharField(max_length=45)
    sexo = models.CharField(max_length=45)
    fecha_nacimiento = models.DateField()
    alimentacion = models.CharField(max_length=45)
    comportamientos = models.TextField()
    habitos = models.TextField()
    sintomas = models.TextField()
    caracteristicas_fisicas = models.TextField()
    raza_idraza = models.ForeignKey('Raza', models.DO_NOTHING, db_column='Raza_idRaza')  # Field name made lowercase.
    persona_idpersona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='Persona_idPersona')  # Field name made lowercase.
    habitat_idhabitat = models.ForeignKey(Habitat, models.DO_NOTHING, db_column='Habitat_idHabitat')  # Field name made lowercase.
    especie_idespecie = models.ForeignKey(Especie, models.DO_NOTHING, db_column='Especie_idEspecie')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mascotas'


class Medicamentos(models.Model):
    idmedicamentos = models.AutoField(db_column='idMedicamentos', primary_key=True)  # Field name made lowercase.
    nombre_generico = models.CharField(max_length=60)
    nombre_comercial = models.CharField(max_length=60)
    tipo_medicamento = models.CharField(max_length=45)
    administracion = models.CharField(max_length=45)
    aplicacion = models.CharField(max_length=45)
    dosis = models.CharField(max_length=45)
    posologia = models.CharField(max_length=60)
    registro_invima = models.CharField(max_length=80)
    laboratorio = models.CharField(max_length=60)
    lote = models.CharField(max_length=45)
    composicion = models.CharField(max_length=100)
    cantidad_composicion = models.CharField(max_length=80)
    fecha_creacion = models.DateField()
    fecha_vencimiento = models.DateField()
    indicaciones = models.TextField()
    contra_indicaciones = models.TextField()
    funcionamiento = models.TextField()
    via = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'medicamentos'


class Municipio(models.Model):
    idmunicipio = models.IntegerField(db_column='idMunicipio', primary_key=True)  # Field name made lowercase.
    nombre_municipio = models.CharField(max_length=45)
    descripcion = models.TextField()
    departamento_iddepartamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='Departamento_idDepartamento')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'municipio'


class Persona(models.Model):
    idpersona = models.AutoField(db_column='idPersona', primary_key=True)  # Field name made lowercase.
    primer_nombre = models.CharField(max_length=45)
    segundo_nombre = models.CharField(max_length=45, blank=True, null=True)
    primer_apellido = models.CharField(max_length=45)
    segundo_apellido = models.CharField(max_length=45)
    correo = models.CharField(max_length=80)
    documento = models.CharField(max_length=45)
    direccion = models.CharField(max_length=80)
    nacionalidad = models.CharField(max_length=45)
    nivel_academico = models.CharField(max_length=45)
    profesion = models.CharField(max_length=80)
    telefono = models.CharField(max_length=45)
    celular = models.CharField(max_length=45)
    genero = models.CharField(max_length=45)
    lugar_nacimiento = models.CharField(max_length=80)
    fecha_nacimiento = models.DateField()
    edad = models.CharField(max_length=45)
    tipo_persona_idtipo_persona = models.ForeignKey('TipoPersona', models.DO_NOTHING, db_column='Tipo_persona_idTipo_persona')  # Field name made lowercase.
    tipo_documento_idtipo_documento = models.ForeignKey('TipoDocumento', models.DO_NOTHING, db_column='Tipo_documento_idTipo_documento')  # Field name made lowercase.
    departamento_iddepartamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='Departamento_idDepartamento')  # Field name made lowercase.
    profesion_idprofesion = models.ForeignKey('Profesion', models.DO_NOTHING, db_column='Profesion_idProfesion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'persona'


class Procedimientos(models.Model):
    idprocedimientos = models.AutoField(db_column='idProcedimientos', primary_key=True)  # Field name made lowercase.
    tipo_procedimieno = models.CharField(max_length=100)
    resultados = models.TextField()
    descripcion = models.TextField()
    hora_procedimiento = models.TimeField()
    fecha_inicial = models.DateField()
    fecha_proxima = models.DateField()
    fecha_final = models.DateField()
    conclusiones = models.TextField()

    class Meta:
        managed = False
        db_table = 'procedimientos'


class Profesion(models.Model):
    idprofesion = models.IntegerField(db_column='idProfesion', primary_key=True)  # Field name made lowercase.
    tipo_profesion = models.CharField(max_length=45)
    descripcion = models.TextField()

    class Meta:
        managed = False
        db_table = 'profesion'


class Raza(models.Model):
    idraza = models.IntegerField(db_column='idRaza', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField()

    class Meta:
        managed = False
        db_table = 'raza'


class ResumenServicio(models.Model):
    idresumen_servicio = models.IntegerField(db_column='idResumen_servicio', primary_key=True)  # Field name made lowercase.
    descripcion_servicio = models.TextField()
    productos_utilizados = models.TextField()
    elementos_utilizados = models.TextField()
    fecha_servicio = models.DateField()
    hora_servicio = models.TimeField()
    incovenientes = models.TextField()
    servicios_idservicios = models.ForeignKey('Servicios', models.DO_NOTHING, db_column='Servicios_idServicios')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resumen_servicio'


class Servicios(models.Model):
    idservicios = models.AutoField(db_column='idServicios', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=80)
    descripcion = models.TextField()
    cabeza_idcabeza = models.ForeignKey(Cabeza, models.DO_NOTHING, db_column='Cabeza_idCabeza')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servicios'


class TipoDocumento(models.Model):
    idtipo_documento = models.IntegerField(db_column='idTipo_documento', primary_key=True)  # Field name made lowercase.
    nombre_documento = models.CharField(max_length=45)
    descripcion = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_documento'


class TipoPersona(models.Model):
    idtipo_persona = models.AutoField(db_column='idTipo_persona', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField()

    class Meta:
        managed = False
        db_table = 'tipo_persona'


class Vacunacion(models.Model):
    idvacunacion = models.IntegerField(db_column='idVacunacion', primary_key=True)  # Field name made lowercase.
    nombre_generico = models.CharField(max_length=60)
    nombre_comercial = models.CharField(max_length=60)
    laboratorio = models.CharField(max_length=80)
    composicion = models.TextField()
    cantidad_composicion = models.CharField(max_length=100)
    lote = models.CharField(max_length=60)
    fecha_creacion = models.DateField()
    fecha_vencimiento = models.DateField()
    registro_invima = models.CharField(max_length=80)
    posologia = models.CharField(max_length=100)
    indicaciones = models.TextField()
    contraindicaciones = models.TextField()
    cuidados = models.TextField()
    inmunidad = models.CharField(max_length=100)
    esquema_vacunacion_idesquema_vacunacion = models.ForeignKey(EsquemaVacunacion, models.DO_NOTHING, db_column='Esquema_vacunacion_idEsquema_vacunacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vacunacion'
