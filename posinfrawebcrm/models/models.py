# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Areas(models.Model):
    _name = 'infrasan.areas'   
    _inherit = 'mail.thread'
    _rec_name = 'nombre' 
    _sql_constraints = [('unique_nombre', 'unique(nombre)', 'No se puede duplicar')]
    nombre = fields.Char('Nombre del area',size=35)
    ids_nodos = fields.One2many('infrasan.nodos','id_area',string='Nodos')
    ids_funcionarios = fields.One2many('res.partner','id_area',string='Funcionarios')

class Funcionarios(models.Model):
    _inherit = 'res.partner'                
    id_area = fields.Many2one('infrasan.areas',string='Area de la organizacion')
    ids_usuarios = fields.One2many('infrasan.usuarios','id_funcionario',string='Usuarios')    

class Nodos(models.Model):
    _name = 'infrasan.nodos'   
    _inherit = 'mail.thread' 
    _rec_name = 'nombre'
    _sql_constraints = [('unique_nombre', 'unique(nombre)', 'No se puede duplicar')]
    nombre = fields.Char('ID/Nombre de host/Nombre de dominio',size=45)
    tipo = fields.Selection([('fisico','Fisico'),('virtual','Virtual')],default='fisico',string='Tipo de nodo')
    id_area = fields.Many2one('infrasan.areas',string='Areas de la organizacion')
    ids_usuarios = fields.One2many('infrasan.usuarios','id_nodo',string='Usuario del sistema operativo')
    ids_ips = fields.One2many('infrasan.ips','id_nodo',string='Direcciones ip')
    ids_ubicacionesvirtuales = fields.One2many('infrasan.ubicacionesvirtuales','id_nodo',string='Ubicaciones')
    ids_servicios = fields.Many2many('infrasan.servicios','nodo_servicio_rel','id_nodo','id_servicio',string='Servicios')
    ciudad = fields.Char('Ciudad',size=24)#datos locacion.
    ccm = fields.Char('CCM',size=24)
    piso = fields.Char('Piso',size=16)
    fila = fields.Char('Fila',size=16)
    posicionu = fields.Char('PosicionU',size=16)
    etiqueta_rack = fields.Char('Etiqueta rack',size=24)
    etiqueta_equipo = fields.Char('Etiqueta equipo',size=24)
    equipo = fields.Char('Equipo',size=24)#especificaciones hardware
    marca = fields.Char('Marca',size=24)
    modelo = fields.Char('Modelo',size=16)
    generacion = fields.Integer('Generacion')
    serial = fields.Char('Serial',size=64)
    procesador = fields.Char('Procesador',size=64)
    memoria_ram = fields.Char('Memoria Ram',size=16)
    bahias_discos_en_uso = fields.Integer('Bahias de discos en uso')
    bahias_discos_vacios = fields.Integer('Bahias de discos vacias')
    descripcipon_de_discos = fields.Integer('Descripcion de discos')
    fecha_instalacion_en_sitio = fields.Date('Fecha instalacion en sitio')
    fecha_ultimo_mantenimiento = fields.Date('Fecha ultimo mantenimiento')
    expiracion_vida_util_de_equipo = fields.Char('Expiracion o vida util del equipo',size=16)
    proveedor = fields.Char('Proveedor',size=16)
    propietario = fields.Char('Propietario',size=16)
    aplicacion = fields.Char('Aplicacion',size=16)   
    sistema_operativo = fields.Char('Sistema operativo',size=16)
    licencia_so = fields.Char('Licencia sistema operativo',size=16)
    version_so = fields.Char('Version del sistema operativo',size=16)
    fecha_instalacion = fields.Date('Fecha instalacion del sistema operativo',size=16)
    gestion_a_realizar = fields.Char('Gestion a realizar',size=16)
    id_contrato_soporte = fields.Char('ID contrato de soporte',size=16)
    fecha_inicio_soporte = fields.Char('Fecha inicio soporte',size=16)
    fecha_fin_soporte = fields.Char('Fecha fin de soporte',size=16)
    contacto_soporte = fields.Char('Contacto de soporte',size=16)
    datos_soporte = fields.Char('Datos conctacto de soporte',size=16)
    comentarios = fields.Char('Comentarios',size=16)

class Usuarios(models.Model):
    _name = 'infrasan.usuarios'   
    _inherit = 'mail.thread'
    _rec_name = 'id_nodo'
    _sql_constraints = [('unique_nombre', 'unique(id_funcionario,id_nodo,id_servicio)', 'No se puede duplicar')]
    id_funcionario = fields.Many2one('res.partner',string='Funcionario')
    id_nodo = fields.Many2one('infrasan.nodos',string='Nodos')
    id_servicio = fields.Many2one('infrasan.servicios',string='Servicios')

class Servicios(models.Model):
    _name = 'infrasan.servicios'
    _rec_name = 'nombre'
    _inherit = 'mail.thread'
    _sql_constraints = [('unique_nombre_versionado', 'unique(nombre,puerto)', 'No se puede duplicar')]    
    nombre = fields.Char('Nombre, version y puerto del servicio. Ejemplo: ORACLEDB11G:1521',size=64)        
    ids_nodos = fields.Many2many('infrasan.nodos','nodo_servicio_rel','id_servicio','id_nodo',string='Nodos')
    ids_usuarios = fields.One2many('infrasan.usuarios','id_servicio',string='Usuarios del servicio')
    ids_ubicacionesvirtuales = fields.One2many('infrasan.ubicacionesvirtuales','id_servicio',string='Servicios')


class Redes(models.Model):
    _name = 'infrasan.redes'   
    _rec_name = 'nombre'
    _inherit = 'mail.thread' 
    _sql_constraints = [('unique_red', 'unique(nombre)', 'No se puede duplicar')]
    nombre = fields.Char('Nombre de la red',size=16)
    ids_ips = fields.One2many('infrasan.ips','id_red',string='Dispositivos e IPs')

class IPs(models.Model):
    _name = 'infrasan.ips'   
    _inherit = 'mail.thread'
    _rec_name = 'numero' 
    _sql_constraints = [('unique_red', 'unique(numero)', 'No se puede duplicar')]
    nombre_dispositivo = fields.Char('Nombre del dispositivo',size=16)
    numero = fields.Char('Direccion IPv4',size=16)
    mascara = fields.Char('Mascara de red',size=16)
    id_red = fields.Many2one('infrasan.redes',string='Red')
    id_nodo = fields.Many2one('infrasan.nodos',string='Nodos')

class ubicacionesVirtuales(models.Model):
    _name = 'infrasan.ubicacionesvirtuales'    
    _rec_name = 'path'
    _sql_constraints = [('unique_path', 'unique(path)', 'No se puede duplicar')]        
    tipo = fields.Selection([('archivo_configuracion','Archivo de configuracion'),
                             ('data_source','Data source'),
                             ('path','Path'),
                             ('compilable','Despliegable/Compilable/Paquete'),
                             ('url_acceso','URL acceso'),
                             ('url_balanceada','URL balanceada'), 
                             ('url_desplegable','URL repo desplegable'),
                             ('log','Log')],default='archivo_configuracion',string='Tipo')
    path = fields.Char('Ubicacion de archivo',size=128)
    detalle_uso = fields.Char('Detalle de uso',size=150)
    id_nodo = fields.Many2one('infrasan.nodos',string='Nodo')
    id_servicio = fields.Many2one('infrasan.servicios',string='Servicio')


# class infrasan(models.Model):
#     _name = 'infrasan.infrasan'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
