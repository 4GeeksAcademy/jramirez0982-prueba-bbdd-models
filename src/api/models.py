from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, Enum
from sqlalchemy.orm import Mapped, mapped_column
import enum

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
class RolEnum(enum.Enum):
    INGRESADO = 'Ingresado'
    EN_CURSO = 'En curso'
    FINALIZADO = 'Finalizado'


class Usuarios(db.Model):
    __tablename__ = "usuarios"
    id: Mapped[int] = mapped_column(primary_key = True)
    nombre: Mapped[str] = mapped_column(String(80), nullable=False)
    identificacion: Mapped[int] = mapped_column(Integer, unique=True, nullable = False)
    password: Mapped[str] = mapped_column(String(12), nullable = False)
    telefono: Mapped[str] = mapped_column(String(11))
    email: Mapped[str] =  mapped_column(String(30), unique = True, Nullable = False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False)
    foto_usuario: Mapped[str] = mapped_column(str(100))
    rol: Mapped[RolEnum] = mapped_column(Enum(RolEnum), nullable=False)


class Orden_de_trabajo(db.Model):
    __tablename__ = "Orden_de_trabajo"
