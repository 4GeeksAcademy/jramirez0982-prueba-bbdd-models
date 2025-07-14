from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, Enum, Date, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum, datetime
from typing import List

db = SQLAlchemy()

# class User(db.Model):
#     id: Mapped[int] = mapped_column(primary_key=True)
#     email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
#     password: Mapped[str] = mapped_column(nullable=False)
#     is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }

#Se definen los posibles estados de la orden de servicio con tipo de datos ENUM

class AuxOrdenServicio(db.Model):
    __tablename__ = "auxOrdenServicio"
    id: Mapped[int] = mapped_column(primary_key=True)
    orden_id: Mapped[int] = mapped_column(ForeignKey("orden_de_trabajo.id_ot"), nullable = False)
    servicio_id: Mapped[int] = mapped_column(ForeignKey("servicio.id_service"), nullable = False)


class RolEnum(enum.Enum):
    MECANICO = 'Mecanico'
    CLIENTE = 'Cliente'
    

class User(db.Model):
    __tablename__ = "user"
    id_user: Mapped[int] = mapped_column(primary_key = True)
    nombre: Mapped[str] = mapped_column(String(80), nullable=False)
    identificacion: Mapped[int] = mapped_column(Integer, unique=True, nullable = False)
    password: Mapped[str] = mapped_column(String(12), nullable = False)
    telefono: Mapped[str] = mapped_column(String(11))
    email: Mapped[str] =  mapped_column(String(30), unique = True, nullable = False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False)
    foto_usuario: Mapped[str] = mapped_column(String(100))
    rol: Mapped[RolEnum] = mapped_column(Enum(RolEnum, name="rol_enum"), nullable=False)

    
class status(enum.Enum):
    INGRESADO = 'Ingresado'
    EN_PROCESO = 'En proceso'
    FINALIZADO = 'Finalizado'


class Orden_de_trabajo(db.Model):
    __tablename__ = "orden_de_trabajo"
    id_ot: Mapped[int] = mapped_column(primary_key = True)
    nombre_cliente: Mapped[str] = mapped_column(String(80), nullable=False)
    fecha_ingreso: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    estado_servicio: Mapped[status] = mapped_column(Enum(status, name="estado_orden"), nullable = False)
    fecha_final: Mapped[datetime.date] = mapped_column(Date, nullable = False)
    
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id_user"), nullable=False)
    vehiculo_id: Mapped[int] = mapped_column(ForeignKey("vehiculos.id_vehiculo"), nullable = False)
    mecanico_id: Mapped[int] = mapped_column(ForeignKey("user.id_user"), nullable = False)


class Vehiculos(db.Model):
    __tablename__ = 'vehiculos'
    id_vehiculo: Mapped[int] = mapped_column(primary_key = True)
    matricula: Mapped[str] = mapped_column(String(8), unique = True, nullable = False)
    marca: Mapped[str] = mapped_column(String(15), nullable = False)
    modelo: Mapped[str] = mapped_column(String(15), nullable = False)
    year: Mapped[int] = mapped_column(Integer, nullable = False)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id_user"), nullable = False)
  
class Servicio(db.Model):
    __tablename__ = 'servicio'
    id_service: Mapped[int] = mapped_column(primary_key = True)
    name_service: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)